#!/usr/bin/env python3
"""Build call-letter HTML (and optionally PDF) for Operation Hinterland.

Source of truth remains the letter-*.md files. WHEN is the confirmed session.

  python3 build_letters.py --who keene
  python3 build_letters.py --who all --pdf
"""

from __future__ import annotations

import argparse
import html
import subprocess
from pathlib import Path

OUT = Path(__file__).resolve().parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Session date/time printed on every letter.
WHEN = "14.11.2026 at 1400 hours"

ROUND_STAMP = """
<svg class="stamp-round" viewBox="0 0 120 120" aria-hidden="true">
  <g fill="none" stroke="#c1121f" stroke-width="2.2">
    <circle cx="60" cy="60" r="56"/>
    <circle cx="60" cy="60" r="48"/>
  </g>
  <circle cx="60" cy="60" r="3.2" fill="#c1121f"/>
  <text x="60" y="64" text-anchor="middle" fill="#c1121f"
        font-family="Courier Prime, monospace" font-size="11" font-weight="700"
        letter-spacing="1.4">JOD</text>
  <defs>
    <path id="arc-top" d="M 22,60 A 38,38 0 0 1 98,60"/>
    <path id="arc-bot" d="M 98,60 A 38,38 0 0 1 22,60"/>
  </defs>
  <text fill="#c1121f" font-family="Courier Prime, monospace" font-size="8.2"
        letter-spacing="2.4">
    <textPath href="#arc-top" startOffset="50%" text-anchor="middle">ADDRESSEE ONLY</textPath>
  </text>
  <text fill="#c1121f" font-family="Courier Prime, monospace" font-size="7.4"
        letter-spacing="1.6">
    <textPath href="#arc-bot" startOffset="50%" text-anchor="middle">JOINT OPS DESK</textPath>
  </text>
</svg>
"""

