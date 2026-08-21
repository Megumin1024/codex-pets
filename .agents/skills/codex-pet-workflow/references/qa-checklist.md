# QA Checklist

## Before generation

- [ ] Reference images are copied into the run directory.
- [ ] Canonical base has one centered full-body character.
- [ ] Identity features and palette are written down.
- [ ] Chroma key is recorded.

## Standard rows

- [ ] idle is calm and visibly animated.
- [ ] running-right and running-left face the correct screen direction.
- [ ] waving uses a hand pose only.
- [ ] jumping has no ground shadow or impact effect.
- [ ] failed is readable without detached symbols.
- [ ] waiting differs from idle.
- [ ] running shows task work, not literal jogging.
- [ ] review shows focus without invented props.
- [ ] Every used frame is complete, separated, and uncropped.

## Look rows

- [ ] 000 visibly reads up.
- [ ] 090 visibly reads screen-right.
- [ ] 180 visibly reads down.
- [ ] 270 visibly reads screen-left.
- [ ] Diagonals follow the clockwise order without reversal.
- [ ] Direction changes use facial/head mechanics, not whole-sprite rotation.
- [ ] `direction-semantics.json` has all 16 entries.

## Deterministic checks

- [ ] One despill/transparent cleanup pass completed.
- [ ] v2 validator returns `ok: true`.
- [ ] Dimensions are exactly `1536×2288`.
- [ ] Mode is RGBA.
- [ ] Transparent RGB residue is zero.
- [ ] Unused standard cells are empty.
- [ ] Final package contains `pet.json` and `spritesheet.webp`.

## Human review

- [ ] Contact sheet inspected at normal pet size.
- [ ] Motion previews do not show size popping or reversed timing.
- [ ] Direction QA sheet inspected independently.
- [ ] Any warning is recorded rather than silently ignored.
