# Nothing Happens After Eleven Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Author night 3 of *No Further Action* as a drafting, table-compilable child adventure (`nothing-happens-after-eleven`) plus the persistent Hoot Owl location and the campaign-file corrections the spec requires.

**Architecture:** Copy the adventure template into a campaign child folder. Keep truths, story points, locations, secrets, and opposition in modular Markdown. Recurring people stay in campaign `world/`; one-night crew stay in the child's `npcs/`. Score `QUALITY.md` (numeric band, Coherence, Grounding audit) before compiling `RUN.md` from `templates/adventure/SKELETON.md`. Do not treat any prepared outcome as history.

**Tech Stack:** Markdown adventure sources; SWADE Fifth Printing (2023); house rules HR-NFA-001 and HR-NFA-002; Python `tools/print-run` renderer.

**Spec:** [`docs/superpowers/specs/2026-09-21-nothing-happens-after-eleven-design.md`](../specs/2026-09-21-nothing-happens-after-eleven-design.md)

## Global Constraints

- Follow `GM.md`, then `rules/RULES.md`, then `campaigns/no-further-action/CAMPAIGN.md`, then this child's `ADVENTURE.md` before writing mechanics.
- English repository and table material. Title: **Nothing Happens After Eleven**. Slug: `nothing-happens-after-eleven`.
- Child front matter: `status: drafting`, `language: en`, `format: one-shot`, `expected_runtime_hours: "3-5"`, `system: "SWADE Fifth Printing (2023)"`, `rank: "Novice"`, `players: "1"`, `pc_mode: player-supplied`, `setting_modules: []`, `supernatural_level: none`, `historical_accuracy.requirement: cinematic`, `house_rules: [HR-NFA-001, HR-NFA-002]`.
- No supernatural texture, no gap, no nausea, no ClearWave, no Concordance, no consortium speech, no Loman/Abigail/tower/lake as this night's problem.
- Night 3 ends with certainty without proof. Night 4 is where evidence and the unfair walk live. Do not take Whitley off the force in this child's end states.
- Earl is **not** bought. The CAMPAIGN.md line that his cruiser is bought is wrong; fix it in Task 7.
- `RUN.md` one-home rule: each speech, Trait table, stat block, and procedure appears once.
- Spoken lines: people with limited knowledge; follow `.cursor/skills/npc-voice/SKILL.md` when writing Portrayal and RUN speech.
- Working (not played) calendar pin: **Saturday 17 May 1986**, late spring. Label it working in the timeline.
- Locked names (use these; do not rename without editing this plan and the spec):
  - Local millwright Extra: **Ned Colfax**
  - Rookton night-runner Extra: **Roy Meeks**
  - Rookton hauler Extras: **Dale Runkle**, **Jimmy Sloat**
  - West End tenant who phones: **Rita Holm** (no dedicated NPC file unless portrayal needs more than a situation line)
  - Hoot Owl owner: **Pat Calhoun**
  - Cash go-between (GM-only, not on-screen as proof this night): **Marnie Quade**, Owl bartender; she passes envelopes and does not know the salvage
- Midnight phone (locked): the precinct **night line** rings in the **radio room**. Nancy is off. Doyle is at home. Kevin is already in the car westbound. Lilly is the only person in the building and **answers**.
- Rennicks stay off-screen. Rookton haulers are not the split-title buyer.
- Commit only if the user of that session asks; this plan's commit steps are optional checkpoints, not a standing order to push.

---

## File map

**Create (child):**

- `campaigns/no-further-action/nothing-happens-after-eleven/ADVENTURE.md`
- `campaigns/no-further-action/nothing-happens-after-eleven/plot.md`
- `campaigns/no-further-action/nothing-happens-after-eleven/locations.md`
- `campaigns/no-further-action/nothing-happens-after-eleven/secrets.md`
- `campaigns/no-further-action/nothing-happens-after-eleven/characters.md`
- `campaigns/no-further-action/nothing-happens-after-eleven/encounters.md`
- `campaigns/no-further-action/nothing-happens-after-eleven/QUALITY.md`
- `campaigns/no-further-action/nothing-happens-after-eleven/RUN.md`
- `campaigns/no-further-action/nothing-happens-after-eleven/npcs/ned-colfax.md`
- `campaigns/no-further-action/nothing-happens-after-eleven/npcs/roy-meeks.md`
- `campaigns/no-further-action/nothing-happens-after-eleven/npcs/dale-runkle.md` (short Extra file or a combined `haulers.md` if three one-page files are thinner together — prefer **one file** `npcs/rookton-haulers.md` for Runkle and Sloat, Meeks separate as the runner)

