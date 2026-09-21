# KCRK 102.3 FM — Campaign Location Design

Approved in conversation on 2026-09-21. Persistent campaign geography and staff for *No Further Action*. Design intent only until the files are written; writing them makes the station and Mel **authored as true for this table**. The building’s interior visit remains **played** (night 2). Nothing here is new session history.

## Contract

Add the missing campaign home for **KCRK 102.3 FM** (already labeled on Sheet 2 and played on night 2) plus **Mel Corwin** as a recurring person. Occasional help stays a cheap named pool on the location page.

This pass does **not** add a radio story to night 3 (`nothing-happens-after-eleven`). It does **not** compile `RUN.md`, reprint maps, or invent Concordance knowledge for station people.

**Approach:** civic location + people at Daisy’s / Hoot Owl density (Approach 1). Scope **B:** location file + full Mel NPC; helpers are notes, not NPC files.

## Predetermined truths (this pass)

- Call letters and frequency stay **KCRK 102.3 FM**. Geography lock stays Sheet 2: **south of the Ashgrove River**, east of the Bridge Street continuation, **Trapper Ridge** side. Short drive from Town Hall across the Bridge Street bridge. **Not** the inland tower compound. **Not** the east-grid powerline easement.
- **Mel Corwin** is owner **and** station manager (one man). He is about **67** in January 1986. He bought the station when mill spots still paid. He hosts a **fixed two-hour weekday afternoon** show of 1950s–60s classics and keeps **the books** (advertising ledger, program log, who may sign a work order). Abigail runs the rest of the schedule. The line she does not cross is his show and his books.
- Mel is **not** a morning body. Graveyard and morning belong to Abigail. That is why, on night 2, she could honestly say the station manager was not there, and why Ray’s “manager signs” stall worked. Do not invent a second manager.
- Lilly and Mel **have not been established as having met**.
- **Abigail Carr** remains the daily board / on-air host. Her played lines, the Session 2 studio rapport, and “Ray did not take the tapes” do not change.
- Occasional help (not default presence when Lilly visits):
  - **Hap Dwyer** — unofficial engineer. Retired mill electrician, ham in the shed. Mel trusts him with the transmitter and a sick board. Not on payroll; comes when Mel calls. Would not have treated a Water Authority sheet as his job. **Not present** on night 2.
  - **Ricky Boone** — intern. Ashgrove High, junior/senior in 1986. Files carts, shadows the board, coffee, wants a tape for a bigger market. Mel’s hire, not Abigail’s. After school and some Saturdays. Does not sign work orders and does not own keys.
  - **Bev March** — weekend voice. Saturday morning community hour (lost dogs, Grange, school sports, spots Mel already sold). Can run that slot. Does not manage the station. Not a second Abigail and not Mel’s classics block.
- None of these people know the Concordance, ClearWave, or what Ray and Cal were doing. Ray Holtz was never staff.
- Persistent rooms, thin, from night-2 play: **front office**, **studio**, **one public exit**, **one service exit**, lot of **wet river gravel and asphalt fines**. No full floor plan, cart library, or weekly grid.

## Files

| File | Action |
|---|---|
| `campaigns/no-further-action/world/locations/kcrk.md` | **Create** from `templates/location.md`. Place payload lives here. |
| `campaigns/no-further-action/world/npcs/mel-corwin.md` | **Create** from `templates/npc.md`. Mel’s portrayal lives here. No statistics. |
| `campaigns/no-further-action/world/npcs/abigail-carr.md` | **Edit in place:** employer paragraph becomes a short pointer to Mel’s file. Do not rewrite played spoken lines or Session 2 rapport. Keep call letters and geography in her Role line. |
| `campaigns/no-further-action/world/WORLD.md` | Add KCRK under Locations and Mel under NPCs. |
| `campaigns/no-further-action/INDEX.md` | Add inventory rows (§7.1 Mel, §7.2 KCRK). Update Resume work after authoring. Do not recopy portrayal into the index. |
| `campaigns/no-further-action/world/locations/ashgrove.md` | People/radio lines: name Mel as owner/manager; keep existing KCRK geography lock. Do not reprint the PNG. |
| `campaigns/no-further-action/MUSIC.md` | **No change.** Still owns format and diegetic policy. |
| `campaigns/no-further-action/vozes-sem-corpo/locations.md` | **No change.** Leftover night-2 situation boards. Recap + campaign files win if they disagree. |
| Night 3 folder, `CAMPAIGN.md` predetermined truths, maps, `RUN.md` | **Out of scope.** |

## Canon status

**KCRK location**

- **Canon status:** mixed — studio and lot **established in play** (night 2); Mel’s schedule, books, and the helper pool **authored as true for this table; not yet in play**.
- **Current state:** ordinary small FM after night 2. Ray is dead and was never staff. Daily work is not the reel-custody crisis. Working May 1986 (night 3 calendar) does not change owner, DJ, or cheap help.

