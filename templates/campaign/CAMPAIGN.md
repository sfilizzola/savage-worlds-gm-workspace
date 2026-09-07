---
title: "<Campaign title>"
status: concept
language: en
format: short-arc
system: "SWADE Fifth Printing (2023)"
rank: "Novice"
players: "4-6"
pc_mode: both
setting_modules: []
supernatural_level: none
historical_accuracy:
  requirement: not-applicable
  scope: "<What must be accurate, or why this is not applicable>"
  sources: []
house_rules: none
---

# <Campaign Title>

Complete every front-matter field before adding child adventures or campaign-local canon. Repeat the same `system`, `rank`, `pc_mode`, `setting_modules`, `supernatural_level`, `historical_accuracy`, and `house_rules` values in each child's `ADVENTURE.md` unless a listed child-adventure exception says otherwise.

This file is campaign configuration and indexes. It is **not** `RUN.md` and must not be compiled as table flow. Campaigns have **no** `QUALITY.md`; each child adventure scores `QUALITY.md` and compiles its own `RUN.md`.

Allowed values:

- `status`: concept | drafting | verified | ready | played | archived
- `language`: `en` unless this campaign explicitly uses another language for repository and table material
- `format`: short-arc | campaign
  - `short-arc`: a bounded mini-campaign (about 6–12 sessions). Use this as the default linked-play length.
  - `campaign`: a longer evolving campaign. Use only when the situation, factions, and advancement need an open calendar.
  - Do **not** set `one-shot` here. A single night is a child adventure (`format: one-shot` on that child's `ADVENTURE.md`) or a standalone folder under `adventures/`.
- `system`: `"SWADE Fifth Printing (2023)"` unless the GM records a different declared core
- `rank`: Novice | Seasoned | Veteran | Heroic | Legendary
- `players`: a range such as `"4-6"`
- `pc_mode`: pregenerated | player-supplied | both
- `supernatural_level`: none | subtle | moderate | full
- `historical_accuracy.requirement`: not-applicable | cinematic | researched | strict
- `historical_accuracy.scope`: what must be accurate, or why accuracy is not applicable
- `historical_accuracy.sources`: list of titles/paths used for this campaign's background, or `[]`
- `house_rules`: `none` or a list of IDs from `rules/house-rules.md`

`setting_modules: []` means no optional setting module is active for this table. List `Weird War II` explicitly to use it. Child adventures must not activate a module the campaign has not listed unless a child-adventure exception records it.

## One-sentence throughline

<Who is this table about, what pressure runs across the linked adventures, and what is at stake if they fail across the arc?>

## GM intent

<What experience, themes, and main story does the GM want this campaign to support? Desired destination is not a required path.>

## Campaign predetermined truths

Facts that are true for this table regardless of player action. Keep these distinct from planned events and from unused adventure prep.

- <Truth>

## Party index

Canonical mechanical sheets live under this campaign's `characters/`. Link them here. Do not keep a second full sheet inside a child adventure.

- <Name> — `characters/<file>.md` — player / concept / notes

## Adventure index

Child folders sit beside `world/` and `characters/`. List every child that belongs to this campaign. Each child keeps its own `ADVENTURE.md`, `QUALITY.md`, and `RUN.md`.

| Slug | Title | Status | Notes |
|------|-------|--------|-------|
| `<adventure-slug>` | | | |

## Canon boundaries

- **Root `world/`:** setting-wide facts shared across tables. Do not dump this campaign's evolving play state there.
- **This campaign's `world/`:** this table's established locations, factions, recurring NPCs, lore, and timelines.
- **Child adventures:** night-specific prep, situation details, and secrets that are not yet (or never) table-wide canon.
- **Session recaps:** what actually happened. Promote into campaign `world/` only after it is established.

Adventure preparation is not canon merely because it was written. A planned event becomes history only if it occurs.

## Child-adventure exceptions

List any child that is allowed to differ from this file's configuration (rank, modules, historical accuracy, house rules, `pc_mode`, or similar). If there are none, write `none`.

- <Child slug>: <what differs and why>
