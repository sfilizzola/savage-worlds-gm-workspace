# Player handouts — Operation Hinterland

## Call letters

Real-life invitations to the four players. Print one per envelope. These are not table canon, not a briefing, and not session history. They name the operation only. Insert the date and time before sending.

| File | Player character | Role |
|---|---|---|
| `letter-keene.md` | 1st Lt. Jack Keene (U.S.) | Point / small-unit lead |
| `letter-krajewski.md` | Sgt. Tomasz Krajewski (Polish) | Demo / field engineer |
| `letter-vasseur.md` | Sgt. Hélène Vasseur (Free French) | Signals / language |
| `letter-lang.md` | Cpl. Beatrice "Bee" Lang (British) | Scout / medic |

Full character sheets (print with the letter): `../characters/print/*.pdf`. Markdown source: `../characters/`. Rebuild sheets with the workspace printer: `python3 ../characters/print/build_sheets.py` ([`tools/print-sheets/`](../../../tools/print-sheets/README.md)).

**Meeting point:** Charlie-Mills-Strasse 3, Hamburg, Germany.  
**Date / time:** blank line on the print; fill by marker.  
**Mess:** snacks provided; drinks are bring-your-own.

Print letters: `print/letter-keene.pdf`, `print/letter-krajewski.pdf`, `print/letter-vasseur.pdf`, `print/letter-lang.pdf`.  
Rebuild: `python3 print/build_letters.py --who all --pdf`

## Rules card (table start)

First-time Savage Worlds table. Same one-pager for every player. Not character-specific. Edges and weapons stay on the sheet.

| File | What to print |
|---|---|
| `player-quick-ref.pdf` | **Easiest.** One A4 per player (plus Voss if a fifth sits). |
| `player-quick-ref.html` | Rebuild the PDF if you edit the card. File → Print → A4, backgrounds on, headers/footers off. |
| `player-quick-ref.md` | Source text and GM authority block. Do not print the GM block. |

Place the card beside the character sheet. It is not a briefing and not session history.

## GM card (table start)

Two A4 pages. GM only. Hydra tracker, night/fuse, opposition numbers, Edges that fire. Players keep the one-pager above.

| File | What to print |
|---|---|
| `gm-quick-ref.pdf` | **Easiest.** One two-page A4 for the GM, beside `RUN.md`. |
| `gm-quick-ref.html` | Rebuild the PDF if you edit the card. File → Print → A4, backgrounds on, headers/footers off. |
| `gm-quick-ref.md` | Source text and authority block. |

Do not hand this to players. Live head locations and the false-head twist are on it.
