# Campaign handouts — No Further Action

Table-start reference material shared across every era (1986 / 1998 / 2016), as opposed to a single night's prep. Not table canon, not a briefing, not session history.

## Player rules card

First refresher for a returning player, or a first-time reference. Core SWADE (dice, Bennies, turns, combat basics) plus this campaign's `HR-NFA-002` detective-work procedures. Not character-specific — no Trait numbers from `characters/lilly-dawson.md` are repeated here.

| File | What it is |
|---|---|
| `player-quick-ref.md` | English source of truth, plus the GM authority block (do not print that block). |
| `player-quick-ref.pt.md` | Brazilian Portuguese translation. The printed card is built from this text. |
| `print/player-quick-ref.pt.html` | Styled like the campaign's personnel-file character sheet (`tools/print-sheets/sheet.css`, same fonts). Rebuild the PDF from this if you edit the card: File → Print → A4, backgrounds on, headers/footers off. |
| `print/player-quick-ref.pt.pdf` | **Easiest.** One A4 page, ready to print. |

`print/sheet.css` is a copy of `tools/print-sheets/sheet.css`; `print/fonts` symlinks to `tools/print-sheets/fonts`. If the shared sheet CSS changes, re-copy it here and re-render. Verify the card still fits one page with:

```text
python3 tools/print-sheets/measure.py campaigns/no-further-action/handouts/print/player-quick-ref.pt.html
```

Place the card beside the character sheet. It repeats no GM secrets, no Concordance material, and no prepared outcomes for an unplayed night.
