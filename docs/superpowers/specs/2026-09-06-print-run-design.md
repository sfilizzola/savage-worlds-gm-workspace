# Print RUN.md as A4 PDF - Approved Design

## Purpose

Give the GM a **paper-first table packet**: an A4 two-column PDF generated from an adventure’s `RUN.md`. A tablet is supported only as the same paged object (open the PDF or HTML and flip pages), not as a reflowing notes app.

`RUN.md` remains the file the GM and agents edit. Modular adventure files remain prep canon (`GM.md`). The PDF is a generated print of `RUN.md`, not a second story source.

## Decision

**Workspace HTML + Chrome printer**, same family as `tools/print-sheets/`.

- Physical object: A4 portrait stack (binder or clipboard), not A5 booklet, not situation cards.
- Layout: two columns, ~9–10pt serif, story-point titles spanning both columns.
- Tool: `tools/print-run/` from day one (every adventure `RUN.md`, not Hinterland-only).
- Engine: Markdown → HTML + `run.css` → optional headless Chrome A4 PDF.
- No renderer inside an adventure directory (`AGENTS.md` already forbids that for sheets).

## Scope

**In scope**

- CLI that takes a path to `RUN.md` and writes HTML; `--pdf` also writes PDF.
- Shared print CSS: A4, two columns, running title, page number, GM-only highlight.
- Heuristic mapping from existing skeleton labels (Mood, GM Note, tables, Extra/Wild Card blocks) onto keep-together cards.
- Default output `adventures/<slug>/print/RUN.html` and `RUN.pdf` when the input is `adventures/<slug>/RUN.md`.
- Docs: `tools/print-run/README.md`, a row in `tools/README.md`, a short `HOW_TO_USE.md` note, one `AGENTS.md` line pointing at the tool.
- Fixture test on a tiny fake `RUN.md` plus one manual Hinterland skim.

**Out of scope**

- Changing `templates/adventure/SKELETON.md` or how `RUN.md` is compiled.
- A5 booklet imposition, duplex signatures, or card-per-situation packs.
- Form-fillable Acrobat checkboxes.
- Maps, player handouts, call letters, pregen sheets (existing printers stay).
- Rewriting `RUN.md` into a print-specific twin file.
- Pixel-diff or visual regression of PDFs.
- Pandoc, Typst, or LaTeX.

## Architecture

```text
adventures/<slug>/RUN.md          # edit this (table document)
        |
        v
tools/print-run/render.py
  + run.css
        |
        +-- Markdown subset → HTML (classes for mood, gm-note, stats, tables)
        +-- copy run.css beside HTML
        +-- optional: Chrome --print-to-pdf A4, no UI header/footer
        |
        v
adventures/<slug>/print/RUN.html
adventures/<slug>/print/RUN.pdf   # generated; do not hand-edit
```

Reuse the Chrome discovery pattern already in `tools/print-sheets/render.py` (macOS Chrome path; HTML fallback if Chrome is missing).

## Components

| Unit | Does | Used how | Depends on |
|---|---|---|---|
| `render.py` | Read `RUN.md`, emit HTML, optionally PDF | CLI | stdlib + Chrome for PDF |
| `run.css` | A4 page, two columns, cards, print colors | Linked from HTML; copied next to output | nothing |
| GFM-subset converter | Headings, paragraphs, lists, tables, emphasis, inline code, blockquotes | Inside `render.py` | stdlib only (no Pandoc, no `markdown` package in v1) |
| `testdata/mini-run.md` | One story point covering every mapped pattern | Tests | none |

Do not add `adventures/<slug>/print/build_run.py` wrappers in v1. Call the workspace tool with the path to `RUN.md`.

## Page anatomy

