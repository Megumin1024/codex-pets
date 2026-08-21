"""Create a slower v2 atlas by holding selected standard-row poses.

Usage: edit SOURCE and OUT, then run with the bundled Python runtime.
The source must already be a validated, despilled 8x11 atlas.
"""
from pathlib import Path
from PIL import Image

SOURCE = Path("final/atlas-extended.webp")
OUT = Path("outputs/paimeng-pet-slow/spritesheet-preclean.png")
CELL_W, CELL_H = 192, 208
COLS, ROWS = 8, 11

# Preserve the destination slot count. Adjust only standard rows 0-8.
FRAME_MAPS = {
    0: [0, 0, 1, 2, 3, 4, 6],
    1: [0, 1, 2, 3, 4, 5, 6, 6],
    2: [0, 1, 2, 3, 4, 5, 6, 6],
    3: [0, 1, 2, 2],
    4: [0, 1, 2, 3, 3],
    5: [0, 1, 2, 3, 4, 5, 6, 6],
    6: [0, 1, 2, 3, 4, 4],
    7: [0, 1, 2, 3, 4, 4],
    8: [0, 1, 2, 3, 4, 4],
}

with Image.open(SOURCE) as opened:
    source = opened.convert("RGBA")
    if source.size != (COLS * CELL_W, ROWS * CELL_H):
        raise SystemExit(f"Expected 1536x2288, got {source.size}")
    output = source.copy()
    for row, mapping in FRAME_MAPS.items():
        for col, source_col in enumerate(mapping):
            box = (source_col * CELL_W, row * CELL_H, (source_col + 1) * CELL_W, (row + 1) * CELL_H)
            output.paste(source.crop(box), (col * CELL_W, row * CELL_H))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    output.save(OUT, "PNG")
print(OUT)