**Mel Corwin**

- **Canon status:** authored as true for this table; not yet in play.
- **Visibility:** mixed — night 2 established a **station manager** who was not in the building; the name **Mel Corwin**, his age, his afternoon show, and his books are authored and have not been spoken at the table. He has not appeared on-screen.
- Played fact that stays: the manager was absent that morning.

**Helpers**

- Authored as true; not yet in play. No `world/npcs/` files. Promote one person later only if a night needs them as a real speaker.

**INDEX state tags**

- KCRK: **mixed**.
- Mel Corwin: **authored — not played**.

## Location file contents (`kcrk.md`)

Follow `templates/location.md` field order. Density like [`the-hoot-owl.md`](../../../campaigns/no-further-action/world/locations/the-hoot-owl.md) / [`daisys.md`](../../../campaigns/no-further-action/world/locations/daisys.md).

- **Function:** Ashgrove’s local FM; Abigail’s workplace; Mel’s license and books.
- **First impression:** player-perceivable only; cold rain, cramped boards, monitor music, tape. No secrets, no Ray, no reel counters.
- **Persistent truths:** call letters; Sheet 2 lock; Mel owner/manager; Abigail daily board; weekday afternoon classics; helper pool with the three names above; rooms/exits/lot; not the inland tower.
- **People/factions:** Mel, Abigail, Hap, Ricky, Bev. Link Abigail’s and Mel’s NPC files. No Concordance.
- **Resources and hazards:** airtime, logs, a service door, gossip that is human. A stranger with a work order is a person, not a faction.
- **Secrets:** none involving the Concordance.
- **How it changes if ignored:** still broadcasts; Mel still does his two hours; Abigail still has a job.
- **Maps/handouts:** Sheet 2 (`ashgrove_town_map_1984.png`); no new handout.

Do **not** copy night-2 Trait tables, Handouts B/C, Ray’s lines, reel counters 0418/0419, or Ray’s 8:45 arrival into this file. Those stay in leftover child prep and/or the night-2 recap.

## Mel file contents (`mel-corwin.md`)

Follow `templates/npc.md`. Extra, unstatted (same rule as Abigail).

- **Role:** Owner and station manager, KCRK 102.3 FM; weekday afternoon classics host.
- **Current objective:** Keep the station a real local signal that still plays the records he loves; keep Abigail on the board because she is good; keep the books and the two-hour block under his hand.
- **Fear:** A stranger with paper taking tape or gear he did not authorize; looking like a joke to Rookton; anyone treating his two hours as filler.
- **Leverage/resources:** Keys, signature on work orders, advertising ledger, airtime, Hap’s phone number.
- **Secret:** none about the consortium.
- **Relationships:** Abigail (trusts her energy; she does not touch his show or books); Hap (calls when gear is sick); Ricky (his intern); Bev (Saturday community hour); Lilly (not established as having met — polite, territorial about logs, will talk music longer than police business; likes that a detective took Abigail seriously, still will not hand originals without a signature he understands).
- **If ignored:** He still does the two hours and the books.
- **Portrayal:** Late 60s; speech in call letters, logs, carts, “the board,” first names. Avoid explaining the lake, treating Ray as a known engineer, or knowing the consortium.
- **Spoken lines:** write 1–3 table cues in Mel’s register (not slogans, not a briefing). Use `.cursor/skills/npc-voice/` when drafting them.
- **Pressure variants:** Cooperate / Refuse / Threatened / Ignored, same person.
- **Mechanics:** Extra; no Trait block unless a later night needs a contest.

## Abigail edit (narrow)

In `abigail-carr.md` Relationships and Background, replace the duplicated Mel biography with: she works for **Mel Corwin** ([`mel-corwin.md`](mel-corwin.md)) — owner and station manager; she does not touch his two-hour classics show or his books. Keep her Role (KCRK, age, Sheet 2), played lines, and night-2 refuse line (“Station manager isn't here…”) as **her** speech; the new Mel file explains why that was true.

## Hard no’s

- Night-3 plot, quality rescore, or radio story point.
- `RUN.md` compile or print.
- Helper NPC files under `world/npcs/` or anything in `characters/`.
- Statistics for Mel or the pool.
- Concordance, ClearWave, inland-tower, or nausea mechanism in these mouths.
- New Mel family, simulated FCC procedure, 1998 ownership sale, or automation bible.
- Expanding `MUSIC.md` into a staff roster or turning `kcrk.md` into a playlist.
- Reprinting `ashgrove_town_map_1984.png`.
- Promoting leftover `vozes-sem-corpo` crisis state as the campaign location’s current state.

## Success

An agent can open `kcrk.md` and `mel-corwin.md` and run a later visit without reading night-2 leftover boards for “who works here.” INDEX/WORLD route to those files. Night 2 recap remains the authority for what happened that morning. Night 3 is untouched.
