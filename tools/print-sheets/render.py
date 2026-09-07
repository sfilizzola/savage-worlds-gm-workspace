#!/usr/bin/env python3
"""Print SWADE pregen sheets as A4 HTML (and optionally PDF).

This is a sheet printer, not a character generator. Stats, Edges, and gear
come from a JSON file that lives with the character sheets it prints, in a
standalone adventure or at a campaign root. Markdown character sheets remain
the mechanical source of truth. Output lands beside the JSON you pass.

  python3 tools/print-sheets/render.py <path-to-characters>/print/chars.json
  python3 tools/print-sheets/render.py adventures/<slug>/characters/print/chars.json --pdf
  python3 tools/print-sheets/render.py campaigns/<campaign-slug>/characters/print/chars.json --pdf
  python3 tools/print-sheets/render.py path/to/chars.json --who keene --pdf
"""

from __future__ import annotations

import argparse
import html
import json
import shutil
import subprocess
from pathlib import Path

TOOL_DIR = Path(__file__).resolve().parent
STEPS = ["4", "6", "8", "10", "12"]
DIE_RANK = {"d4": 0, "d6": 1, "d8": 2, "d10": 3, "d12": 4}
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

SHEET_DEFAULTS = {
    "title_suffix": "",
    "op": "",
    "file": "Personnel file",
    "meta": [],
    "skills_heading": "Skills · unskilled d4−2",
    "skills_footnote": "* Core skill. Core skills start at d4.",
    "weapons_heading": "Weapons",
    "gear_heading": "Gear",
    "you_label": "You",
    "play_label": "At the table",
    "footer_left": "",
    "footer_right": "",
    "reserve_banner": "Reserve pregen",
    "team_kit": "",
    "bennies": "Bennies · start 3 · tick when spent",
}


def e(value: object) -> str:
    return html.escape(str(value), quote=False)


def track(die: str) -> str:
    n = DIE_RANK[die]
    cells = []
    for i, label in enumerate(STEPS):
        cls = "on" if i <= n else ""
        cells.append(f'<i class="{cls}">{label}</i>')
    return f'<span class="track">{"".join(cells)}</span>'


def skill_row(name: str, die: str, mod: str) -> str:
    extra = f'<span class="mod">{e(mod)}</span>' if mod else "<span></span>"
    return (
        f'<div class="skill-row"><span class="k">{e(name)}</span>'
        f'{extra}<span class="die">{e(die)}</span></div>'
    )


