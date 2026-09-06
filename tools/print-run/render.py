#!/usr/bin/env python3
"""Print an adventure RUN.md as A4 HTML (and optionally PDF).

RUN.md remains the file you edit. This tool does not compile or rewrite it.

  python3 tools/print-run/render.py adventures/<slug>/RUN.md
  python3 tools/print-run/render.py adventures/<slug>/RUN.md --pdf
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

import mdhtml

TOOL_DIR = Path(__file__).resolve().parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def default_out_dir(run_path: Path) -> Path:
    path = run_path.expanduser()
    if not path.is_absolute():
        path = Path.cwd() / path
    parent = path.parent
    if parent.parent.name == "adventures" and path.name == "RUN.md":
        return parent / "print"
    return parent


def title_from(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        m = re.match(r"^#\s+(.*)$", line)
        if m:
            return m.group(1).strip()
    return fallback


def css_content(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def document(title: str, body: str) -> str:
    safe_title = html.escape(title, quote=True)
    css_title = css_content(title)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{safe_title}</title>
<link rel="stylesheet" href="run.css">
<style>
@page {{
  size: A4 portrait;
  margin: 14mm 12mm 18mm 12mm;
  @top-left {{
    content: "{css_title} · GM only";
    font-size: 8pt;
    color: #555;
  }}
  @bottom-right {{
    content: counter(page);
    font-size: 8pt;
    color: #555;
  }}
}}
</style>
</head>
<body>
<article class="run">
{body}
</article>
</body>
</html>
"""


def print_pdf(html_path: Path) -> None:
    chrome = Path(CHROME)
    if not chrome.is_file():
        raise SystemExit(f"Chrome not found at {CHROME}. Print the HTML to A4 instead.")
    pdf_path = html_path.with_suffix(".pdf")
    subprocess.run(
        [
            str(chrome),
            "--headless",
            "--disable-gpu",
            "--virtual-time-budget=8000",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            html_path.as_uri(),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print("wrote", pdf_path.name)


def build(src: Path, out_dir: Path, pdf: bool) -> None:
    text = src.read_text(encoding="utf-8")
    if not re.search(r"^#", text, re.M):
        print("warning: no headings in", src, file=sys.stderr)
    title = title_from(text, src.stem)
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(TOOL_DIR / "run.css", out_dir / "run.css")
    html_path = out_dir / "RUN.html"
    html_path.write_text(document(title, mdhtml.convert(text)), encoding="utf-8")
    print("wrote", html_path.name)
    if pdf:
        print_pdf(html_path)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Build an A4 two-column print of RUN.md."
    )
    parser.add_argument("run", type=Path, help="Path to RUN.md")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Output directory (default: adventures/<slug>/print/ for that path)",
    )
    parser.add_argument("--pdf", action="store_true", help="Also print A4 PDF via Chrome")
    args = parser.parse_args(argv)
    src = args.run.expanduser()
    if not src.is_absolute():
        src = (Path.cwd() / src).resolve()
    else:
        src = src.resolve()
    if not src.is_file():
        raise SystemExit(f"No such file: {src}")
    out = (args.out_dir or default_out_dir(src)).resolve()
    build(src, out, args.pdf)


if __name__ == "__main__":
    main()
