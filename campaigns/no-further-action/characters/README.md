# Campaign characters

This directory is the **canonical** home for this campaign's player characters.

- Mechanical source of truth: `lilly-dawson.md` (1986 Novice). 1998 Seasoned and 2016 Veteran sheets will live here when rebuilt.
- Print extract: `print/chars.json`
- Portrait: `lilly-1986-id.png` (1986 ID photo, head-and-shoulders crop of `lily_pic 1986.png`). Referenced from the print extract as `../lilly-1986-id.png`. The full-figure `lily_portrait_1986.png` and the era stills stay here as player art; they are not what the file mounts.

```text
python3 tools/print-sheets/render.py campaigns/no-further-action/characters/print/chars.json --pdf
python3 tools/print-sheets/measure.py campaigns/no-further-action/characters/print/lilly.html
```

Lilly's sheet prints as an Ashgrove PD personnel file: mounted photo, description-and-service fields, a disposition stamp, ruled case notes, open threads, and a signature strip. See `tools/print-sheets/README.md` for those keys.

Two rules for the case-file blocks:

- **Player-facing only.** `dossier` may carry what Lilly knows. `threads` on this sheet are blank write-in rows. No GM Correction material, no prepared outcomes for an unplayed night.
- **Era-stable, not night-specific.** `you` and `play` must stay true for every 1986 job, since later 1986 nights are unrelated cases. Names of tonight's people (Whitley, Doyle, Nancy, Abigail) belong in the child adventure's `characters.md`.
- **Do not invent canon to fill a field.** A field the campaign has not established (height, shield number, partner) takes an empty value, which prints a line to fill in by hand.

The extract's fields must stay consistent with `lilly-dawson.md`. After editing the `.md`, update `print/chars.json`, rebuild, and re-run `measure.py` — the sheet keeps only about 4mm of slack on one A4 page.

## Brazilian Portuguese print

A translated table copy of the same 1986 sheet, for a player who reads pt-BR. It **does not replace** anything: `lilly-dawson.md` (English) stays the mechanical source of truth, and `print/chars.json` stays the English print extract.

```text
python3 tools/print-sheets/render.py campaigns/no-further-action/characters/print/chars.pt-BR.json --pdf
python3 tools/print-sheets/measure.py campaigns/no-further-action/characters/print/lilly-pt.html
```

| File | Role |
|---|---|
| `lilly-dawson.md` | Source of truth. English. Mechanics change here first. |
| `print/chars.json` | English print extract → `lilly.html` / `lilly.pdf` |
| `print/chars.pt-BR.json` | Translated print extract → `lilly-pt.html` / `lilly-pt.pdf` |

Rules for the translation:

- **Numbers are not translated.** Die types, Pace, Parry, Toughness, ranges, damage, weight, and HR-NFA-001 must read identically in both extracts. If a trait changes in the `.md`, update **both** extracts and re-measure both sheets.
- **Proper nouns and the disposition stamp stay English.** Ashgrove PD, New Jersey, FBI, and the `No Further Action` stamp are in-world American paperwork and also the campaign title.
- **Rules authority does not move.** The table's authority remains SWADE Fifth Printing (2023) in English, in `sources/systems/SWADE/`. The pt-BR sheet is a reading aid, not a second rules source.

### PT/EN trait glossary

Terms below were checked against Brazilian publisher and community material on 2026-09-08 (retropunk.com.br, odysseypub.com.br, d30rpg.com.br). The workspace holds **no** official Retropunk SWADE PDF, so terms are marked *attested* or *unconfirmed*. Unconfirmed terms are the GM's call; if you want them fixed for the campaign, record the decision in `rules/rulings.md`.

| English (authority) | Printed pt-BR | Status |
|---|---|---|
| Agility / Smarts / Spirit / Strength / Vigor | Agilidade / Astúcia / Espírito / Força / Vigor | attested |
| Pace / Parry / Toughness | Movimentação / Aparar / Resistência | attested |
| Hindrances / Edges | Complicações / Vantagens | attested |
| Bennies | Benes | attested |
| Athletics / Notice / Persuasion / Stealth | Atletismo / Perceber / Persuadir / Furtividade | attested |
| Research / Shooting / Electronics / Academics | Pesquisar / Atirar / Eletrônica / Conhecimento Acadêmico | attested |
| Investigator / Curious | Investigador / Curioso | attested |
| Wild Card | Coringa | unconfirmed (also seen as Curinga) |
| Common Knowledge | Conhecimento Geral | unconfirmed (also seen as Conhecimento Comum) |
| Fighting / Driving / Intimidation | Lutar / Dirigir / Intimidar | unconfirmed |
| Alertness / Danger Sense | Alerta / Sentido de Perigo | unconfirmed |
| Night Terrors | Terrores Noturnos | unconfirmed |
| Novice rank | Novato | unconfirmed |
| Wounds / Fatigue / Incapacitated | Ferimentos / Fadiga / INC | unconfirmed |

Child adventures **link** here. Do **not** duplicate full mechanical sheets inside a child adventure.