**Create (campaign):**

- `campaigns/no-further-action/world/locations/the-hoot-owl.md`

**Modify (campaign):** `CAMPAIGN.md`, `INDEX.md`, `world/WORLD.md`, `world/locations/ashgrove.md`, `world/locations/daisys.md`, `world/locations/cinder-creek-lumber.md`, `world/locations/ashgrove-precinct.md` (night line / radio room after midnight), `world/npcs/chief-whitley.md`, `world/npcs/earl-voss.md`, `world/npcs/kevin-alder.md`, `world/npcs/len-pell.md`, `world/npcs/daisy-pell.md`, `world/lore/timeline.md`, `world/lore/revelation-ladder.md`.

**Do not copy** `templates/adventure/SKELETON.md` into the child. Compile `RUN.md` from it.

---

### Task 1: Scaffold the child and author The Hoot Owl

**Files:**
- Create: `campaigns/no-further-action/nothing-happens-after-eleven/` from `templates/adventure/` (ADVENTURE, plot, locations, secrets, characters, encounters, QUALITY only — delete any copied `RUN.md` stub and do not copy `SKELETON.md`)
- Create: `campaigns/no-further-action/world/locations/the-hoot-owl.md`
- Modify: `campaigns/no-further-action/world/WORLD.md` (add Hoot Owl under Locations)
- Modify: `campaigns/no-further-action/world/locations/ashgrove.md` (the Main Street index already names Hoot Owl; add a relative link to the new file beside that name)
- Modify: `campaigns/no-further-action/INDEX.md` section 7.2 (add Hoot Owl row: authored — not played, persists 1986–2016)

**Interfaces:**
- Consumes: spec “Files this design implies”; `templates/location.md`
- Produces: empty-but-headed child files ready to fill; persistent Owl canon (name, door, owner, Wed/Sat mill-crowd drinking nights, persists through 2016, **not** the mill-plaza bar in `docs/gap-intentions.md`)

- [ ] **Step 1: Copy template files into the child**

From workspace root:

```bash
mkdir -p campaigns/no-further-action/nothing-happens-after-eleven/npcs
cp templates/adventure/ADVENTURE.md templates/adventure/plot.md templates/adventure/locations.md \
  templates/adventure/secrets.md templates/adventure/characters.md templates/adventure/encounters.md \
  templates/adventure/QUALITY.md \
  campaigns/no-further-action/nothing-happens-after-eleven/
```

Do not copy `templates/adventure/RUN.md` or `SKELETON.md`.

- [ ] **Step 2: Write `the-hoot-owl.md`**

Use `templates/location.md` fields. Required payload:

- Canon status: `authored as true for this table; not yet in play`
- Region: south side of Main / ORE. 328, numbered row between Pell's Hardware and leftover Ashgrove Arms (Sheet 2)
- Function: town pub through 2016
- Persistent truths: owner **Pat Calhoun**; mill-crowd drinking nights **Wednesday and Saturday**; **Len Pell** is a regular those nights; diegetic radio possible
- Current state (working May 1986, not history): tonight closed to walk-ins for **Oscar Lind's** mill old-shift send-off supper; overflow at Daisy's
- Secrets: none Concordance. GM: **Marnie Quade** sometimes passes an envelope; she does not know the mill job
- Maps: `ashgrove_town_map_1984.png`
- How ignored: stays the Main Street pub; a later plaza bar is a different place

- [ ] **Step 3: Link Owl from WORLD.md, ashgrove.md, INDEX 7.2**

- [ ] **Step 4: Smoke-check**

`ls campaigns/no-further-action/nothing-happens-after-eleven/` shows the seven copied files plus `npcs/`. `the-hoot-owl.md` has every location template field filled (no `TBD`).

---

### Task 2: Author persistent people and places this night needs

