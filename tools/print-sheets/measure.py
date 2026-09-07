#!/usr/bin/env python3
"""Report the printed height of a generated sheet, block by block.

A4 portrait with the stylesheet's 7mm margins leaves 283mm of printable
height. A sheet taller than that spills onto a second page, so keep a few
millimetres of slack for font-metric drift between Chrome versions.

  python3 tools/print-sheets/measure.py <path-to>/lilly.html
"""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BUDGET_MM = 283.0

PROBE = """<style>.sheet{min-height:0}.ident{align-items:start}</style>
<script>window.addEventListener('load',function(){
  var mm=function(el){return (el.getBoundingClientRect().height/96*25.4).toFixed(1)};
  var sheet=document.querySelector('.sheet');
  var out=['TOTAL='+mm(sheet)];
  [].forEach.call(sheet.children,function(c){
    out.push((c.className||c.tagName).split(' ')[0]+'='+mm(c));
  });
  ['.photo','.who','.side','.frame','.photo figcaption','.dossier',
   '.thread-list','.rules'].forEach(function(sel){
    var el=document.querySelector(sel);
    if(el){out.push(sel+'='+mm(el));}
  });
  document.title=out.join('|');
});</script>
</head>"""


def measure(html_path: Path) -> list[str]:
    probe_path = html_path.with_name(f"_measure_{html_path.name}")
    probe_path.write_text(
        html_path.read_text(encoding="utf-8").replace("</head>", PROBE),
        encoding="utf-8",
    )
    try:
        result = subprocess.run(
            [
                CHROME,
                "--headless",
                "--disable-gpu",
                "--virtual-time-budget=6000",
                "--dump-dom",
                probe_path.as_uri(),
            ],
            capture_output=True,
            text=True,
            check=True,
        )
    finally:
        probe_path.unlink(missing_ok=True)
    found = re.search(r"<title>(.*?)</title>", result.stdout, re.S)
    if not found:
        raise SystemExit("Could not read measurements from Chrome.")
    return found.group(1).split("|")


def main() -> None:
    parser = argparse.ArgumentParser(description="Measure a generated sheet's height.")
    parser.add_argument("html", type=Path, help="Path to a generated sheet HTML file")
    args = parser.parse_args()
    path = args.html.resolve()
    if not path.is_file():
        raise SystemExit(f"No such file: {path}")

    parts = measure(path)
    total = float(parts[0].split("=")[1])
    for part in parts:
        print(part.replace("=", ": "))
    slack = BUDGET_MM - total
    verdict = "fits" if slack >= 0 else "OVERFLOWS"
    print(f"\nbudget: {BUDGET_MM}mm · slack: {slack:+.1f}mm · {verdict}")


if __name__ == "__main__":
    main()
