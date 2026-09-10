# Savage Worlds GM Authoring Workspace v0.1

This repository is a reusable workspace for preparing and maintaining Savage Worlds adventures and campaigns. It treats RPG preparation like a small, modular codebase: sources are dependencies, world files hold reusable canon, adventure files hold preparation, session records capture what actually happened, and `RUN.md` is the compiled table-facing artifact.

## Start here

1. Read [`GM.md`](GM.md) before creating or revising material.
2. Choose a playable root:
   - **Standalone adventure** - copy `templates/adventure/` into `adventures/<adventure-slug>/`.
   - **Linked play** - copy `templates/campaign/` into `campaigns/<campaign-slug>/`, complete `CAMPAIGN.md`, then add child adventure folders beside the campaign's `world/` and `characters/`.
3. Complete the required configuration in each adventure's `ADVENTURE.md` before writing mechanics.
4. Add only the modular files the adventure needs.
5. Score [`QUALITY.md`](templates/adventure/QUALITY.md) (five-beat map, Coherence (prep), and 120-point checklist) before compiling.
6. Compile the playable material into `RUN.md` using `templates/adventure/SKELETON.md` and complete its verification checklist.
7. After play, record what happened separately. Promote established facts into the campaign's `world/` for linked play; promote into root `world/` only when the fact is setting-wide canon.

## Authority model

1. An explicit, active house rule may override the normal rules within its stated scope.
2. Otherwise, *Savage Worlds Adventure Edition*, Fifth Printing (2023), is the permanent mechanical authority.
3. An activated setting module may add setting content and rules only where compatible with SWADE. Older mechanics never silently replace SWADE mechanics.
4. Recorded rulings interpret unclear cases; they do not become house rules unless the GM explicitly promotes them.
5. If the sources do not establish a mechanic, mark it `RULE UNCLEAR - GM DECISION REQUIRED`. Do not invent a Savage Worlds mechanic.

Weird War II and Deadlands Noir are installed as optional modules. Neither has any effect unless an adventure activates it.

## Repository map

- `GM.md` - operating instructions for the GM and co-GM.
- `sources/` - read-only rulebooks, setting books, historical references, maps, and background texts.
- `rules/` - authority policy, explicit house rules, and recorded rulings.
- `world/` - setting-wide canon shared across tables: locations, factions, NPCs, and lore.
- `adventures/` - standalone units: one-shots and other adventures that are not split across a campaign.
- `campaigns/` - linked play: `CAMPAIGN.md`, campaign `world/` and `characters/`, and the child adventure folders beside them.
- `templates/` - files to copy when creating new material.
- `tools/` - workspace utilities, including the pregen [sheet printer](tools/print-sheets/) and the [`RUN.md` printer](tools/print-run/).
- `docs/` - design decisions for the workspace itself.

## Four kinds of truth

- **Source material:** what a rulebook, setting book, map, or historical source says.
- **Canon:** facts established as true in the game world.
- **Prep:** situations, possibilities, and secrets prepared for play.
- **Session record:** what actually happened at the table.

Prepared material is never automatically canon or session history.