**Files:**
- Modify: `world/npcs/chief-whitley.md` — 1986 discovery: night 3 is certainty without proof; night 4 is the unfair walk. He is smart: he does not assign Lilly mill noise. Cash at a remove via Marnie/Owl, not haulers in person. He does not know about the magazine.
- Modify: `world/npcs/earl-voss.md` — West End/mill posting on Len's drinking nights; nested cruiser; asleep ~midnight–5am; **not graft**; Secret line must not say he is bought.
- Modify: `world/npcs/kevin-alder.md` — posted away those nights; has counted 328 flatbeds since winter and written nothing; 2am Daisy's coffee still true.
- Modify: `world/npcs/len-pell.md` — Wed/Sat at the Owl; Rennick key on a nail in the mill office when he drinks; tonight he went to the yard because the Owl was closed to walk-ins.
- Modify: `world/npcs/daisy-pell.md` — sister-in-law to Len; notices when he is absent on a drinking night; Owl overflow lands in her diner.
- Modify: `world/locations/cinder-creek-lumber.md` — leftover powder magazine inland of the stacks, never properly cleared (authored, not played); rail spur; Len's key.
- Modify: `world/locations/daisys.md` — next door to Owl overflow; Kevin coffee; Daisy/Len.
- Modify: `world/locations/ashgrove-precinct.md` — after midnight the **night line** rings in the radio room; no standing night clerk in 1986; if only Lilly is in the building, she can answer.

Keep each file's **Canon status** honest: new graft-machine facts are **authored as true; not yet in play**. Do not rewrite Session 2 history.

**Interfaces:**
- Consumes: spec predetermined truths
- Produces: campaign entities later SPs can point at instead of duplicating biographies

- [ ] **Step 1: Edit the eight files above** so a later agent can run the night without inventing Earl's nest or the night line.
- [ ] **Step 2: Grep the eight files for `bought` and `Concordance`.** Earl must not be bought. Nobody here lectures the machine.

---

### Task 3: Fill `ADVENTURE.md` and `characters.md`

**Files:**
- Create/fill: `campaigns/no-further-action/nothing-happens-after-eleven/ADVENTURE.md`
- Create/fill: `campaigns/no-further-action/nothing-happens-after-eleven/characters.md`

**Interfaces:**
- Consumes: spec Contract, Global Constraints front matter
- Produces: premise sentence that QUALITY Coherence will copy verbatim

- [ ] **Step 1: Front matter** exactly as Global Constraints. `historical_accuracy.sources` include `../MUSIC.md`. Status `drafting`.

- [ ] **Step 2: Resume work** — do not duplicate campaign lore. Replace the template list with a relative link to [`../INDEX.md`](../../INDEX.md) Resume work, and one line: child task is authoring night 3 from the spec.

- [ ] **Step 3: One-sentence premise** (QUALITY contract — use this sentence unchanged in QUALITY.md):

> After Whitley steers Lilly onto Main Street, a 00:20 West End power-loss call pulls her and Kevin to the Cinder Creek yard, where she must stop a salvage load-out, account for Len Pell, and write a scene that can be written.

- [ ] **Step 4: GM intent, player-facing mission, predetermined truths, objectives, stakes, starting state, scope budget, radio brief, quality-gate pointer** — copy truths from the spec; do not add new campaign secrets. Player-facing mission: answer the West End call, take the crew, account for Len. Secondary: notice the tuck-fold / roster / unsigned line / Kevin's trucks (certainty, not a filed graft case).

Scope budget: ~4–6 substantial situations; one reversal (not kids / not a simple outage; powder on the truck); one yard climax; no essential side quest.

Radio: diegetic only; plausible 1986 airplay; never announces the solution; cues at precinct and Daisy's if a radio is naturally on (`../MUSIC.md`).

- [ ] **Step 5: `characters.md`** — Lilly only; link `../characters/lilly-dawson.md`; no second sheet. Night hook: she is avoiding a boring Daisy's compliance walk by staying at her desk; that is why she hears the night line. Do not require a specific Edge.

---

### Task 4: Plot, night locations, secrets

**Files:**
- Fill: `plot.md`, `locations.md`, `secrets.md`

**Interfaces:**
- Consumes: premise; spec reachability vectors
- Produces: named story points SP1–SP6 for RUN compile; Grounding values (not categories)

**Story points (reachable, not a tour):**

