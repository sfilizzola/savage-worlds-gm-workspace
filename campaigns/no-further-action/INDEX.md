# No Further Action — Campaign Index

Router and compact inventory for this campaign. It tells you **where** a fact lives and **what tier** that fact belongs to.

`INDEX.md` is **never authoritative**. If this file and a linked source disagree, the linked source wins and this file is stale — fix it under [Maintenance contract](#9-maintenance-contract).

Scope: the No Further Action campaign only. Other campaigns, standalone adventures under `adventures/`, and setting-wide root `world/` are out of scope.

---

## Current-state warning: read before writing anything

- **`vozes-sem-corpo` is drafted preparation. It has not been played.** Its `ADVENTURE.md`, `plot.md`, `secrets.md`, `locations.md`, `encounters.md`, child `npcs/`, and `RUN.md` are prepared material, not session history.
- **Frank Loman remains missing in established play.** [`world/npcs/frank-loman.md`](world/npcs/frank-loman.md) and [`world/lore/timeline.md`](world/lore/timeline.md) record his fate as *not established*.
- The drafted night's **culprits, cause of death, body location, and evidence outcomes must not be promoted** into `world/`, the timeline, or any NPC file until the night is played and a session recap records what actually happened.
- Do not attribute Frank's death, Cal Briggs, Ray Holtz, Helen Loman, the inland tower compound, or the replay explanation to campaign canon. They are child-owned proposals. See [Adventure-local people and places](#76-adventure-local-people-and-places-child-owned).
- **`ClearWave` is unused prep.** January 1986 play did not establish that name. See [`neblina-sobre-o-lago/session-recap.md`](neblina-sobre-o-lago/session-recap.md), "Retired or contradicted prep".

---

## 1. Start here

Cheapest default read order. Stop as soon as the task is answered.

1. Workspace [`GM.md`](../../GM.md) — operating policy. Required first by [`AGENTS.md`](../../AGENTS.md).
2. This file — routing, status, inventories.
3. [`CAMPAIGN.md`](CAMPAIGN.md) — campaign configuration, predetermined truths, adventure index.
4. The one recap, world entity, or child adventure that the [Task router](#4-task-router) points at.
5. [`rules/RULES.md`](../../rules/RULES.md) — before writing any mechanics.

[`AGENTS.md`](../../AGENTS.md) additionally requires that before modifying a child adventure you read that child's `ADVENTURE.md` **and** this campaign's [`CAMPAIGN.md`](CAMPAIGN.md).

## 2. Current-state snapshot

Navigation summary only. Not authoritative; each row links to the source that is.

| Item | Current value | Authoritative source |
|---|---|---|
| Campaign status | `drafting`, solo player, player-supplied PC, SWADE Fifth Printing (2023) | [`CAMPAIGN.md`](CAMPAIGN.md) front matter |
| Active era and table date | January 1986, end of night 1, on Abigail Carr's call | [`neblina-sobre-o-lago/session-recap.md`](neblina-sobre-o-lago/session-recap.md), [`world/lore/timeline.md`](world/lore/timeline.md) |
| Latest played night | Night 1, `neblina-sobre-o-lago` | [`neblina-sobre-o-lago/session-recap.md`](neblina-sobre-o-lago/session-recap.md) |
| Next drafted night | Night 2, `vozes-sem-corpo` — prepared, unplayed; calendar is the morning after night 1 | [`vozes-sem-corpo/ADVENTURE.md`](vozes-sem-corpo/ADVENTURE.md) |
| Established unresolved state | Frank Loman missing; Whitley shelved the file; Abigail Carr's call unanswered. Full thread list: recap, "Unresolved questions and active threads" | [`neblina-sobre-o-lago/session-recap.md`](neblina-sobre-o-lago/session-recap.md), [`world/lore/timeline.md`](world/lore/timeline.md) |
| Current gate | 1986 → 1998 interstitial file is an empty job ticket; one of four 1986 recaps exists. Conditions: [Gates](#8-gates-and-danger-zones) | [`world/lore/between-1986-and-1998.md`](world/lore/between-1986-and-1998.md), [`CAMPAIGN.md`](CAMPAIGN.md) "Era gap (1986 → 1998)" |
| Character rank | Novice 1986 sheet only; Seasoned and Veteran sheets do not exist | [`characters/lilly-dawson.md`](characters/lilly-dawson.md) |

## 3. Canon and preparation ladder

Read top-down. A lower tier never overrides a higher one, and only tiers 1–3 may be spoken of as things that are true now.

| Tier | Owning files | May an agent treat it as history? |
|---|---|---|
| 1. What happened at the table | [`neblina-sobre-o-lago/session-recap.md`](neblina-sobre-o-lago/session-recap.md) | Yes. Recaps are the record of play. |
| 2. Promoted table canon and authored persistent entities | [`world/WORLD.md`](world/WORLD.md); persistent NPC and location files under [`world/npcs/`](world/npcs/README.md) and [`world/locations/`](world/locations/README.md), each gated by its own **Canon status** line; [`world/lore/timeline.md`](world/lore/timeline.md) (read section headers: established play vs working dates); [`world/lore/between-1986-and-1998.md`](world/lore/between-1986-and-1998.md) (empty job ticket). This tier does **not** include [`world/lore/the-concordance.md`](world/lore/the-concordance.md) or [`world/lore/revelation-ladder.md`](world/lore/revelation-ladder.md). | Only as far as each listed file's own **Canon status** line allows. `established` means it has appeared in or been promoted from play; `authored as true for this table; not yet in play` means true but never yet seen by the player. |
| 3. Campaign configuration and predetermined GM truths | [`CAMPAIGN.md`](CAMPAIGN.md), [`world/lore/the-concordance.md`](world/lore/the-concordance.md) | True for the table, but **not** player-known and **not** events. Do not let a 1986 speaker know tier-3 material. |
| 4. Plans and preparation | [`world/lore/revelation-ladder.md`](world/lore/revelation-ladder.md), every child adventure file, compiled `RUN.md` | No. This is intention and prepared situation. Outcomes here have not occurred. |
| 5. Design intentions with no files | The ten `concept` rows in [Adventure inventory](#6-adventure-inventory) | No. These are jobs on the calendar, not written adventures. |

Two boundary reminders from [`CAMPAIGN.md`](CAMPAIGN.md): `supernatural_level: subtle` is presentation, canon is **no supernatural**; and `setting_modules: []` means Deadlands Noir is **not** active — the investigation procedures are house rule `HR-NFA-002` only.

## 4. Task router

Open the narrowest source first. Prerequisite gates are named where they exist.

| Task | Read in this order | Gate |
|---|---|---|
| Orient to the campaign | [`GM.md`](../../GM.md) → this file → [`CAMPAIGN.md`](CAMPAIGN.md) | — |
| Determine what happened in play | [`neblina-sobre-o-lago/session-recap.md`](neblina-sobre-o-lago/session-recap.md) → [`world/lore/timeline.md`](world/lore/timeline.md) | Ignore all child prep and `RUN.md` for this question. |
| Run the next session at the table | [`vozes-sem-corpo/RUN.md`](vozes-sem-corpo/RUN.md) → [`vozes-sem-corpo/print/RUN.pdf`](vozes-sem-corpo/print/RUN.pdf) for A4; rebuild with [`tools/print-run/`](../../tools/print-run/README.md) | `RUN.md` is a compiled artifact. Rebuild it if any source under `vozes-sem-corpo/` changed. |
| Write or revise a child adventure | [`CAMPAIGN.md`](CAMPAIGN.md) → that child's `ADVENTURE.md` → its `plot.md`, `locations.md`, `encounters.md`, `secrets.md` → [`templates/adventure/SKELETON.md`](../../templates/adventure/SKELETON.md) | Score [`templates/adventure/QUALITY.md`](../../templates/adventure/QUALITY.md) into the child's `QUALITY.md` before compiling `RUN.md`. |
| Write or repair NPC portrayal | The entity's own file in [`world/npcs/`](world/npcs/README.md) or the child's `npcs/` → [`GM.md`](../../GM.md), "People, speech, and behavior" → [`.cursor/skills/npc-voice/SKILL.md`](../../.cursor/skills/npc-voice/SKILL.md) | A speaker may only know what that person could know. Tier-3 truths never leak into 1986 dialogue. |
| Inspect GM secrets and the long arc | [`world/lore/the-concordance.md`](world/lore/the-concordance.md) → [`world/lore/revelation-ladder.md`](world/lore/revelation-ladder.md) → [`CAMPAIGN.md`](CAMPAIGN.md), "Campaign predetermined truths" | Both lore files are GM-only. The ladder is planned delivery, not events. |
| Plan the 1998 era or rebuild Lilly | [`world/lore/between-1986-and-1998.md`](world/lore/between-1986-and-1998.md) → [`CAMPAIGN.md`](CAMPAIGN.md), "Rank and sheets" → [`characters/lilly-dawson.md`](characters/lilly-dawson.md) | **Blocked.** All four 1986 nights must be played and recapped first, and the interstitial file filled from those recaps — not from concept notes. |
| Select period radio or music | [`MUSIC.md`](MUSIC.md) → the child's `ADVENTURE.md` "Radio brief" | Diegetic only. Music never announces the solution. |
| Promote post-session canon | The new `session-recap.md` → [`GM.md`](../../GM.md), "Post-session discipline" → affected files in [`world/`](world/WORLD.md) → [`world/lore/timeline.md`](world/lore/timeline.md) → then update this index | Promote only what occurred. Retire contradicted prep instead of rewriting it as history. |
| Edit PC mechanics or print the sheet | [`characters/lilly-dawson.md`](characters/lilly-dawson.md) → [`characters/README.md`](characters/README.md) → [`characters/print/chars.json`](characters/print/chars.json) and [`characters/print/chars.pt-BR.json`](characters/print/chars.pt-BR.json) → [`tools/print-sheets/`](../../tools/print-sheets/README.md) | Mechanics change in the `.md` first, then both print extracts, then re-measure. Check [`rules/house-rules.md`](../../rules/house-rules.md) before any number moves. |

## 5. File-type legend

| File | Who owns it | What it is not |
|---|---|---|
| [`CAMPAIGN.md`](CAMPAIGN.md) | Campaign configuration, predetermined truths, party index, adventure index, canon boundaries. | Not table flow. Campaigns have no `QUALITY.md`. |
| [`world/WORLD.md`](world/WORLD.md) | Hub for persistent entities and the canon policy for this table. | Not a lore dump; payload lives in the entity files it links. |
| `session-recap.md` (in the played child) | The record of what happened at the table. Highest authority for history. | Not prep, and not a plan for the next night. |
| Child `ADVENTURE.md` | That night's configuration, intent, premise, predetermined truths, scope budget, quality gate. | Not campaign configuration, and not history. |
| Child `plot.md` | Story points, five-beat map, dynamic forces, end states. | Not a required scene order. |
| Child `locations.md` | Actionable location states and situations for that night. | Not persistent campaign geography until play promotes it. |
| Child `encounters.md` | Prepared combat and pressure situations with cited mechanics. | Not a balanced encounter budget. |
| Child `secrets.md` | GM-only truths for that night and their discovery vectors. | Not player-known, and not established until played. |
| Child `npcs/` | Adventure-local speakers, owned by that child. | Not campaign NPCs; promotion requires play plus a recap. |
| Child `characters.md` | Party assumptions and night hooks; links to the canonical sheet. | Never a second full mechanical sheet. |
| Child `QUALITY.md` | Scored quality gate plus the pass/fail Coherence (prep) block. | Not optional — a failed or missing coherence block blocks a ready compile. |
| Child `RUN.md` | **Compiled table artifact.** Built from reviewed sources for use at the table; may duplicate runtime information deliberately. | **Not canonical session history and not a source of truth.** Rebuild it when a source changes. |
| Child `print/` | Rendered A4 output of `RUN.md`. | Not hand-edited; regenerate with [`tools/print-run/`](../../tools/print-run/README.md). |
| [`characters/`](characters/README.md) | Canonical mechanical sheets for this campaign's PC, print extracts, and portraits. | Not a place for GM secrets or prepared outcomes. |
| [`MUSIC.md`](MUSIC.md) | Campaign radio direction, the selection test, KCRK details, era palette, research sources. | Not canon events; the retrospective palette is non-canon guidance. |

## 6. Adventure inventory

All twelve jobs from [`CAMPAIGN.md`](CAMPAIGN.md), each listed once. Concept rows have **no folder**; do not create stubs for them.

| # | Slug | Title | Status | Calendar | Folder | Key artifacts | Purpose |
|---|---|---|---|---|---|---|---|
| 1 | `neblina-sobre-o-lago` | Neblina sobre o Lago | played | Jan 1986 | [exists](neblina-sobre-o-lago/ADVENTURE.md) | [`ADVENTURE.md`](neblina-sobre-o-lago/ADVENTURE.md), [`session-recap.md`](neblina-sobre-o-lago/session-recap.md), [`characters.md`](neblina-sobre-o-lago/characters.md); no `RUN.md`, no `QUALITY.md` | The Loman missing-person case at Lake Barrow; ends on Abigail Carr's call. |
| 2 | `vozes-sem-corpo` | Vozes sem Corpo | drafting (preparation) | morning after night 1, Jan 1986 | [exists](vozes-sem-corpo/ADVENTURE.md) | **config** [`ADVENTURE.md`](vozes-sem-corpo/ADVENTURE.md) · **prep** [`plot.md`](vozes-sem-corpo/plot.md), [`locations.md`](vozes-sem-corpo/locations.md), [`encounters.md`](vozes-sem-corpo/encounters.md), [`secrets.md`](vozes-sem-corpo/secrets.md), [`characters.md`](vozes-sem-corpo/characters.md) · **quality gate** [`QUALITY.md`](vozes-sem-corpo/QUALITY.md) (coherence passed) · **table document** [`RUN.md`](vozes-sem-corpo/RUN.md), [`print/RUN.pdf`](vozes-sem-corpo/print/RUN.pdf) · **local NPCs** [`ray-holtz.md`](vozes-sem-corpo/npcs/ray-holtz.md), [`cal-briggs.md`](vozes-sem-corpo/npcs/cal-briggs.md), [`helen-loman.md`](vozes-sem-corpo/npcs/helen-loman.md) | The fresh call and the recording become a case. Only 1986 sequel. **Prepared outcomes are not history.** |
| 3 | `ashgrove-shots-1986` | (untitled; working) | concept | months later in 1986 | none | no files | Unrelated action cop case; its discovery trail can reach Whitley's local graft. |
| 4 | `ashgrove-puzzle-1986` | (untitled; working) | concept | later 1986, after night 3 | none | no files | Puzzle night and arc-1 finishing rhyme; the 1986 personal bruise sits in the paperwork. |
| 5 | `federal-in-ashgrove` | (untitled; working) | concept | 1998, spread through the year | none | no files | FBI in her town; first concrete Concordance language. **Gated** on [`world/lore/between-1986-and-1998.md`](world/lore/between-1986-and-1998.md). |
| 6 | `rhyme-out-of-town` | (untitled; working) | concept | 1998, weeks/months later | none | no files | Same practice, different zip code, outside Ashgrove. |
| 7 | `sealed-paper` | (untitled; working) | concept | 1998 | none | no files | The 1998 personal bruise: prison, blood, Medrick, the old PI. Not the 2016 lock. |
| 8 | `dead-letterhead` | (untitled; working) | concept | 1998 | none | no files | A shell that died and came back; one durable fact she can keep. |
| 9 | `written-in-real-time` | (untitled; working) | concept | 2016, hours/days | none | no files | Movement 1 of one urgent case: a No Further Action written in a living system. |
| 10 | `break-the-vendor` | (untitled; working) | concept | 2016, hours/days later | none | no files | Movement 2: attack capacity — lab, records, counsel — under time pressure. |
| 11 | `the-dawson-file` | (untitled; working) | concept | 2016, hours/days later | none | no files | Movement 3: origin and Concordance lock while the case is live. |
| 12 | `ashgrove-disposition` | (untitled; working) | concept | 2016, hours/days later | none | no files | Movement 4: takedown in Ashgrove. The haunt is a feeling; the proof is human. |

Calendar and era rules, the 1986 connection rule (nights 1–2 share Abigail's thread; nights 3–4 are separate jobs), and the per-era child exceptions live in [`CAMPAIGN.md`](CAMPAIGN.md).

## 7. Entity inventory

Routing metadata only — role, era, and state tag. Objectives, fears, portrayal, dialogue, secrets, and location payload stay in the entity files.

State tags: **played** · **authored — not played** · **mixed** (part played, part authored or GM) · **GM-only** · **preparation** (proposed by a child adventure, not yet true).

**played** means established in this table's play — it appeared in a session or was promoted from a recap. **authored — not played** means true for this table but never yet seen by the player, so it is canon an agent may use and not an event that has happened.

### 7.1 Recurring campaign NPCs

Hub: [`world/WORLD.md`](world/WORLD.md). Directory policy: [`world/npcs/README.md`](world/npcs/README.md).

| NPC | Role | Era | State |
|---|---|---|---|
| [Sgt. Tom Doyle](world/npcs/sgt-doyle.md) | Veteran sergeant-detective, Ashgrove PD; the other detective besides Lilly | 1986– | played |
| [Chief Whitley](world/npcs/chief-whitley.md) | 1986 police chief; 1998 former chief, civilian | 1986 and 1998 | mixed — chief and file-shelving played; graft, exit, and 1998 status are GM predetermined |
| [Nancy Iverson](world/npcs/nancy.md) | Precinct secretary; the flow of who-said-what | 1986– | played (surname authored after play) |
| [Abigail Carr](world/npcs/abigail-carr.md) | Radio host, KCRK 102.3 FM; the caller who ends night 1 | 1986– | mixed — the call is played; personality and motives are thin |
| [Frank Loman](world/npcs/frank-loman.md) | Local fisherman; the missing-person case | 1986 | played as **missing**; not present, not a speaker, fate not established |
| [Walt Kearney](world/npcs/walt-kearney.md) | Retired Ashgrove detective, still in town | 1986– | authored — not played |
| [Don Halvorsen](world/npcs/don-halvorsen.md) | Day patrol, Ashgrove PD | 1986– | authored — not played |
| [Andy Foyle](world/npcs/andy-foyle.md) | Day patrol, Ashgrove PD | 1986– | authored — not played |
| [Earl Voss](world/npcs/earl-voss.md) | Night patrol, Ashgrove PD; the sleeper | 1986– | authored — not played (town knowledge is mixed) |
| [Kevin Alder](world/npcs/kevin-alder.md) | Night patrol, Ashgrove PD; last hire before Lilly | 1986– | authored — not played |
| [Daisy Pell](world/npcs/daisy-pell.md) | Owns and works Daisy's | 1986– | authored — not played |
| [Len Pell](world/npcs/len-pell.md) | Cinder Creek yard after dark; Daisy's brother-in-law | 1986– | authored — not played (GM until Lilly is on the yard) |
| [Art Lindstrom](world/npcs/art-lindstrom.md) | Mayor of Ashgrove | 1986– | authored — not played (GM until a civic reason exists) |

### 7.2 Campaign locations

Directory policy: [`world/locations/README.md`](world/locations/README.md).

| Location | Function | Era | State |
|---|---|---|---|
| [Ashgrove, Oregon](world/locations/ashgrove.md) | The table's town; Lilly's posting | 1986– | mixed — posting established; named shops, schools, and civic people authored |
| [Lake Barrow](world/locations/lake-barrow.md) | Fishing water ~5 km out; site of the Loman scene | 1986 | played |
| [Ashgrove Police Precinct](world/locations/ashgrove-precinct.md) | Lilly's workplace | 1986– | mixed — workplace established; building scale, empty lab, patrol roster authored |
| [Daisy's](world/locations/daisys.md) | Town living room; diner and night-shift coffee | 1986– | authored — not played |
| [Cinder Creek Lumber](world/locations/cinder-creek-lumber.md) | Closed mill yard; night-shift geography | closed ~1982–84; play from 1986 | authored — not played |

### 7.3 Lore

Directory policy: [`world/lore/README.md`](world/lore/README.md).

| File | Holds | State |
|---|---|---|
| [Timeline](world/lore/timeline.md) | Authored background, what is established in play, working (not played) dates, and what is **not** established | mixed — read the section headers before quoting anything |
| [Between 1986 and 1998](world/lore/between-1986-and-1998.md) | The twelve interstitial years | empty job ticket — neither history nor prep; fill only from four played 1986 recaps |
| [The Concordance](world/lore/the-concordance.md) | The consortium, the manufactured serial-killer case, Medrick and Simon, the synchronization gap, the Ashgrove node, the supernatural boundary | GM-only predetermined truth; not player-known |
| [Revelation ladder](world/lore/revelation-ladder.md) | Planned delivery across 1986, 1998, and 2016, plus redundancy and anti-cliché guardrails | GM-only **plan**; only night 1 has happened |

### 7.4 Player character and print workflow

| File | Role |
|---|---|
| [`characters/README.md`](characters/README.md) | Directory contract, print commands, pt-BR rules, PT/EN trait glossary |
| [`characters/lilly-dawson.md`](characters/lilly-dawson.md) | **Mechanical source of truth.** Lilly Dawson, Novice 1986, Wild Card, player-supplied. Seasoned (1998) and Veteran (2016) sheets do not exist yet. |
| [`characters/print/chars.json`](characters/print/chars.json) | English print extract → `lilly.html` / `lilly.pdf` |
| [`characters/print/chars.pt-BR.json`](characters/print/chars.pt-BR.json) | pt-BR print extract → `lilly-pt.html` / `lilly-pt.pdf`; a reading aid, not a rules source |
| [`tools/print-sheets/`](../../tools/print-sheets/README.md) | A4 sheet printer and `measure.py`. Not a character generator, and never copied into an adventure. |

Portraits and era stills sit in `characters/` as player art; the sheet mounts `lilly-1986-id.png`.

### 7.5 Rules and radio

| File | Role |
|---|---|
| [`rules/RULES.md`](../../rules/RULES.md) | Operational precedence; read before writing mechanics |
| [`rules/house-rules.md`](../../rules/house-rules.md) | Active overrides. This campaign declares **HR-NFA-001** (fifteen skill points for Lilly) and **HR-NFA-002** (noir investigation procedures in SWADE names). |
| [`rules/rulings.md`](../../rules/rulings.md) | Dated situational decisions; precedents, not standing overrides |
| [`MUSIC.md`](MUSIC.md) | Diegetic-only radio policy, selection test, KCRK 102.3 FM, era palette, research sources |

Radio policy in one line: plausible airplay first, subtle resonance second, no lyrics quoted, and music never announces the solution. The campaign's technical fingerprint is the synchronization gap, not a melody.

### 7.6 Adventure-local people and places (child-owned)

Owned by `vozes-sem-corpo` and **not** campaign canon. They become persistent only if play establishes them and a recap promotes them into `world/`.

| Entity | Kind | Owner | State |
|---|---|---|---|
| [Ray Holtz](vozes-sem-corpo/npcs/ray-holtz.md) | adventure-local speaker (station) | `vozes-sem-corpo` | preparation — proposed adventure truth |
| [Cal Briggs](vozes-sem-corpo/npcs/cal-briggs.md) | adventure-local speaker (tower compound) | `vozes-sem-corpo` | preparation — proposed adventure truth |
| [Helen Loman](vozes-sem-corpo/npcs/helen-loman.md) | adventure-local speaker (family contact) | `vozes-sem-corpo` | preparation — proposed adventure-local person |
| 102.3 FM (station interior) | night situation | [`vozes-sem-corpo/locations.md`](vozes-sem-corpo/locations.md) | preparation — the frequency itself is campaign continuity in [`MUSIC.md`](MUSIC.md) |
| Ashgrove Records and Social Map | night situation | [`vozes-sem-corpo/locations.md`](vozes-sem-corpo/locations.md) | preparation — not campaign geography |
| Inland Tower Compound | night situation | [`vozes-sem-corpo/locations.md`](vozes-sem-corpo/locations.md) | preparation — not campaign geography |
| Disposition Desk | night situation | [`vozes-sem-corpo/locations.md`](vozes-sem-corpo/locations.md) | preparation — not campaign geography |

`neblina-sobre-o-lago` has no child `npcs/` or `locations.md`; its people and places were promoted into `world/` by [`session-recap.md`](neblina-sobre-o-lago/session-recap.md).

### 7.7 Off-screen names with no campaign NPC file

Named in play-adjacent material with **no campaign NPC file**. None is a missing file. Route to the owner and read the payload there.

| Name | Owner (route here) | Status |
|---|---|---|
| Simon Dawson | [`characters/lilly-dawson.md`](characters/lilly-dawson.md) (player-facing) · [`world/lore/the-concordance.md`](world/lore/the-concordance.md) (GM) | no campaign NPC file; off-screen |
| Medrick Dawson | [`characters/lilly-dawson.md`](characters/lilly-dawson.md) (player-facing) · [`world/lore/the-concordance.md`](world/lore/the-concordance.md) (GM) | no campaign NPC file; off-screen |
| Capt. Harold M. Keane | [`characters/lilly-dawson.md`](characters/lilly-dawson.md) · [`CAMPAIGN.md`](CAMPAIGN.md) · [`world/lore/timeline.md`](world/lore/timeline.md) | no campaign NPC file; off-screen |
| Ashley | [`characters/lilly-dawson.md`](characters/lilly-dawson.md) | no campaign NPC file; off-screen |
| Lilly's biological father | [`characters/lilly-dawson.md`](characters/lilly-dawson.md) (player-facing) · [`world/lore/the-concordance.md`](world/lore/the-concordance.md) (GM) | no campaign NPC file; off-screen |

## 8. Gates and danger zones

- **1986 → 1998 interstitial gate.** [`world/lore/between-1986-and-1998.md`](world/lore/between-1986-and-1998.md) is empty and blocks both `federal-in-ashgrove` design and the Seasoned rebuild. Its fill conditions and its "do not invent from unplayed notes" rule are stated in that file and in [`CAMPAIGN.md`](CAMPAIGN.md), "Era gap (1986 → 1998)".
- **Rank rebuilds are planned, not done.** Only the Novice 1986 sheet exists. Seasoned (1998) and Veteran (2016) rebuilds are described in [`CAMPAIGN.md`](CAMPAIGN.md) and have no files; the twelve years must come from the interstitial file.
- **Whitley: planned exit versus played history.** Played: he is the 1986 chief and he shelved the Loman file. Planned only: local graft, being taken off the force by the end of the 1986 arc via an unfair walk, and civilian status by 1998. Do not narrate the exit as something that happened. See [`world/npcs/chief-whitley.md`](world/npcs/chief-whitley.md).
- **KCRK 102.3 FM was authored after session one.** The call letters and frequency are continuity for future nights. Do not claim the player heard "102.3 FM" during night 1. See [`MUSIC.md`](MUSIC.md) and [`neblina-sobre-o-lago/session-recap.md`](neblina-sobre-o-lago/session-recap.md).
- **No faction files exist.** [`world/factions/`](world/factions/README.md) holds only its README. The Concordance currently lives entirely in [`world/lore/the-concordance.md`](world/lore/the-concordance.md) as GM-only predetermined truth. Do not create a faction file to make it feel discoverable.
- **Two `world/` directories.** Root [`world/`](../../world/WORLD.md) is setting-wide and deliberately empty of Ashgrove play state. This campaign's [`world/`](world/WORLD.md) holds this table's canon. Never write table play state into the root.
- **`RUN.md` is downstream.** [`vozes-sem-corpo/RUN.md`](vozes-sem-corpo/RUN.md) is compiled from that folder's sources. Editing `RUN.md` to change a fact leaves the sources authoritative and the compile stale.
- **Deadlands Noir is inactive.** No child may activate it as a setting module; `HR-NFA-002` supplies the investigation procedures.

## 9. Maintenance contract

Update this index when:

- an adventure changes status (concept → drafting → played);
- a child folder or key artifact is added, removed, or renamed — including a new `session-recap.md`, `QUALITY.md`, or `RUN.md`;
- a campaign NPC, location, lore file, or governing support file is added, removed, or renamed;
- an entity's state changes between authored, played, mixed, GM-only, or retired — including any promotion out of a child adventure;
- a prerequisite gate opens or changes, or the current-state snapshot stops matching the latest recap and timeline.

Do **not** update this index merely because portrayal text, prose, mechanics, clues, stat blocks, or other payload changed without changing navigation metadata.

When a night is played, the promotion order is: write the recap → promote established facts into `world/` and the timeline → retire contradicted prep → then correct the [Current-state warning](#current-state-warning-read-before-writing-anything), [Current-state snapshot](#2-current-state-snapshot), and the affected inventory rows here.
