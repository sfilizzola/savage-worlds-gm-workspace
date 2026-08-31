# Pregen sheet printer

Prints filled A4 SWADE character sheets as HTML (and optionally PDF). This is **not** a character generator: it does not roll traits, spend points, or apply MOS packages.

Markdown character sheets in the adventure remain the mechanical source of truth. `chars.json` is the print extract.

## Use

From the workspace root:

```text
python3 tools/print-sheets/render.py adventures/<slug>/characters/print/chars.json
python3 tools/print-sheets/render.py adventures/<slug>/characters/print/chars.json --who keene --pdf
```

From an adventure that already has a wrapper (Operation Hinterland):

```text
python3 adventures/operation-hinterland/characters/print/build_sheets.py
python3 adventures/operation-hinterland/characters/print/build_sheets.py --who keene --pdf
```

`--pdf` uses Chrome headless, A4, no header/footer. If Chrome is missing, print the HTML the same way.

## Adventure files

```text
adventures/<slug>/characters/
├── <name>.md            # mechanical source of truth
└── print/
    ├── chars.json       # print extract for this tool
    ├── build_sheets.py  # optional wrapper; calls this tool
    ├── <id>.html        # generated
    └── <id>.pdf         # generated
```

Copy `sheet.css` is written next to the HTML on each build. Fonts live in `tools/print-sheets/fonts/` and are symlinked into the output folder when needed.

After editing a `.md` sheet, update that adventure's `chars.json` to match, then rebuild.

## JSON shape

Top-level keys: `sheet` (masthead, headings, footer, shared team kit) and `characters` (one object per pregen). Tags are a list of `{label, value}` so a Weird War II file can use Rank / MOS / Nationality / Service and another adventure can use different labels.

See `adventures/operation-hinterland/characters/print/chars.json` for a complete example.