- `@page` A4 portrait, modest margins (~12–14mm). Browser print chrome off.
- Header (CSS margin box or a repeating HTML header): adventure title taken from the first `#` heading or the filename, plus `GM only`.
- Footer: page number.
- Body: `column-count: 2`, ~9–10pt system serif (`Georgia`, `Palatino`, `Times`). Do not require `print-sheets` webfonts in v1.
- Every `h2` gets class `section-banner`: `column-span: all`, left rule, `break-after: avoid`.
- Long story points **may split** across columns/pages. Do not force `break-inside: avoid` on a whole story point (Hinterland blocks are too large; that would leave huge empty columns).
- Keep-together (`break-inside: avoid` + `page-break-inside: avoid`): Mood card, GM Note strip, short tables, each stat-block card.
- Ink: black plus one pale yellow GM-only strip. Acceptable on B&W (yellow → light gray). No parchment textures, no full-bleed color.

## Markdown mapping

The printer does not require new syntax. It classifies after HTML conversion (or during walk of block elements):

| Source pattern | Print treatment |
|---|---|
| `#` title | Document title / header string |
| `## …` | Story-point or section banner, full width |
| `###` / `####` | Nested headings inside the column flow |
| Paragraph or list item whose visible text starts with `GM Note` | Yellow strip |
| `Mood (table)` heading plus Climate / See / Hear / Feel bullets | One Mood card; stop at the next skeleton field (`Goal:`, `Situation now:`, etc.) |
| GFM table | Compact table; keep-together if it fits about one column |
| A block that contains `Wild Card` or `Extra` and a following `Attributes:` line | Stat-block card |
| Quoted spoken lines | Ordinary italic or quoted body; not a read-aloud box |
| Everything else | Normal flow |

Unrecognized structure still prints as HTML. Never fail the build because a label is slightly off.

## CLI

```text
python3 tools/print-run/render.py adventures/<slug>/RUN.md
python3 tools/print-run/render.py adventures/<slug>/RUN.md --pdf
python3 tools/print-run/render.py path/to/RUN.md --out-dir path/to/dir
```

- Default `--out-dir` for `adventures/<slug>/RUN.md` is `adventures/<slug>/print/`.
- Any other path: write `RUN.html` / `RUN.pdf` into `--out-dir` if given, otherwise into the same directory as the markdown file.
- Without `--pdf`: HTML only, exit 0 on success.
- With `--pdf`: write HTML first; if Chrome is missing or the PDF step fails, keep the HTML, message on stderr (same tone as print-sheets), exit non-zero.
- Missing or unreadable input: exit non-zero, write nothing.
- File with no headings: still emit PDF/HTML of the body; warn on stderr.

## Error handling

| Case | Behavior |
|---|---|
| Missing `RUN.md` | Non-zero; no output files |
| Chrome missing + `--pdf` | HTML written; non-zero |
| Unclassified markdown | Print anyway |
| Empty-looking file | Warn; still emit |

## Testing

- Fixture `tools/print-run/testdata/mini-run.md` includes: one `## Story Point`, Mood four-lines, a GM Note, a Discoverable table, one Extra stat block, and a plain paragraph.
- Automated: render to a temp dir and assert HTML contains the expected classes (`section-banner`, `gm-note`, `mood`, `stat-block`, a `<table>`).
- Manual once per implementation: generate Operation Hinterland `RUN.md` and skim First 15 minutes, one story point with stats, and the NPC appendix. Fix CSS if a banner or GM Note is unreadable; do not block on perfect column balancing.

## Documentation

- `tools/print-run/README.md`: command, output paths, Chrome requirement, “edit RUN.md not the PDF.”
- `tools/README.md`: add a row next to print-sheets.
- `HOW_TO_USE.md`: table-print paragraph for RUN, distinct from pregen sheets.
- `AGENTS.md`: print RUN with `tools/print-run/`; do not put a RUN renderer inside an adventure.

## Constraints carried from the workspace

- English table material unless the adventure declares otherwise.
- Do not reproduce long copyrighted SWADE text in CSS comments or sample fixture; the fixture uses fake names and fake page cites.
- Generated `print/RUN.pdf` may be gitignored or committed later; v1 does not require committing binary PDFs. HTML/CSS in `tools/print-run/` is source.