def render(ch: dict, sheet: dict) -> str:
    title = ch["name"]
    if sheet["title_suffix"]:
        title = f'{ch["name"]} — {sheet["title_suffix"]}'
    meta_lines = sheet["meta"]
    if isinstance(meta_lines, str):
        meta_html = e(meta_lines)
    else:
        meta_html = "<br>".join(e(line) for line in meta_lines)

    attrs = "".join(
        f'<div class="attr-row"><span class="k">{e(n)}</span>{track(d)}'
        f'<span class="die">{e(d)}</span></div>'
        for n, d in ch["attrs"]
    )
    mid = len(ch["skills"]) // 2 + len(ch["skills"]) % 2
    left = "".join(skill_row(*s) for s in ch["skills"][:mid])
    right = "".join(skill_row(*s) for s in ch["skills"][mid:])
    hind = "".join(
        f'<div class="he"><div class="t">{e(n)} · {e(t)}</div>'
        f'<div class="d">{e(d)}</div></div>'
        for n, t, d in ch["hindrances"]
    )
    edges = "".join(
        f'<div class="he"><div class="t">{e(n)}</div><div class="d">{e(d)}</div></div>'
        for n, d in ch["edges"]
    )
    weap = "".join(
        f"<tr><td>{e(w)}</td><td>{e(r)}</td><td>{e(rof)}</td>"
        f"<td>{e(dmg)}</td><td>{e(notes)}</td></tr>"
        for w, r, rof, dmg, notes in ch["weapons"]
    )
    gear = "".join(
        f'<li><span>{e(n)}</span><span class="w">{e(w)}</span></li>'
        for n, w in ch["gear"]
    )
    tags = "\n".join(
        f"        <div><dt>{e(t['label'])}</dt><dd>{e(t['value'])}</dd></div>"
        for t in ch.get("tags", [])
    )
    parry_cls = "statbox alert" if ch.get("parry_alert") else "statbox"
    load_cls = "load alert" if ch.get("encumbered") else "load"
    banner = (
        f'<div class="reserve-banner">{e(sheet["reserve_banner"])}</div>'
        if ch.get("reserve")
        else ""
    )
    pace_note = ch.get("pace_note") or "12 yards / round"
    team = ch.get("ammo", "")
    team_kit = sheet.get("team_kit") or ""
    you = ch.get("you") or ""
    play = ch.get("play") or ""
    you_block = ""
    if you or play:
        you_block = f"""
    <div class="you">
      <div>
        <div class="lbl">{e(sheet["you_label"])}</div>
        <p>{e(you)}</p>
      </div>
      <div>
        <div class="lbl">{e(sheet["play_label"])}</div>
        <p>{e(play)}</p>
      </div>
    </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>{e(title)}</title>
  <link rel="stylesheet" href="sheet.css" />
</head>
<body>
  <article class="sheet">
    <header class="mast">
      <div>
        <div class="op">{e(sheet["op"])}</div>
        <div class="file">{e(sheet["file"])}</div>
      </div>
      <div class="meta">{meta_html}</div>
    </header>

    {banner}
    <div class="ident">
      <div>
        <h1 class="name">{e(ch["name"])}</h1>
        <div class="role">{e(ch["role"])}</div>
      </div>
      <dl class="tags">
{tags}
      </dl>
    </div>

    <div class="row-stats">
      <div class="panel">
        <h2>Attributes</h2>
        <div class="body">{attrs}</div>
      </div>
      <div>
        <div class="derived">
          <div class="statbox"><div class="lbl">Pace</div><div class="val">{e(ch["pace"])}</div><div class="note">{e(pace_note)}</div></div>
          <div class="{parry_cls}"><div class="lbl">Parry</div><div class="val">{e(ch["parry"])}</div><div class="note">{e(ch["parry_note"])}</div></div>
          <div class="statbox"><div class="lbl">Toughness</div><div class="val">{e(ch["tough"])}</div><div class="note">{e(ch["tough_note"])}</div></div>
        </div>
        <div class="bennies">{bennies_html(sheet["bennies"])}</div>
      </div>
      <div>
        <div class="tracks-row">
          <div class="woundbox">
            <div class="lbl">Wounds</div>
            <div class="boxes">
              <div class="tick"><span class="cap">−1</span><span class="box"></span></div>
              <div class="tick"><span class="cap">−2</span><span class="box"></span></div>
              <div class="tick"><span class="cap">−3</span><span class="box"></span></div>
              <div class="tick"><span class="cap warn">INC</span><span class="box inc"></span></div>
            </div>
          </div>
          <div class="woundbox">
            <div class="lbl">Fatigue</div>
            <div class="boxes">
              <div class="tick"><span class="cap">−1</span><span class="box"></span></div>
              <div class="tick"><span class="cap">−2</span><span class="box"></span></div>
              <div class="tick"><span class="cap warn">INC</span><span class="box inc"></span></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="mid">
      <div class="panel">
        <h2>{e(sheet["skills_heading"])}</h2>
        <div class="body skills-grid">
          <div>{left}</div>
          <div>{right}</div>
        </div>
        <p class="armor" style="margin-top:1.4mm">{e(sheet["skills_footnote"])}</p>
      </div>
      <div class="panel">
        <h2>Hindrances</h2>
        <div class="body">{hind}</div>
        <h2 style="margin-top:1.8mm">Edges</h2>
        <div class="body">{edges}</div>
      </div>
    </div>

    <div class="bot">
      <div class="panel">
        <h2>{e(sheet["weapons_heading"])}</h2>
        <div class="body">
          <table>
            <thead><tr><th>Weapon</th><th>Range</th><th>RoF</th><th>Dmg</th><th>Notes</th></tr></thead>
            <tbody>{weap}</tbody>
          </table>
          <p class="team">{e(team)}</p>
        </div>
      </div>
      <div class="panel">
        <h2>{e(sheet["gear_heading"])}</h2>
        <ul class="gear-list">{gear}</ul>
        <div class="{load_cls}">
          <div>Carried<strong>{e(ch["carried"])}</strong></div>
          <div>Limit<strong>{e(ch["limit"])}</strong></div>
          <div>Encumbrance<strong>{e(ch["penalty"])}</strong></div>
        </div>
        <p class="armor">{e(ch.get("armor", ""))}</p>
        <p class="team">{e(team_kit)}</p>
      </div>
    </div>
{you_block}
    <footer class="foot">
      <span>{e(sheet["footer_left"])}</span>
      <span>{e(sheet["footer_right"])}</span>
    </footer>
  </article>
</body>
</html>
"""


