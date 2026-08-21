from pathlib import Path
from PIL import Image

SOURCE = Path(r"C:\Users\ASUS\Documents\Codex\2026-08-21\hatch-pet-c-users-asus-codex-2\outputs\paimeng-pet\spritesheet.webp")
OUT = Path(r"C:\Users\ASUS\Documents\ChatGPT\原神派萌宠物\outputs\paimeng-pet-slow\spritesheet-preclean.png")

CELL_W, CELL_H = 192, 208
COLS, ROWS = 8, 11

# Preserve the v2 contract while holding selected key poses longer.
MAPS = {
    0: [0, 0, 1, 2, 3, 4, 6],     # idle: hold the calm opening pose
    1: [0, 1, 2, 3, 4, 5, 6, 6],
    2: [0, 1, 2, 3, 4, 5, 6, 6],
    3: [0, 1, 2, 2],
    4: [0, 1, 2, 3, 3],
    5: [0, 1, 2, 3, 4, 5, 6, 6],
    6: [0, 1, 2, 3, 4, 4],
    7: [0, 1, 2, 3, 4, 4],
    8: [0, 1, 2, 3, 4, 4],
}

with Image.open(SOURCE) as source:
    source = source.convert("RGBA")
    if source.size != (COLS * CELL_W, ROWS * CELL_H):
        raise SystemExit(f"unexpected source size: {source.size}")
    # Start from the already despilled atlas so unused transparent cells keep
    # their clean hidden RGB values and the app's effective slot usage stays intact.
    output = source.copy()
    for row in range(ROWS):
        mapping = MAPS.get(row, list(range(COLS)))
        used = len(mapping)
        for col in range(COLS):
            if col >= used:
                continue
            src_col = mapping[col]
            box = (src_col * CELL_W, row * CELL_H, (src_col + 1) * CELL_W, (row + 1) * CELL_H)
            output.paste(source.crop(box), (col * CELL_W, row * CELL_H))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    output.save(OUT, "PNG")
print(OUT)
