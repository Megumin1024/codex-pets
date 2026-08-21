# Codex Pet v2 Contract

## Atlas

- Format: PNG or WebP.
- Mode: RGBA with transparent background.
- Size: `1536×2288`.
- Grid: 8 columns × 11 rows.
- Cell: `192×208`.
- `spriteVersionNumber` must be `2`.
- Rows 0–8 are standard actions; rows 9–10 are the 16 look directions.
- The 8×9 `1536×1872` atlas is intermediate only.

## Direction order

Row 9: `000, 022.5, 045, 067.5, 090, 112.5, 135, 157.5`.

Row 10: `180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5`.

`000` is up, not neutral/front. Neutral/front is the no-vector dead zone and falls back to idle.

## Manifest

```json
{
  "id": "pet-name",
  "displayName": "Pet Name",
  "description": "One short sentence.",
  "spriteVersionNumber": 2,
  "spritesheetPath": "spritesheet.webp"
}
```

## Speed

There is no documented generic speed or FPS field in the v2 manifest. A slower variant must be implemented by changing standard-row frame selection/holds while preserving the atlas contract, then re-running transparency and atlas validation.
