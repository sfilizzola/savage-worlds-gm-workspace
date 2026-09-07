# Campaign Folder Structure - Approved Design

## Purpose

Give this workspace a home for linked play (a short arc or campaign) without forcing every one-shot into a parent folder. A campaign is a directory with table-wide canon and party sheets; each night remains a normal adventure folder inside it. Standalone one-shots stay flat under `adventures/`.

This change is templates and operating documentation only. It does not create a sample campaign and does not move Operation Hinterland.

## Decision

**Two roots for playable material.**

| Home | Use |
|------|-----|
| `adventures/<slug>/` | Standalone one-shot, or a single-folder piece that has not been split or adopted. Hinterland stays here. |
| `campaigns/<slug>/` | Shared table context plus child adventure folders. |

**Two entry points, same end state.**

1. **Campaign first:** copy `templates/campaign/` to `campaigns/<slug>/`, then add child adventures from `templates/adventure/`.
2. **Adventure first:** start in `adventures/<slug>/` as today; later **adopt** the folder into a new or existing campaign with a documented `git mv` checklist (no CLI).

**Canon jobs stay split.**

- Repo-root `world/` — setting-wide facts that can apply to any table.
- Campaign `world/` — this table’s evolving people, places, factions, and lore.
- Adventure files — night-of prep. Prep is not canon.

**Party sheets live once**, in `campaigns/<slug>/characters/`. Child adventures link; they do not keep a second full sheet set.

## Scope

**In scope**

- `templates/campaign/` and `campaigns/README.md`.
- `CAMPAIGN.md` template (table-wide config and indexes).
- Campaign `world/` stub layout matching repo `world/`.
- Campaign `characters/README.md` pointing at the sheet printer and forbidding duplicate full sheets in child adventures.
- Updates to workspace maps and how-to: `README.md`, `HOW_TO_USE.md`, `AGENTS.md`, `GM.md`, `adventures/README.md`, `world/WORLD.md`.
- Path examples in printer READMEs, `tools/README.md`, `templates/adventure/characters.md`, `templates/adventure/SKELETON.md` comments, and `.cursor/skills/npc-voice/SKILL.md` so campaign nights and campaign `characters/` are valid.
- A written adopt checklist in `HOW_TO_USE.md`.

**Out of scope**

- Creating `campaigns/<any-real-slug>/` as a test campaign (the GM does that after this lands).
- Moving or rewriting Operation Hinterland.
- An `init` / `adopt` script.
- Changing printer Python behavior (they already take a file path; default output is beside that file).
- Rewriting historical files under `docs/superpowers/plans/` or older design specs except this new spec.
- A campaign-level `RUN.md` or `QUALITY.md`.
- Dual listing (adventure stays under `adventures/` while also living in a campaign).

## Layout

```text
world/                                 # setting-wide canon (any table)
adventures/
  operation-hinterland/                # one-shot; unchanged
  <standalone-slug>/
campaigns/
  README.md
  <campaign-slug>/                     # created by the GM later, not in this pass
    CAMPAIGN.md
    world/
      WORLD.md
      locations/
      factions/
      npcs/
      lore/
    characters/                        # canonical party + print extract
    <adventure-slug>/                  # full adventure tree
      ADVENTURE.md
      QUALITY.md
      RUN.md
      …
templates/
  adventure/                           # unchanged role
  campaign/                            # new
```

### Identification

- A directory is a **campaign** if it contains `CAMPAIGN.md`.
- A directory is an **adventure** if it contains `ADVENTURE.md`.
- `world/` and `characters/` are never adventures.
- Agents looking for playable units key off `ADVENTURE.md` and `CAMPAIGN.md`, not a fixed depth and not `adventures/*/` only. Do not add a discovery script or directory walker in this pass. Printer CLIs already take an explicit file path.

## Campaign template

Copy `templates/campaign/` to `campaigns/<slug>/`. Do not copy `templates/adventure/SKELETON.md` into a campaign or an adventure.

Required files in the template:

