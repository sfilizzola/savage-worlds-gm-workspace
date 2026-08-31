# Player character sheets — Operation Hinterland

One file per pregen, laid out to match the printed **Weird War II** character sheet (WW2 p.176). Mechanics are **SWADE Fifth Printing (2023)**; period names, MOS packages, and weapon/gear tables come from Weird War II and are rebuilt where they conflict with SWADE.

| File | Slot | Character | Print |
|---|---|---|---|
| `keene.md` | 1 | 1st Lt. Jack Keene (U.S.) | `print/keene.pdf` |
| `krajewski.md` | 2 | Sgt. Tomasz Krajewski (Polish) | `print/krajewski.pdf` |
| `vasseur.md` | 3 | Sgt. Hélène Vasseur (Free French) | `print/vasseur.pdf` |
| `lang.md` | 4 | Cpl. Beatrice "Bee" Lang (British) | `print/lang.pdf` |
| `voss.md` | Reserve | Cpl. Pieter Voss (Dutch) | `print/voss.pdf` |

Party overlap, team kit, German faces, and re-entry: `../characters.md`. Call letters: `../handouts/`.

**Table print:** one A4 from `print/` per player, plus the shared rules card `../handouts/player-quick-ref.pdf`. Rebuild with the workspace sheet printer (`tools/print-sheets/`) via `print/build_sheets.py` after a `.md` sheet change; keep `print/chars.json` in sync. Do not print 1949 E/O pay codes (BG-OH-007). Rank titles are period speech. Gender is not a table question.

## Sheet fields that are inactive tonight

The WW2 sheet still has these boxes. They are filled as unused, not as live rules:

| WW2 field | Why unused |
|---|---|
| Charisma | Removed in SWADE |
| Sanity | Adventure supernatural level `none` (WW2 pp.7, 93) |
| Rank (Officer/NCO) extra Benny / +2 Toughness | Old WW2 Edge; rank is flavor (WW2 p.21). SWADE **Command** is the leadership mechanic |
| National Identity, Demo Man, Medic!, Jump Qualified | Old WW2 Edges; not used |
| Conviction | SWADE Setting Rule not activated |
| Powers / Power Points | None |