| ID | Place | Job |
|---|---|---|
| SP1 | Precinct (Whitley's office → Lilly's desk → radio room) | Tuck-fold drop; Main Street assignment; 00:20 Rita Holm call; Kevin already west |
| SP2 | Daisy's (Owl overflow) | Optional / parallel. Packed mill crowd. Daisy: Len is not at the Owl. Vector if Lilly sat on the radio |
| SP3 | West End houses / mill-camp street | Confirm the outage; Rita; lights toward the yard; Earl not answering |
| SP4 | Mill fence / Earl's nest | Kevin on scene or arriving; nested cruiser; truck/lights; Len not walking his usual loop |
| SP5 | Cinder Creek yard (load-out) | Climax home: wreckers, truck, magazine clock, Len's state |
| SP6 | Paper after | Fold callback; salvage file vs mill-noise complaint; morning Whitley praise without proof |

Len clock (write in plot.md, not as a scripted corpse): if she rolls at once, locked or hurt and reachable; if she delays for Daisy's or Doyle, worse; if she never comes, Kevin alone and the load may move.

- [ ] **Step 1: `plot.md`** — five-beat map mapped onto SP1–SP6; dynamic forces (crew wants the truck gone, Whitley is at home, magazine as hazard); end states matching spec (full / costly / partial / failure) all leaving **certainty without proof**. Three-clue audit for: (1) this is salvage not an outage; (2) Len is the missing watchman; (3) Whitley has been keeping the lot unpublished (fold + roster + Ned's line + Kevin's trucks).

- [ ] **Step 2: `locations.md`** — situation boards for precinct, Daisy's, West End street, fence, yard (stacks, office/nail for the key, magazine bunker, rail spur). Mood = player-perceivable first impression. No Concordance.

- [ ] **Step 3: `secrets.md`** — GM-only: arrangement, Marnie envelopes, magazine contents, Ned's panic, Meeks pays for quiet, Whitley does not know powder. Discovery vectors only. Tag anything she cannot file this night.