```text
templates/campaign/
  CAMPAIGN.md
  characters/README.md
  world/WORLD.md
  world/locations/README.md
  world/factions/README.md
  world/npcs/README.md
  world/lore/README.md
```

Stub READMEs match the tone of repo `world/` (purpose of the folder, not sample canon). Campaign `world/WORLD.md` must state that this tree is **this table’s** canon and that repo-root `world/` remains setting-wide. `characters/README.md` states: this directory owns party `.md` sheets and `print/chars.json`; print with `tools/print-sheets/` using this path; child adventures must not copy full sheets.

Empty subdirectories may exist as README stubs (same as repo `world/` today). Do not add placeholder NPC or PC files.

## `CAMPAIGN.md`

Front matter (required fields, same value vocabularies as `templates/adventure/ADVENTURE.md` unless noted):

- `title`
- `status`: concept | drafting | verified | ready | played | archived
- `language`
- `format`: short-arc | campaign (`one-shot` is not valid here)
- `system`
- `rank`
- `players`
- `pc_mode`
- `setting_modules`
- `supernatural_level`
- `historical_accuracy` (same shape as adventure)
- `house_rules`

Body (required sections):

- One-sentence throughline
- GM intent
- Campaign predetermined truths (table-persistent; not a night plot)
- Party index (links into `characters/`)
- Adventure index (relative links to each child `ADVENTURE.md`, including planned-but-empty slots if the GM wants them)
- Canon reminder: repo `world/` is setting-wide; this `world/` is this table; adventure prep is not canon
- Exceptions log: any child adventure whose front matter differs from this file (setting module, Rank, house rules), one line each

`CAMPAIGN.md` is not compiled to `RUN.md` and is not scored with `QUALITY.md`.

## Child adventures

Create with `templates/adventure/` (except `SKELETON.md`) as a sibling of `world/` and `characters/`, not under a nested `adventures/` folder.

- Keep the usual adventure files (`ADVENTURE.md`, `QUALITY.md`, modular prep, `RUN.md`, optional `handouts/`, `maps/`, `sources/`, `sessions/`).
- `format` on the child is `one-shot` when the folder is one table night. Arc length lives on `CAMPAIGN.md`. If a child is itself an unsplit multi-session unit, it may use `format: short-arc`; prefer splitting when there are two distinct adventure folders.
- Repeat campaign `setting_modules`, `rank`, `house_rules`, and related shared fields on the child `ADVENTURE.md` so a compile that opens only the adventure still has complete config.
- If a night truly differs, the child’s front matter wins for that night only; add a line to the campaign exceptions log.
- `characters.md` in the child: night hooks, party assumptions, and a link to `../characters/` (and to `../characters/print/chars.json` for print). No second full mechanical sheets.
- Adventure-local `npcs/` remain valid for people who do not persist.

Session recaps stay in the child’s `sessions/`. After play, update campaign `world/` (and party sheets if they changed) from what happened. Touch repo `world/` only when the GM wants setting-wide canon.

## Workflows

### Campaign first

1. Copy `templates/campaign/` → `campaigns/<slug>/`.
2. Fill `CAMPAIGN.md` and add party files under `characters/` as needed.
3. Add campaign `world/` entries when this table has canon.
4. Copy `templates/adventure/` (except skeleton) into `campaigns/<slug>/<adventure-slug>/`.
5. Link the child from the adventure index; point character print at campaign `characters/print/chars.json`.

### Adopt (adventure first)

Works for a new campaign or an existing one.

1. If needed, create the campaign skeleton as above.
2. `git mv adventures/<slug> campaigns/<campaign-slug>/<slug>`.
3. Move party sheets from the adventure’s `characters/` to `campaigns/<campaign-slug>/characters/` if the campaign does not already own those people. If both exist, keep the campaign copies, diff the adventure copies, then remove duplicate full sheets from the adventure.
4. Leave `characters.md` (hooks) and a link to `../characters/`.
5. Promote only recurring people and places into campaign `world/`. Leave night-only NPCs in the adventure `npcs/`.
6. Add the folder to the `CAMPAIGN.md` adventure index.
7. Fix hardcoded `adventures/<slug>/` paths inside the moved tree (print wrappers, handout READMEs, `chars.json` comments, local docs).
8. Do not leave a stub under `adventures/` that pretends the one-shot is still there.

