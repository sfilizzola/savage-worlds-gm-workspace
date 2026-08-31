# Print sheets — Operation Hinterland

Filled A4 personnel files for the table. Same fields as the Weird War II sheet (WW2 p.176), SWADE numbers, no unused boxes (Charisma, Sanity, Conviction, powers). Not a reproduction of the copyrighted form art.

| File | Who | When |
|---|---|---|
| `keene.pdf` | 1st Lt. Jack Keene | Slot 1 |
| `krajewski.pdf` | Sgt. Tomasz Krajewski | Slot 2 |
| `vasseur.pdf` | Sgt. Hélène Vasseur | Slot 3 |
| `lang.pdf` | Cpl. Beatrice "Bee" Lang | Slot 4 |
| `voss.pdf` | Cpl. Pieter Voss | Reserve / fifth / re-entry |

Print **one A4 per player**. Put `../../handouts/player-quick-ref.pdf` beside it.

Source of truth remains the `.md` sheets in the parent folder. Print data is `chars.json`. Rebuild with the workspace sheet printer:

```text
python3 build_sheets.py
python3 build_sheets.py --who all --pdf
```

That wrapper calls [`tools/print-sheets/`](../../../../tools/print-sheets/README.md). Direct:

```text
python3 ../../../../tools/print-sheets/render.py chars.json --pdf
```

Do not print 1949 E/O pay codes. Rank titles are period speech. Gender is not a table question.
