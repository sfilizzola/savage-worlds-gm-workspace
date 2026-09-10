# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is **not** a software project. It is a Savage Worlds (SWADE) tabletop RPG authoring workspace that treats game prep like a modular codebase: `sources/` are dependencies, `world/` holds reusable canon, adventure files hold preparation, session recaps capture what actually happened, and `RUN.md` is the compiled table-facing artifact. Almost all work is writing and editing Markdown; the only executable code is the Python print tooling in `tools/`.

## Required reading before authoring

`AGENTS.md` is the entry contract. Before any authoring, editing, rules verification, or session-prep task, read in this order:

1. `GM.md` — the authoritative operating policy for the whole workspace (co-GM role, people/speech rules, rules authority, adventure design model, quality gate, `RUN.md` compile contract, post-session discipline).
2. `rules/RULES.md` — rules-authority precedence, before writing any mechanics.
3. The target adventure's `ADVENTURE.md` — before modifying that adventure.
4. If the target is under `campaigns/`, also that campaign's `CAMPAIGN.md`.

Do not shortcut these. `GM.md` overrides default behavior for game content.

**Look locally first.** When working on an adventure or campaign, exhaust the information inside that unit's own folder (its `ADVENTURE.md`/`CAMPAIGN.md`, `plot.md`, `npcs/`, `locations.md`, `encounters.md`, `secrets.md`, `characters/`, `world/`, `sources/`) before spending tokens reading the full source rulebooks in `sources/` or searching the internet. The adventure/campaign folder is the primary context; the rulebooks and the web are fallbacks for what the local files genuinely do not answer.

## Print tooling (the only runnable code)

Pure Python 3 standard library — no pip install needed. `--pdf` shells out to headless Chrome; without Chrome the HTML is still written and you print it to A4 yourself. Always run from the workspace root. Generated `print/` output and `chars.json` are build artifacts — never hand-edit `print/RUN.html`, `print/RUN.pdf`, or the generated sheet HTML/PDF.

```bash
# Compile a RUN.md to A4 (standalone or campaign child); output lands beside the input in print/
python3 tools/print-run/render.py adventures/<slug>/RUN.md
python3 tools/print-run/render.py campaigns/<campaign-slug>/<adventure-slug>/RUN.md --pdf

# Print filled pregen character sheets (NOT a generator — it never rolls or spends points)
python3 tools/print-sheets/render.py adventures/<slug>/characters/print/chars.json --who keene --pdf

# Verify a printed sheet still fits one A4 page (283mm printable height)
python3 tools/print-sheets/measure.py <path>/<id>.html

# Tests for the RUN printer
python3 tools/print-run/test_print_run.py
```

The `.md` character sheet is the mechanical source of truth; `characters/print/chars.json` is a hand-maintained print extract. After editing a `.md` sheet, update the matching `chars.json`, then rebuild.

## Repository layout & the "playable root" model

Playable material has two roots — pick one:

- **Standalone adventure** → `adventures/<slug>/`. Copy from `templates/adventure/`.
- **Linked play** → `campaigns/<campaign-slug>/`, where `CAMPAIGN.md`, the campaign's `world/`, and its canonical `characters/` sit **beside** the child adventure folders. Copy from `templates/campaign/`.

Supporting directories: `sources/` (read-only rulebooks/setting/historical refs), `rules/` (authority policy, `house-rules.md`, `rulings.md`), `world/` (setting-wide canon shared across tables), `templates/` (copy these to start new material), `docs/` (workspace design decisions).

**Three `world/` scopes exist — do not conflate them:** repository-root `world/` is setting-wide canon; a campaign's `world/` is that table's evolving canon and secrets; adventure files are prep only.

## Four kinds of truth (the core discipline)

Never collapse these:

- **Source material** — what a rulebook/map/historical source says.
- **Canon** — facts established as true in the game world.
- **Prep** — situations, possibilities, secrets prepared for play. Prep is NOT canon.
- **Session record** — what actually happened at the table.

Prepared material is never automatically canon or history merely because it was drafted. After play, promote only established events into canon; retire contradicted prep rather than rewriting it as if it happened.

## Rules authority (precedence, highest first)

1. Explicit active **house rule** (declared by the adventure, within its scope).
2. **SWADE Fifth Printing (2023)** — permanent default authority for all mechanics.
3. **Active setting module** — adds compatible content only; never silently replaces SWADE. (Weird War II and Deadlands Noir are installed but inert unless an adventure activates them.)
4. **Recorded ruling** in `rules/rulings.md` — interprets an unclear case; promoted to `house-rules.md` only when the GM explicitly makes it a standing override.

Never invent Savage Worlds notation or import older-edition mechanics. Cite source title + page beside prepared mechanics. If authority cannot be established, write `RULE UNCLEAR - GM DECISION REQUIRED`, state the question and sources checked, and ask the GM.

## Adventure lifecycle & the quality gate

Design flows `GM intent → objective → story point → situation → player decision → consequence → next reachable story point`. Build reachable situations, not a fixed scene chain or a menu of expected solutions. Never make one roll/clue/NPC/door/PC the only route to the main plot.

Before compiling `RUN.md`: fill and score the adventure's `QUALITY.md` (copied from `templates/adventure/QUALITY.md`) — five-beat map, Coherence (prep) pass/fail, and the 120-point checklist. "Ready" requires the numeric band (≥100, or 80–99 with named repairs) **and** a passed Coherence block with a logic summary. Re-score after any major plot change.

## Compiling RUN.md

`RUN.md` is a deliberate build artifact for the table. Follow `templates/adventure/SKELETON.md` exactly, including **Table flow (one home)**: every payload (speech, marks, Trait tables, stat blocks, procedure) appears **once**, in the story point where it is used — pointers may name that home, but duplicating a payload *inside* `RUN.md` is a compile fail. `RUN.md` may duplicate the modular sources (`plot.md`, NPC files, `encounters.md`); that is compile. Omitting a required skeleton block is also a compile fail. When a source changes, rebuild and re-verify.

At-hand boards use GitHub-style Markdown alerts (`> [!IMPORTANT]` for at-hand statistics, `> [!TIP]` for at-hand rules) — every content line and internal blank line prefixed with `>`. NPC speech uses a `Spoken lines:` field or a blockquote opening with a quotation mark (the printer tints these plum).

## Writing NPCs and dialogue

People are people, not plot devices — they know only what they could know, act from want/fear/cost, and speak in their own register (see `GM.md` "People, speech, and behavior"). A dedicated `.cursor/skills/npc-voice/` skill implements this; its destination rules: edit an existing named-NPC file in place; a person who should recur in a campaign goes in `campaigns/<campaign-slug>/world/npcs/<name>.md`; otherwise `<adventure>/npcs/<name>.md`. Never put NPC portrayal in `characters/` (that is pregen PCs) or in repository-root `world/npcs/` unless the GM asks. Do not invent stats while writing voice.

## Conventions

- English is the default for all repository and GM-facing content, even when a player handout is in another language. Translated character sheets/handouts get their own extract with distinct ids beside the English one.
- Sheet renderers and RUN renderers live only in `tools/` — never put a generator or renderer inside an adventure.
- Commit or push only when the user asks.