Hinterland is not adopted in this implementation.

## Canon lookup (campaign night)

In order:

1. The child adventure’s files (prep, secrets, night NPCs).
2. This campaign’s `world/` and `characters/`.
3. Repo-root `world/` for setting-wide facts.

Never treat unused prep as canon. Never silently copy campaign state into repo `world/`.

## Agent and skill rules

`AGENTS.md` gains: before modifying a target under `campaigns/`, read that campaign’s `CAMPAIGN.md` as well as the target `ADVENTURE.md`. Still read `GM.md` and `rules/RULES.md` as today.

`GM.md` gains a short pointer: one-shots live under `adventures/`; linked play lives under `campaigns/<slug>/` with child adventures; do not stretch a one-shot folder into a campaign calendar — use a campaign parent when there is shared table state or more than one adventure folder, or when the GM starts from campaign context.

npc-voice:

- If a named NPC file already exists, edit it in place (unchanged).
- Else if the person should persist for this table: `campaigns/<slug>/world/npcs/<name>.md`.
- Else: `<adventure>/npcs/<name>.md` (whether that adventure is under `adventures/` or `campaigns/`).
- Still never player sheets. Still never repo `world/npcs/` unless the GM asks.

## Printers and path docs

One Python behavior change is required so examples tell the truth:

- `python3 tools/print-run/render.py <path-to>/RUN.md` — when the input file is named `RUN.md`, output defaults to that file’s parent `print/` folder (standalone `adventures/<slug>/` or campaign child `campaigns/<campaign-slug>/<adventure-slug>/`). Other markdown filenames still default to the same directory as the input. `--out-dir` remains optional override, not a campaign workaround.
- `python3 tools/print-sheets/render.py <path-to>/characters/print/chars.json` — for a campaign, that path is `campaigns/<slug>/characters/print/chars.json`.

`tools/README.md` currently says adventure data stays under `adventures/<slug>/`. Replace with: one-shot data under `adventures/<slug>/`; campaign nights under `campaigns/<campaign>/<adventure>/`; campaign party sheets under `campaigns/<campaign>/characters/`. Handouts stay with the adventure that owns them.

Keep Hinterland examples as the one-shot illustration. Add one parallel example path using `campaigns/<campaign>/<adventure>/` without inventing a real campaign name beyond a placeholder such as `<campaign-slug>`.

## HOW_TO_USE.md

Add two operator sections (wording can follow existing prompt-block style):

- **Start a campaign or short arc** — copy campaign template; then add adventures; do not put a one-shot parent under `adventures/`.
- **Adopt a one-shot into a campaign** — the checklist above.

Revise **Continue a campaign or short arc** so “established world canon” means campaign `world/` plus repo `world/`, and the next session is a child adventure (new folder or existing), not a second `RUN.md` at campaign root.

Revise the start-here copy in `README.md` so step 2 is either copy adventure template into `adventures/<slug>/` **or** copy campaign template into `campaigns/<slug>/` then add child adventures.

## Verification

Implementation is complete when:

- `templates/campaign/` and `campaigns/README.md` exist and match this layout.
- A co-GM can follow `HOW_TO_USE.md` for campaign-first and adopt without inventing directories.
- `AGENTS.md` and npc-voice name the correct NPC and `CAMPAIGN.md` reads.
- Printer docs accept campaign paths; a `RUN.md` input defaults to its parent `print/` folder; Hinterland one-shot examples still work.
- No `campaigns/<real-slug>/` adventure content is added in this pass.
- Operation Hinterland paths are unchanged.

## Non-goals (do not sneak in)

- Auto-discovery scripts, indexes, or generated campaign dashboards.
- Changing `format` vocabularies on existing Hinterland `ADVENTURE.md`.
- Nested `campaigns/<slug>/adventures/` (rejected; children sit beside `world/` and `characters/`).