def bennies_html(text: str) -> str:
    """Keep the three tick boxes immediately after the word Bennies."""
    pips = '<span class="pip"></span><span class="pip"></span><span class="pip"></span>'
    if text.lower().startswith("bennies"):
        rest = text[len("Bennies") :].lstrip(" ·")
        if rest:
            return f"Bennies {pips} · {e(rest)}"
        return f"Bennies {pips}"
    return e(text)


def merge_sheet(raw: dict | None) -> dict:
    sheet = dict(SHEET_DEFAULTS)
    if raw:
        sheet.update(raw)
    return sheet


def load_pack(path: Path) -> tuple[dict, list[dict]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if "characters" not in data:
        raise SystemExit(f"{path}: missing 'characters'")
    return merge_sheet(data.get("sheet")), data["characters"]


def sync_assets(out: Path) -> None:
    src_css = TOOL_DIR / "sheet.css"
    dst_css = out / "sheet.css"
    if src_css.resolve() != dst_css.resolve():
        shutil.copy2(src_css, dst_css)

    src_fonts = TOOL_DIR / "fonts"
    dst_fonts = out / "fonts"
    if not src_fonts.is_dir():
        return
    if dst_fonts.exists() or dst_fonts.is_symlink():
        if dst_fonts.resolve() == src_fonts.resolve():
            return
        return
    try:
        dst_fonts.symlink_to(src_fonts, target_is_directory=True)
    except OSError:
        shutil.copytree(src_fonts, dst_fonts)


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


def build(data_path: Path, out: Path, who: str, pdf: bool) -> None:
    sheet, characters = load_pack(data_path)
    known = {ch["id"]: ch for ch in characters}
    wanted = list(known) if who == "all" else [who]
    missing = [w for w in wanted if w not in known]
    if missing:
        raise SystemExit(f"Unknown character id: {', '.join(missing)}")

    out.mkdir(parents=True, exist_ok=True)
    sync_assets(out)
    for lid in wanted:
        path = out / f"{lid}.html"
        path.write_text(render(known[lid], sheet), encoding="utf-8")
        print("wrote", path.name)
        if pdf:
            print_pdf(path)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Build A4 SWADE pregen sheets from a character print extract."
    )
    parser.add_argument("data", type=Path, help="Path to chars.json")
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output directory (default: same folder as chars.json)",
    )
    parser.add_argument(
        "--who",
        default="all",
        help="Character id, or all (default: all)",
    )
    parser.add_argument("--pdf", action="store_true", help="Also print A4 PDF via Chrome")
    args = parser.parse_args(argv)
    data_path = args.data.resolve()
    if not data_path.is_file():
        raise SystemExit(f"No such file: {data_path}")
    out = (args.out or data_path.parent).resolve()
    build(data_path, out, args.who, args.pdf)


if __name__ == "__main__":
    main()