LETTERS = [
    {
        "id": "keene",
        "ref": "JOD / OH–01",
        "org": "Allied Special Operations",
        "to": "1st Lt. Jack Keene, U.S. Army",
        "role": "Point / small-unit lead. You run the team.",
        "priority": "You are not being asked. You are being collected.",
        "salutation": "Lieutenant Keene,",
        "paras": [
            "After the last few months, HQ has a very short list of men who can walk four specialists into ugly country, keep them pointed the same way, and walk most of them back out again. Your name is at the top. Twice, in one clerk’s case, which we are choosing to read as enthusiasm and not a filing error.",
            "You are the team leader. Your job is to read the ground, call the approach, and hold four stubborn specialists together when the map and the mud start arguing. The others blow, listen, patch, and scout. You decide when. That is the whole advertisement.",
        ],
        "report": "You are hereby directed to report for briefing:",
        "after": [
            "Attendance is mandatory. Heroics are optional until we say otherwise. Stubbornness will be tolerated; it usually is, in your case.",
        ],
        "food": "Snacks will be provided on site.",
        "drinks": "Bring your own. The bar does not exist. This is not a negotiation.",
        "closing": "Do not be late, Lieutenant. The other three are already being told you are in charge. Try to look like you knew that. If anyone asks who is hosting: you are. If anyone asks who is cooking: you are not. Those are different wars.",
        "close": "By order,",
        "sign": "Col. W. Harrow",
        "title": "Joint Operations Desk",
        "post": "(who would like his evenings back)",
    },
    {
        "id": "krajewski",
        "ref": "JOD / OH–02",
        "org": "Allied Special Operations",
        "to": "Sgt. Tomasz Krajewski",
        "role": "Demolitions and field engineer. If it must stop working, that is you.",
        "priority": "Handle like explosives. Which is to say: carefully, and then all at once.",
        "salutation": "Sierżancie Krajewski,",
        "paras": [
            "Your work with explosives and field engineering these last months has made you inconveniently famous. Officers who cannot tell a primer from a paperweight keep asking for “the Pole who can drop a problem without dropping the building next to it.” That is you. Congratulations. Condolences. Same envelope.",
            "You are the demolitions man. Charges, wire, tools, improvisation: if a thing needs to be cut, rigged, or persuaded to become a hole in the ground, you are the one holding the kit. The lieutenant calls the noise. You make sure there is still a charge left when he does. Za Polskę — and for the three people who will be standing too close to your bag.",
        ],
        "report": "You will report to:",
        "after": [
            "Leave the practical jokes at home. A whoopee cushion is funny. A satchel charge in the umbrella stand is a court martial with extra paperwork.",
        ],
        "food": "Snacks will be provided. They are not fused. You may eat them without a countdown.",
        "drinks": "Bring your own. We supply courage of the dry variety only.",
        "closing": "Do not bring extra surprises. The operation is surprise enough.",
        "close": "Respectfully,",
        "sign": "Col. W. Harrow",
        "title": "Joint Operations Desk",
        "post": "P.S. If the doorbell sticks, knock. Do not improve it.",
    },
    {
        "id": "vasseur",
        "ref": "JOD / OH–03",
        "org": "Allied Special Operations / Forces Françaises Libres",
        "to": "Sgt. Hélène Vasseur",
        "role": "Signals and languages. Wires, sets, and other people’s conversations.",
        "priority": "Immediate. Curiosity is not a sufficient excuse for lateness. We checked.",
        "salutation": "Ma chère Sergent,",
        "paras": [
            "Your months among wires, languages, and other people’s secrets have made you the least replaceable person in a very replaceable war. HQ would like it noted that this is a compliment. They would also like it noted that they are slightly afraid of you. Both can be true.",
            "You are the signals specialist, and the one who can switch tongues without switching sides. Radios, switchboards, taps, papers: you read them, and if the conversation goes badly you can also turn them into scrap. The others will arrive speaking one language each and expect you to make a team out of it. Quelle surprise.",
        ],
        "report": "You are directed to report for briefing:",
        "after": [
            "Be cautious, of course. Also be on time. Liberté, equality, and try not to take the host’s telephone apart before the briefing starts. It is a civilian line. It is allowed to be boring.",
        ],
        "food": "Snacks will be provided. This is not French cooking. We are aware. Please do not file a complaint in triplicate.",
        "drinks": "Bring your own. Wine is a personal matter. The desk provides only water and bad decisions.",
        "closing": "Do not ask too many questions before you arrive. That is what the briefing is for. We both know you will anyway.",
        "close": "With distinguished regards — and a certain amused distrust,",
        "sign": "Col. W. Harrow",
        "title": "Joint Operations Desk",
        "post": "",
    },
    {
        "id": "lang",
        "ref": "JOD / OH–04",
        "org": "Allied Special Operations",
        "to": "Cpl. Beatrice Lang",
        "role": "Scout and field medic. Find the way in. Keep the bodies attached.",
        "priority": "Quietly urgent. Do try not to make a fuss. A fuss is the opposite of the point.",
        "salutation": "Corporal Lang,",
        "paras": [
            "Someone at this desk has finally admitted that a scout who can also keep a body attached to its owner is not a luxury. It is the difference between a team and a sad anecdote. Your last months in the field — eyes first, bandages second — have put you on a very short list. The list has four names. You are one of them.",
            "You are the scout and the medic. Your job is to find the quiet way in without announcing it, watch what the lieutenant is about to walk into, and patch the damage when the way out is less elegant. The others lead, blow, and listen. You keep them on their feet long enough to matter.",
        ],
        "report": "You will present yourself at:",
        "after": [
            "Do not get lost. That would be embarrassing, and this desk does not budget for irony. If you arrive early, you may reconnoitre the kitchen. If you start bandaging people who are only hungry, we will have words.",
        ],
        "food": "Snacks will be laid on. This is not a promise of a proper meal, a decent cup of tea, or the Empire. Manage your expectations, Corporal.",
        "drinks": "Bring your own. We are many things. A pub is not one of them.",
        "closing": "Bee — if we may — try to keep the lieutenant from walking into the furniture, and the sergeant from turning the furniture into rubble. That is the job. The other job comes later.",
        "close": "I have the honour to remain, etc.,",
        "sign": "Col. W. Harrow",
        "title": "Joint Operations Desk",
        "post": "P.S. The first-aid kit is for actual injuries. Crisps do not count, however sharp.",
    },
]


