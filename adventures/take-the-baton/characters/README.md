# Player character sheets — Take the Baton

One file per pregen. Mechanics are SWADE Fifth Printing (2023) core only — `setting_modules: []`, no period or setting-specific gear tables.

| File | Slot | Character | Print |
|---|---|---|---|
| `marcus-webb.md` | 1 | Marcus Webb (Leg 1, lead-off) | `print/marcus-webb.pdf` |
| `renee-ortiz.md` | 2 | Renee Ortiz (Leg 2) | `print/renee-ortiz.pdf` |
| `toby-sharpe.md` | 3 | Toby Sharpe (Leg 3) | `print/toby-sharpe.pdf` |
| `dee-whitfield.md` | 4 | Dee Whitfield (Alternate) | `print/dee-whitfield.pdf` |
| `elle-kim.md` | Reserve | Elle Kim (team manager, now school nurse) | `print/elle-kim.pdf` |

Party overlap, connections, and re-entry: `../characters.md`.

**Table print:** one A4 per player from `print/`, built with the workspace sheet printer:

```text
python3 tools/print-sheets/render.py adventures/take-the-baton/characters/print/chars.json --pdf
```

Rebuild after any `.md` sheet change and keep `print/chars.json` in sync — the `.md` file is the mechanical source of truth.

## Sheet fields that are inactive tonight

| Field | Why unused |
|---|---|
| Charisma | Removed in SWADE |
| Weapons / Armor | No weapons or armor are part of this adventure's premise; all five sheets carry empty weapons lists |
| Conviction | SWADE Setting Rule not activated |
| Powers / Power Points | None |
