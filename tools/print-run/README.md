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

## Tests

```text
python3 tools/print-run/test_print_run.py
```