- [ ] **Step 4: Grounding pass** — every Independent vector / Discoverable roll / Essential-information line has a value (Rita Holm, 00:20, Saturday 17 May 1986 working, Ned Colfax's line, the exact fold, Oscar Lind supper). No category standing in for a name.

---

### Task 5: Crew files, speech, encounters

**Files:**
- Create: `npcs/ned-colfax.md`, `npcs/roy-meeks.md`, `npcs/rookton-haulers.md` (Runkle, Sloat)
- Fill: `encounters.md`
- Read: `.cursor/skills/npc-voice/SKILL.md`, `rules/RULES.md`, `sources/systems/SWADE/reference/combat.md`, then the SWADE PDF for any explosives/fire gap; extend the cache if the topic will recur

**Interfaces:**
- Consumes: spec crew; SWADE Extra layout
- Produces: one home for each stat block (encounters.md and later the SP5 compile)

- [ ] **Step 1: Portrayal files** — limited knowledge. Ned knows the lot was supposed to be empty Wed/Sat; he does not know the chief's name as a client. Meeks wants the truck on 328. Haulers shoot to break contact. No consortium.

- [ ] **Step 2: `encounters.md`** — all four are **Extras** (solo Novice; do not put an opposing Wild Card on the yard). Cite SWADE page beside Traits. Illumination: night yard is **Dark (-4)** unless a work light is on a stack, then Dim in that cone (`combat.md` Illumination p.102). Cover: stacks, truck bed, mill office. Magazine: a **clock and a hazard**, not a required detonation. If fire reaches the bunker, use Area Effect / Blast Template only after checking the PDF; if authority is thin, write `RULE UNCLEAR - GM DECISION REQUIRED` rather than inventing a homebrew boom table. Recoil/Called Shots belong in RUN rules-quick-ref, not duplicated in three rooms.

- [ ] **Step 3: Lethality** — precinct safe; yard lethal after she chooses to enter. Re-entry: Kevin, Doyle by radio (time cost), Len if found able.

---

### Task 6: Score QUALITY.md and compile RUN.md

**Files:**
- Fill: `QUALITY.md`
- Create: `RUN.md` following `templates/adventure/SKELETON.md` document order

**Interfaces:**
- Consumes: premise sentence from ADVENTURE.md; SP1–SP6; encounter stats; speech
- Produces: ready-to-print table artifact (status stays `drafting` until the GM says `ready`)

- [ ] **Step 1: Score QUALITY.md** — five-beat map, 120-point ranks, Coherence three rows + logic summary, Grounding audit. Target ready band (≥100, or 80–99 with named repairs) **and** both pass/fail blocks passed. Do not compile as ready if Coherence or Grounding fails.

- [ ] **Step 2: Compile RUN.md** — every required skeleton block. Table-start **Current situation** is Phase A: Saturday evening, Whitley's office / Lilly still in the building (tuck already happened or happens as the first minutes). Phase B: 00:20 call. Do not describe the yard as already on the table at minute zero.

First 15 minutes: name SP1 trouble (steer + imminent call), not a map briefing. At-hand statistics use `> [!IMPORTANT]`; at-hand rules `> [!TIP]`; every content and blank line inside those alerts prefixed with `>`.

SP5 is the home for crew stats and Len procedure. Climax situation section is an **index** only.

NPC quick reference: index to SP homes, no reprinted speech.

- [ ] **Step 3: One-home check** — search RUN.md for duplicated Spoken lines or duplicated Extra stat blocks. One copy each.

- [ ] **Step 4: Leakage search** in the child folder:

```bash
rg -n -i 'ClearWave|Concordance|consortium|1:52|nausea|TBD|TODO' \
  campaigns/no-further-action/nothing-happens-after-eleven/
```

Expected: no ClearWave/consortium/1:52/nausea as this night's texture. `TODO`/`TBD` empty.

---

### Task 7: Campaign indexes and the arc-split correction

**Files:**
- Modify: `CAMPAIGN.md` adventure-index row for `nothing-happens-after-eleven`: status `drafting`; notes: salvage/Cinder Creek; Earl **not** bought; trail can make Lilly certain; **proof and unfair walk wait for night 4**. Predetermined-truth bullet that says “likely night 3” for taking Whitley off the force: rewrite to the spec's split.
- Modify: `INDEX.md` — Current-state warning / snapshot / Resume work / inventory row 3 (folder exists, drafting); open GM questions as needed; entity rows if Hoot Owl not added in Task 1.
- Modify: `world/lore/revelation-ladder.md` rung 3: independent crime; graft trail to certainty; **do not** say this night ends his tenure.
- Modify: `world/lore/timeline.md` working line: Saturday 17 May 1986 (working) action case at Cinder Creek; outcomes not history.

Do not fill `between-1986-and-1998.md`.

- [ ] **Step 1: Apply the four file classes above.**
- [ ] **Step 2: Confirm INDEX Resume work** lists: current task drafting night 3; last completed spec+plan; next action fill remaining child files or compile; files to open = child ADVENTURE.md + spec; derived outputs = RUN.html when compiled.

---

### Task 8: Verify print tooling and the diff

**Files:** none new. Test: `tools/print-run/`

- [ ] **Step 1: Printer unit tests**

```bash
python3 tools/print-run/test_print_run.py
```

Expected: pass.

- [ ] **Step 2: Render RUN.html** (PDF optional)

```bash
python3 tools/print-run/render.py campaigns/no-further-action/nothing-happens-after-eleven/RUN.md
```

Expected: HTML under `campaigns/no-further-action/nothing-happens-after-eleven/print/`. Do not hand-edit print output.

- [ ] **Step 3: `git diff --check`** and read the full diff. No secrets files outside GM-labeled sections. No promotion of prep to “established in play.”

---

## Spec coverage (self-review)

| Spec requirement | Task |
|---|---|
| Premise, arc split, no Concordance paper | 3, 4, 6, 7 |
| Tuck-fold open + callback | 4 (SP1, SP6) |
| Owl closed, Daisy overflow, Len on the lot | 1, 2, 4 |
| Earl nested, not bought | 2, 7 |
| Kevin: outage + counted trucks | 2, 4 |
| Lilly at desk, 00:20, night line | 2, 3, 4 |
| Mixed crew, magazine clock, all Extras | 5 |
| Four graft vectors, none evidence | 4 |
| End states leave proof for night 4 | 3, 4, 6 |
| Hoot Owl file + 2016 persistence | 1 |
| CAMPAIGN/INDEX/ladder/timeline corrections | 7 |
| QUALITY + SKELETON RUN + print | 6, 8 |
| SWADE cite / RULE UNCLEAR | 5 |

No `TBD` left: phone, names, working date, go-between name, send-off name (Oscar Lind) are locked here.
