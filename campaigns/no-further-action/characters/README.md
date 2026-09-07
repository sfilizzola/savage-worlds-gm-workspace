# Campaign characters

This directory is the **canonical** home for this campaign's player characters.

- Mechanical source of truth: `lilly-dawson.md` (1986 Novice). 1998 Seasoned and 2016 Veteran sheets will live here when rebuilt.
- Print extract: `print/chars.json`
- Portrait: `lily_portrait_1986.png` (1986). Referenced from the print extract as `../lily_portrait_1986.png`.

```text
python3 tools/print-sheets/render.py campaigns/no-further-action/characters/print/chars.json --pdf
python3 tools/print-sheets/measure.py campaigns/no-further-action/characters/print/lilly.html
```

Lilly's sheet prints as an Ashgrove PD personnel file: mounted photo, description-and-service fields, a disposition stamp, ruled case notes, open threads, and a signature strip. See `tools/print-sheets/README.md` for those keys.

Two rules for the case-file blocks:

- **Player-facing only.** `dossier` may carry what Lilly knows. `threads` on this sheet are blank write-in rows. No GM Correction material, no prepared outcomes for an unplayed night.
- **Do not invent canon to fill a field.** A field the campaign has not established (height, shield number, partner) takes an empty value, which prints a line to fill in by hand.

The extract's fields must stay consistent with `lilly-dawson.md`. After editing the `.md`, update `print/chars.json`, rebuild, and re-run `measure.py` — the sheet keeps only about 4mm of slack on one A4 page.

Child adventures **link** here. Do **not** duplicate full mechanical sheets inside a child adventure.
