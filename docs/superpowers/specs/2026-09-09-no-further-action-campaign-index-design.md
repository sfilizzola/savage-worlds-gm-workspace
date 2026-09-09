# No Further Action Campaign Index — Design

## Purpose

Create an agent-first, human-readable campaign index that lets future agents find the correct source with minimal file exploration and without confusing prepared outcomes with session history.

The index is a router and compact inventory. It does not become a new source of campaign truth.

## Scope

Create `campaigns/no-further-action/INDEX.md` and add thin entry-point links from:

- `campaigns/no-further-action/CAMPAIGN.md`
- `campaigns/no-further-action/world/WORLD.md`

The index covers only the No Further Action campaign. It does not index other campaigns, standalone adventures, or the entire workspace.

## Audience

Optimize the first screen and lookup paths for AI agents. Keep labels and explanations plain enough for the GM to use directly.

## Authority Boundaries

The index must state this authority order:

1. Session recaps record what happened at the table.
2. Campaign `world/` files hold promoted table canon and authored persistent entities, with each file's canon-status label controlling whether it has appeared in play.
3. `CAMPAIGN.md` and `world/lore/the-concordance.md` hold campaign configuration and predetermined GM truths.
4. `world/lore/revelation-ladder.md`, child-adventure files, and compiled `RUN.md` contain plans or preparation, not session history.
5. Concept adventure rows without folders are design intentions only.

`INDEX.md` summarizes locations and lookup responsibilities but is never authoritative over the linked source.

## Required Warning

The index must prominently preserve the current campaign-state trap:

- `vozes-sem-corpo` is drafted preparation, not played history.
- Frank Loman remains missing in established play.
- Prepared outcomes, culprits, body locations, and evidence in the drafted child must not be promoted until play and a session recap establish them.

## Index Structure

### 1. Start Here

Provide the cheapest default read order:

1. Workspace `GM.md`
2. Campaign `INDEX.md`
3. `CAMPAIGN.md`
4. The specific recap, world entity, or child adventure routed by the task
5. `rules/RULES.md` before mechanics

Also state that `AGENTS.md` requires reading the target `ADVENTURE.md` and campaign `CAMPAIGN.md` before modifying a child adventure.

### 2. Current State Snapshot

Give a small, explicitly non-authoritative navigation summary:

- active era and date
- latest played night
- next drafted night
- established unresolved state
- current campaign gate

Every item links to its authoritative source.

### 3. Canon and Preparation Ladder

Explain each information tier, its owning files, and whether an agent may treat it as history. Avoid reproducing lore payload.

### 4. Task Router

Provide minimal ordered file paths for these tasks:

- orient to the campaign
- determine what happened in play
- run the next session
- write or revise a child adventure
- write or repair NPC portrayal
- inspect GM secrets and the long arc
- plan the 1998 era or rebuild Lilly
- select period radio/music
- promote post-session canon
- edit PC mechanics or print the sheet

Routes should open the narrowest authoritative source first and call out any prerequisite gate.

### 5. File-Type Legend

Define the ownership of:

- `CAMPAIGN.md`
- `world/WORLD.md`
- `session-recap.md`
- child `ADVENTURE.md`
- `plot.md`, `locations.md`, `encounters.md`, `secrets.md`, and child `npcs/`
- `QUALITY.md`
- `RUN.md`
- campaign `characters/`
- `MUSIC.md`

The legend must explain that `RUN.md` is a compiled table artifact and not canonical session history.

### 6. Adventure Inventory

List all twelve campaign jobs with:

- slug and title
- status
- calendar/era
- folder state: existing or concept-only
- available key artifacts, such as recap, preparation, quality score, RUN, or no files
- one-line purpose

The inventory links to existing folders/files and visibly labels absent concept folders instead of creating stubs.

### 7. Entity Inventory

Provide one-line linked inventories for:

- recurring campaign NPCs
- campaign locations
- lore files
- player character and print workflow
- active house rules and radio policy

Each NPC/location line includes only enough metadata to route correctly:

- role or function
- relevant era
- state tag such as `played`, `authored—not played`, `GM-only`, or `mixed`

Full objectives, fears, dialogue, secrets, and location payload remain in entity files.

Adventure-local NPCs and locations receive a separate compact section. They remain owned by the child adventure until play makes them persistent and they are promoted.

Off-screen names without campaign NPC files—such as Simon, Medrick, and Captain Keane—are listed as pointers to their current owning lore/character source, not falsely presented as missing entity files.

### 8. Gates and Danger Zones

Call out:

- the 1986-to-1998 interstitial gate
- planned Seasoned/Veteran Lilly rebuilds
- Whitley's planned exit versus played history
- KCRK 102.3's post-session authorship
- empty faction directory and the fact that the Concordance currently lives in lore
- root `world/` versus campaign `world/`

### 9. Maintenance Contract

Update `INDEX.md` when:

- an adventure changes status
- a child folder or key artifact is added, removed, or renamed
- a campaign NPC, location, lore file, or governing support file is added, removed, or renamed
- an entity state changes between authored, played, mixed, or retired
- a prerequisite gate opens or changes

Do not update it merely because portrayal text, prose, mechanics, clues, or other payload changed without changing navigation metadata.

## Cross-Link Changes

Add one short entry-point line near the top of `CAMPAIGN.md` directing agents and GMs to `INDEX.md` for task routing.

Add one short backlink near the top of `world/WORLD.md` directing readers to the campaign index for adventure routes and canon tiers.

Do not duplicate the task router in either file.

## Verification

After implementation:

1. Verify every relative Markdown link in `INDEX.md` resolves.
2. Verify all twelve campaign jobs are represented exactly once.
3. Compare NPC and location inventories against `world/WORLD.md`.
4. Confirm the current-state warning agrees with the played recap and campaign timeline.
5. Confirm no prepared outcome is phrased as established history.
6. Confirm the maintenance contract is present.
7. Inspect the diff to ensure only the index and thin cross-links changed, apart from this design document.

## Non-Goals

- No workspace-wide index.
- No campaign encyclopedia.
- No new canon, NPC biographies, locations, factions, adventure stubs, or mechanics.
- No duplication of full lore, portrayal, clues, or RUN content.
- No automated index generator in this pass.
- No changes to the campaign's adventure design or current state.
