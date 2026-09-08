# Pregen sheet printer

Prints filled A4 SWADE character sheets as HTML (and optionally PDF). This is **not** a character generator: it does not roll traits, spend points, or apply MOS packages.

Markdown character sheets remain the mechanical source of truth. `chars.json` is the print extract.

## Use

From the workspace root.

Standalone adventure pregens:

```text
python3 tools/print-sheets/render.py adventures/<slug>/characters/print/chars.json
python3 tools/print-sheets/render.py adventures/<slug>/characters/print/chars.json --who keene --pdf
```

Campaign party:

```text
python3 tools/print-sheets/render.py campaigns/<campaign-slug>/characters/print/chars.json
python3 tools/print-sheets/render.py campaigns/<campaign-slug>/characters/print/chars.json --who keene --pdf
```

Output stays beside the input: sheets are written into the same character `print/` directory that holds the `chars.json` you passed, unless you pass `--out`.

In a campaign, the party's `.md` sheets and `characters/print/chars.json` at the campaign root are canonical. A child adventure's `characters.md` carries night hooks and links to those sheets; it is not a second mechanical copy and is not what you print.

From an adventure that already has a wrapper (Operation Hinterland):

```text
python3 adventures/operation-hinterland/characters/print/build_sheets.py
python3 adventures/operation-hinterland/characters/print/build_sheets.py --who keene --pdf
```

`--pdf` uses Chrome headless, A4, no header/footer. If Chrome is missing, print the HTML the same way.

## Character files

Same layout wherever the sheets live — a standalone adventure's `characters/` or a campaign's canonical `characters/`:

```text
<path-to-characters>/
├── <name>.md            # mechanical source of truth
├── <name>_portrait.png  # optional; referenced from chars.json
└── print/
    ├── chars.json       # print extract for this tool
    ├── build_sheets.py  # optional wrapper; calls this tool
    ├── <id>.html        # generated
    └── <id>.pdf         # generated
```

Copy `sheet.css` is written next to the HTML on each build. Fonts live in `tools/print-sheets/fonts/` and are symlinked into the output folder when needed.

After editing a `.md` sheet, update the `chars.json` beside it to match, then rebuild.

## JSON shape

Top-level keys: `sheet` (masthead, headings, footer, shared team kit) and `characters` (one object per pregen). Tags are a list of `{label, value}` so a Weird War II file can use Rank / MOS / Nationality / Service and another adventure can use different labels.

See `adventures/operation-hinterland/characters/print/chars.json` for a complete example.

## Case-file blocks (optional)

These keys are off unless present, so an existing `chars.json` prints exactly as before. They exist to make an investigative sheet read like a personnel file; a war sheet can ignore all of them.

Per character:

| Key | Effect |
|---|---|
| `portrait` | `{src, caption, sub}`. Mounts the image with photo corners and a caption strip in a left column of the identity row. `src` is relative to the `chars.json`, so a portrait beside the `.md` sheets is `../name.png`. |
| `stamp` | `{text, sub}` or a plain string. Rotated rubber stamp under the tags. Flavour only — never place it over numbers the GM must read. |
| `dossier` | List of `[label, value]`. Description-and-service fields beside the photo. **An empty value prints a line to fill in by hand**, which is how to carry a field the campaign has not established. |
| `threads` | List of strings with a checkbox each. An empty string prints a blank write-in row. |
| `notes_lines` | Overrides `sheet.notes_lines` for one character. |

In `sheet`:

| Key | Effect |
|---|---|
| `classification` | Small outlined chip under the file line (for example `Confidential · Investigations Division`). |
| `dossier_heading` | Heading above the `dossier` fields. |
| `notes_heading`, `notes_lines` | Ruled writing panel. `notes_lines: 0` omits it. |
| `threads_heading` | Heading above the `threads` list. |
| `signature` | List of labels, each printed as a signature rule (for example `Detective (signature)`, `Reviewed by`, `Date`). |

## Translated sheets

The printer's structural labels default to English and can be overridden in `sheet`, so a table can print the same character in another language without a second renderer. The markdown character file stays the mechanical source of truth, and numbers are never translated.

| Key | Default |
|---|---|
| `lang` | `en` — sets the `<html lang>` attribute |
| `attributes_heading` | `Attributes` |
| `hindrances_heading` | `Hindrances` |
| `edges_heading` | `Edges` |
| `derived_labels` | `["Pace", "Parry", "Toughness"]` |
| `track_labels` | `["Wounds", "Fatigue"]` |
| `incap_label` | `INC` |
| `weapon_columns` | `["Weapon", "Range", "RoF", "Dmg", "Notes"]` |
| `load_labels` | `["Carried", "Limit", "Encumbrance"]` |
| `bennies_word` | `Bennies` — the word the three tick boxes follow in `bennies` |

Keep the translation in its own extract beside the English one and give its characters distinct ids, so the two sheets do not overwrite each other:

```text
python3 tools/print-sheets/render.py campaigns/no-further-action/characters/print/chars.pt-BR.json --pdf
```

Translated prose runs longer than English and can push a one-page sheet onto a second page. Measure the translated sheet separately.

## Checking that a sheet still fits one page

A4 portrait with the stylesheet's 7mm margins leaves **283mm** of printable height. Adding a portrait or case-file blocks can push a sheet onto a second page, and the overflow is easy to miss in a PDF viewer.

```text
python3 tools/print-sheets/measure.py campaigns/<campaign-slug>/characters/print/<id>.html
```

It prints the height of each block, the total, and the remaining slack. Keep a few millimetres spare — font metrics drift between Chrome versions. The identity row is usually governed by whichever is taller, the photo column or the name-and-dossier column, so shrinking the photo below the dossier height buys nothing.
