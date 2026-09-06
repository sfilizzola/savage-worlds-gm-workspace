# RUN.md printer

Turns an adventure `RUN.md` into A4 HTML (and optionally PDF) for paper at the table. A tablet should open the same paged PDF, not a reflowing notes view.

`RUN.md` is the file you edit. Do not hand-edit `print/RUN.html` or `print/RUN.pdf`. Do not put a RUN renderer inside an adventure.

## Use

From the workspace root:

```text
python3 tools/print-run/render.py adventures/<slug>/RUN.md
python3 tools/print-run/render.py adventures/<slug>/RUN.md --pdf
```

Default output for `adventures/<slug>/RUN.md` is `adventures/<slug>/print/RUN.html` (and `RUN.pdf` with `--pdf`). CSS is copied beside the HTML on each build.

`--pdf` uses Chrome headless, A4, no header/footer chrome. If Chrome is missing, the HTML is still written; print that file to A4 yourself (backgrounds on).

```text
python3 tools/print-run/render.py path/to/RUN.md --out-dir path/to/dir
```

## At-hand callouts

The `RUN.md` generation contract uses GitHub-style Markdown alerts for table-critical boards:

```markdown
> [!IMPORTANT]
> #### At-hand statistics
>
> **WATCHER** — Extra
> Attributes: ...

> [!TIP]
> #### At-hand rules
>
> Short procedure and authority.
```

Prefix every content line and internal blank line in each board with `>`, then leave a normal unquoted blank line before the next alert or heading. The printer gives statistics and rules distinct, keep-together cards; compatible Markdown viewers also highlight the source.

## NPC speech

Speech is tinted plum so the GM can find a voice mid-scene. Two carriers get that treatment:

```markdown
- **Spoken lines:** The watcher, if pressed: “Nobody comes up here.”

> “A longer beat the GM speaks as written.”
```

A `Spoken lines` field (list item or paragraph, attribution parenthetical allowed) becomes a tinted strip, and a blockquote that opens with the quotation mark becomes a tinted quote card. In both, the quoted words and any backticked foreign line are colored.

Quotes used for paraphrase, idiom, or a nickname stay black on purpose, so nothing prose gets mistaken for a line to speak.

## Tests

```text
python3 tools/print-run/test_print_run.py
```