def render(letter: dict, when: str) -> str:
    e = html.escape
    paras = "".join(f"<p>{e(p)}</p>" for p in letter["paras"])
    after = "".join(f"<p>{e(p)}</p>" for p in letter["after"])
    post = f'<p class="post">{e(letter["post"])}</p>' if letter["post"] else ""
    if when:
        when_html = f'<div class="when"><span class="k">DATE / TIME:</span> {e(when)}</div>'
    else:
        when_html = (
            '<div class="when blank"><span class="k">DATE / TIME:</span>'
            '<span class="fill"></span></div>'
        )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Call letter — {e(letter["to"])}</title>
  <link rel="stylesheet" href="letter.css" />
</head>
<body>
  <article class="page">
    <div class="grain"></div>
    {ROUND_STAMP}
    <div class="stamp-conf" aria-hidden="true">
      <div class="outer">
        <div class="inner">
          <div class="word">Confidential</div>
          <div class="sub">Restricted · Hinterland</div>
        </div>
      </div>
    </div>

    <header class="letterhead">
      {e(letter["org"])}
      <div class="desk">Joint Operations Desk</div>
      <hr class="rule" />
    </header>

    <div class="refs">
      <span>Ref. {e(letter["ref"])}</span>
      <span>Copy 1 of 1 · Destroy by fire</span>
    </div>

    <div class="block">
      <div class="row"><span class="k">TO:</span><span class="v">{e(letter["to"])}</span></div>
      <div class="row"><span class="k">FROM:</span><span class="v">Joint Operations Desk</span></div>
      <div class="row"><span class="k">RE:</span><span class="v">OPERATION HINTERLAND</span></div>
      <div class="row"><span class="k">ROLE:</span><span class="v">{e(letter["role"])}</span></div>
      <div class="row"><span class="k">PRIORITY:</span><span class="v priority">{e(letter["priority"])}</span></div>
    </div>

    <p class="salute">{e(letter["salutation"])}</p>
    {paras}
    <p>{e(letter["report"])}</p>
    <div class="address">
      <div class="place">Forward Station CHARLIE-MILLS</div>
      <div>Charlie-Mills-Strasse 3</div>
      <div>Hamburg, Germany</div>
      {when_html}
    </div>
    {after}
    <p><span class="k">FOOD:</span> {e(letter["food"])}</p>
    <p><span class="k">DRINKS:</span> {e(letter["drinks"])}</p>
    <p>{e(letter["closing"])}</p>
    <div class="signoff">
      <p>{e(letter["close"])}</p>
      <div class="name">{e(letter["sign"])}</div>
      <div class="title">{e(letter["title"])}</div>
      {post}
    </div>
  </article>
</body>
</html>
"""


def print_pdf(html_path: Path) -> None:
    pdf_path = html_path.with_suffix(".pdf")
    subprocess.run(
        [
            CHROME,
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


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Operation Hinterland call letters.")
    parser.add_argument(
        "--who",
        default="keene",
        help="keene | krajewski | vasseur | lang | all  (default: keene, for a check print)",
    )
    parser.add_argument(
        "--when",
        default=WHEN,
        help='Session date/time (default: WHEN in this file)',
    )
    parser.add_argument("--pdf", action="store_true", help="Also print A4 PDF via Chrome")
    args = parser.parse_args()

    wanted = [L["id"] for L in LETTERS] if args.who == "all" else [args.who]
    known = {L["id"]: L for L in LETTERS}
    missing = [w for w in wanted if w not in known]
    if missing:
        raise SystemExit(f"Unknown letter id: {', '.join(missing)}")

    for lid in wanted:
        path = OUT / f"letter-{lid}.html"
        path.write_text(render(known[lid], args.when.strip()), encoding="utf-8")
        print("wrote", path.name)
        if args.pdf:
            print_pdf(path)


if __name__ == "__main__":
    main()
