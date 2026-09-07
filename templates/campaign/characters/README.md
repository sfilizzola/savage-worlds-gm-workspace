# Campaign characters

This directory is the **canonical** home for this campaign's player characters.

- Keep one `.md` sheet per PC as the mechanical source of truth.
- Put the print extract in `characters/print/chars.json`.
- Rebuild A4 sheets with the workspace printer (HTML/PDF printer, not a generator):

```text
python3 tools/print-sheets/render.py campaigns/<campaign-slug>/characters/print/chars.json
```

Child adventures **link** to these sheets. A child's `characters.md` may hold **night hooks** (why this PC is in tonight's premise, spotlight, connections that matter this session). Do **not** duplicate full mechanical sheets inside a child adventure.

Pregenerated and player-supplied parties both live here when they are this table's ongoing characters. Replacement or reserve pregens for the campaign belong here as well.
