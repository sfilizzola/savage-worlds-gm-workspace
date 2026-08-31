#!/usr/bin/env python3
"""Rebuild Operation Hinterland print sheets via the workspace sheet printer.

  python3 build_sheets.py
  python3 build_sheets.py --who keene --pdf

Engine: tools/print-sheets/render.py
Data: chars.json (print extract). Mechanical source of truth remains the .md sheets.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def workspace_root(start: Path) -> Path:
    for path in [start, *start.parents]:
        candidate = path / "tools" / "print-sheets" / "render.py"
        if candidate.is_file():
            return path
    raise SystemExit("Could not find tools/print-sheets/render.py from this adventure.")


def main() -> None:
    root = workspace_root(HERE)
    cmd = [
        sys.executable,
        str(root / "tools" / "print-sheets" / "render.py"),
        str(HERE / "chars.json"),
        "--out",
        str(HERE),
        *sys.argv[1:],
    ]
    raise SystemExit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
