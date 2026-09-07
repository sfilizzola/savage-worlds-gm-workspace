# How to Use the Savage Worlds GM Authoring Workspace

This workspace is designed to be used as an ongoing Codex project. Playable material has two roots:

- **Standalone adventures** live in `adventures/<adventure-slug>/`: a one-shot, or any unit that is not split across linked sessions.
- **Linked play** lives in `campaigns/<campaign-slug>/`, where `CAMPAIGN.md`, the campaign's `world/`, and its canonical `characters/` sit beside ordinary child adventure folders.

The rest of the repository provides instructions, rules authority, setting-wide world canon, sources, and templates.

Either order is valid: create a campaign first and add child adventures, or start with a standalone adventure and adopt it into a campaign later.

The normal lifecycle of one adventure — standalone or campaign child — is:

```text
Premise
  -> configure ADVENTURE.md
  -> develop modular preparation
  -> score QUALITY.md (five-beat map, Coherence (prep), and 120-point checklist)
  -> verify rules and historical details
  -> compile RUN.md
  -> play
  -> create a session recap
  -> approve canon changes
  -> prepare the next session
```

## 1. One-time Codex setup

Open the root folder of this workspace in Codex.

Codex automatically discovers project instructions from a root-level `AGENTS.md`. The framework uses `GM.md` as its detailed co-GM policy, so create an `AGENTS.md` beside `GM.md` with the following content:

```md
# RPG Workspace Instructions

Before performing any RPG authoring, editing, rules verification, or session-preparation task:

1. Read and follow `GM.md`.
2. Treat `GM.md` as the authoritative operating policy for this workspace.
3. Read `rules/RULES.md` before writing mechanics.
4. Read the target adventure's `ADVENTURE.md` before modifying it.
5. When the target adventure is under `campaigns/`, also read that campaign's `CAMPAIGN.md`.
6. Do not treat preparation as established canon or session history.
7. When generating or substantially revising an adventure, fill and score `QUALITY.md` from `templates/adventure/QUALITY.md` before compiling `RUN.md`.
8. When compiling `RUN.md`, follow `templates/adventure/SKELETON.md` (including **Table flow (one home)**). Do not omit required blocks.
9. Pregen A4 print uses `tools/print-sheets/` (sheet printer, not a generator). Do not put a sheet renderer inside an adventure.
10. Table print of `RUN.md` uses `tools/print-run/`. Do not put a RUN renderer inside an adventure.
```

Start a new Codex task after adding `AGENTS.md` so that the instructions are loaded from the beginning.

You can verify the setup with this prompt:

```text
Before doing any work, tell me which workspace instruction files you found and summarize the RPG rules-authority hierarchy.
```

The expected hierarchy is:

1. An explicit house rule activated by the adventure may override the normal rules within its written scope.
2. Otherwise, SWADE Fifth Printing (2023) is the permanent mechanical authority.
3. An active setting module may add compatible content and rules.
4. Recorded rulings interpret unclear cases but are not automatically house rules.
5. The co-GM must never invent Savage Worlds mechanics.

## 2. Start a campaign or short arc

Choose this root when several sessions will share the same party, the same evolving canon, and a common pressure. A single night with a decisive ending belongs under `adventures/` instead.

The campaign context comes first; each night or arc chapter is then designed and created as its own child adventure.

### Create the campaign root

Do this once, before any child adventure exists:

1. Copy `templates/campaign/` to `campaigns/<campaign-slug>/`.
2. Complete `CAMPAIGN.md`: every front-matter field, the one-sentence throughline, GM intent, campaign predetermined truths, canon boundaries, and child-adventure exceptions.
3. Create the canonical party sheets under `campaigns/<campaign-slug>/characters/`, with the print extract in `campaigns/<campaign-slug>/characters/print/chars.json`. Child adventures link to these sheets and never keep a second full mechanical sheet.
4. Write campaign canon under `campaigns/<campaign-slug>/world/` only when it is established as canon for this table. Predetermined GM canon, secrets, and recurring campaign NPCs may be written during prep before session 1 if they are already true for this table; label them clearly. Planned events and unused preparation do not become history or canon merely because they were drafted. Setting-wide canon shared across tables stays in the repository-root `world/`.

A useful opening prompt:

```text
I want to start a linked Savage Worlds campaign in this workspace.

Premise: [describe the arc]

Act as the co-GM defined in `GM.md`. First read `campaigns/README.md` and `templates/campaign/CAMPAIGN.md`.

Interview me one focused question at a time until the throughline, format, Rank, player count, PC workflow, active setting modules, supernatural level, historical-accuracy requirement and sources, house rules, and canon boundaries are decided.

Then create `campaigns/<campaign-slug>/` from `templates/campaign/` and complete `CAMPAIGN.md`. Do not create child adventures yet; we will design each one separately.
```

`CAMPAIGN.md` is configuration and indexes. It is never compiled as table flow: a campaign has no `QUALITY.md` and no campaign-root `RUN.md`.

### Add a child adventure to the campaign

Design each child when its concept is ready, not in advance. Start with:

```text
I want to add the next child adventure to this campaign.

Premise: [describe this night or arc chapter]

Act as the co-GM defined in `GM.md`. First read this campaign's `CAMPAIGN.md`, its `world/` canon, its `characters/` sheets, and the latest child recap if one exists.

Interview me one focused question at a time about this child's runtime, truths, objective, stakes, and situations. Keep the campaign throughline. Reuse the campaign's declared Rank, player count, PC workflow, setting modules, supernatural level, historical-accuracy requirement, and house rules unless I record a child-adventure exception.

Do not create files until the essential decisions are clear. Challenge single points of failure, excessive scope, railroading, and risks that could remove a player early.
```

Once you approve the concept, tell Codex:

```text
Create this child adventure as `campaigns/<campaign-slug>/<adventure-slug>/` by copying `templates/adventure/` except `SKELETON.md`; compile `RUN.md` against the skeleton later. The child folder sits directly beside the campaign's `world/` and `characters/`, not inside them.

Repeat the campaign's shared configuration in the child's `ADVENTURE.md`: `system`, `rank`, `pc_mode`, `setting_modules`, `supernatural_level`, `historical_accuracy`, and `house_rules`, unless a recorded child-adventure exception says otherwise.

Do not copy full party sheets into the child; link this campaign's `characters/` sheets instead. Include only the optional files and sections that are useful for this child.

Then add the child to the adventure index in `CAMPAIGN.md`.
```

Once the child folder exists, the rest of this document applies to it unchanged: configure its `ADVENTURE.md` (section 5), develop it in focused passes, verify rules and history, score its own `QUALITY.md`, and compile its own `RUN.md`. Section 4 covers only the standalone case.

## 3. Adopt a standalone adventure into a campaign

You do not have to decide the shape in advance. Campaign-first and adventure-first both work: an existing standalone adventure can become a campaign child later.

First create the campaign root as described in "Create the campaign root" above, or open the existing `campaigns/<campaign-slug>/`. Then move the whole adventure folder so Git keeps its history:

```text
git mv adventures/<adventure-slug> campaigns/<campaign-slug>/<adventure-slug>
```

Then finish the adoption:

1. If the campaign does not yet own the party, **move** the child's full mechanical sheets and `print/chars.json` into `campaigns/<campaign-slug>/characters/`. Those become the canonical campaign copies.
2. If both campaign and child copies already exist, keep the campaign copies. Diff the child's full sheets against them, reconcile any child-only changes into the campaign sheets, then delete the duplicate full child sheets (including a child `print/chars.json` if it remains).
3. Leave the child's `characters.md` as night hooks, spotlight notes, and links to the campaign sheets — not a second full sheet.
4. Promote only recurring facts, locations, factions, and NPCs into `campaigns/<campaign-slug>/world/`. Night-specific prep, situation detail, and unspent secrets stay in the child adventure.
5. Add the child to the adventure index in `CAMPAIGN.md`, and reconcile its `ADVENTURE.md` with the campaign configuration or record a child-adventure exception.
6. Repair hardcoded old paths: printer commands, cross-file links, wrapper scripts, recaps, and any remaining `adventures/<adventure-slug>/…` reference.
7. Do not leave a duplicate copy or a placeholder stub under `adventures/`. The adventure must have exactly one home.

Operation Hinterland appears in this document only as a standalone example. It is not part of a campaign and should not be moved.

## 4. Start a standalone adventure from a premise

Start one Codex task for each adventure. Keeping the adventure in one task makes its design discussion easier to follow, while the files preserve the lasting state.

This section creates a standalone unit under `adventures/<adventure-slug>/`. For a campaign child, use "Add a child adventure to the campaign" in section 2 instead. From section 5 onward, the guidance is identical for both roots.

Send this prompt:

```text
I want to create a new Savage Worlds adventure in this workspace.

Premise: [describe your initial idea]

Act as the co-GM defined in `GM.md`. First inspect the workspace instructions, rules authority, available sources, and adventure templates.

Help me define the adventure step by step. Ask one focused question at a time. We must decide the Rank, player count, PC workflow, active setting modules, supernatural level, historical-accuracy requirement and sources, house rules, runtime, truths, objectives, and stakes.

Do not create the adventure files until the essential decisions are clear. Challenge single points of failure, excessive scope, railroading, and risks that could remove a player early.
```

Example premise:

```text
December 1944. Allied soldiers must infiltrate a fortified medieval town in Germany during a winter offensive.
```

Codex should interview you rather than immediately writing a complete adventure. Answer the questions and refine the concept until the main decisions are clear.

Once you approve the concept, tell Codex:

```text
Create the adventure as `adventures/operation-winter-wolf/` using the adventure templates. Include only the optional files and sections that are useful for this adventure. Do not copy `templates/adventure/SKELETON.md` into the adventure directory; compile `RUN.md` against it later.
```

Replace `operation-winter-wolf` with a short lowercase name separated by hyphens.

## 5. Configure `ADVENTURE.md`

Every adventure must declare:

- title and status;
- default language;
- one-shot, short-arc, or campaign format;
- expected runtime;
- SWADE Rank;
- player-count range;
- pregenerated PCs, player-supplied PCs, or both;
- active setting modules;
- supernatural level;
- historical-accuracy requirement, scope, and sources;
- active house rules, or explicitly `none`.

A configuration might look like:

```yaml
---
title: "Operation Winter Wolf"
status: drafting
language: en
format: one-shot
expected_runtime_hours: "6"
system: "SWADE Fifth Printing (2023)"
rank: "Novice"
players: "4-6"
pc_mode: both
setting_modules:
  - Weird War II
supernatural_level: subtle
historical_accuracy:
  requirement: researched
  scope: "Units, weapons, geography, weather, and military terminology"
  sources:
    - "List the historical sources used here"
house_rules: none
---
```

Do not begin detailed mechanical preparation while required configuration fields remain undecided.

## 6. Activate Weird War II only when needed

Weird War II is installed but inactive by default. Activate it explicitly in the adventure:

```yaml
setting_modules:
  - Weird War II
```

If the adventure does not use it, declare:

```yaml
setting_modules: []
```

Select the supernatural level independently:

- `none`: historical WWII without occult events.
- `subtle`: supernatural truth exists but is initially ambiguous.
- `moderate`: supernatural elements become an important part of the adventure.
- `full`: overt Weird War action from the beginning.

Even when Weird War II is active, SWADE Fifth Printing remains the default mechanical authority. Weird War II predates SWADE, so older mechanics require compatibility review. Only an explicit active house rule may deliberately override SWADE.

## 7. Develop the adventure in focused passes

Do not ask Codex to write everything in one enormous pass. Develop and review one responsibility at a time.

Useful assignments include:

```text
Develop the predetermined truths, main objective, story points, pressures, and possible end states. Do not write a mandatory scene sequence.
```

```text
Stress-test this plot for single points of failure. Identify any clue, roll, NPC, location, item, or PC whose loss could stop progress. Propose repairs without removing meaningful failure.
```

```text
Review every essential revelation. Create multiple independent ways it could be discovered through people, places, observations, records, or consequences. Do not turn them into a mandatory checklist.
```

```text
Develop the adventure locations as flexible situations. Describe the people, pressures, environment, discoverable information (Trait / fail / success / raise), quoted spoken lines, hazards, escalation, and relevant verified mechanics. Do not list a menu of expected player solutions.
```

```text
Review whether the current scope fits a focused one-shot. Target 3–4 hours and 4–6 substantial situations. Identify essential material, optional material, a 3–4 hour core, likely pacing checkpoints, and the first cuts if the group falls behind. The opening must put trouble in motion within 10–15 minutes of play.
```

```text
Score this adventure using templates/adventure/QUALITY.md copied into the adventure as QUALITY.md.

Fill the five-beat map. Fill Coherence (prep): copy the one-sentence premise, score the three pass/fail rows with cited evidence, and write the logic summary only if all three pass. Score each ranked item 0–5, multiply by its weight, total out of 120, and name the weakest ranks.

Treat beats as a pacing diagnostic, not a scene script. Do not convert them into a mandatory visit order. The logic summary is reachable paths, not a visit order.

If any coherence row fails, or the logic summary is missing after a pass, repair before compiling RUN.md even if the numeric total is high. If the total is below 100, propose repairs to objective, agency, pacing, climax, or the weakest ranks before compiling RUN.md. Do not force a Chase or Dramatic Task that the fiction does not need.
```

For substantial revisions, ask Codex to explain its proposed changes before editing:

```text
Review this part of the adventure and propose improvements first. Do not modify files until I approve the direction.
```

## 8. Create or integrate player characters

Decide where the sheets live before writing them:

- **Standalone adventure:** full mechanical sheets in `adventures/<adventure-slug>/characters/<name>.md`, print extract in `adventures/<adventure-slug>/characters/print/chars.json`.
- **Campaign child:** full mechanical sheets and `print/chars.json` always live in `campaigns/<campaign-slug>/characters/`, because the party belongs to the table and not to one night. The child's `characters.md` holds only night hooks, spotlight notes, and links to those sheets. Never duplicate a full sheet inside a child adventure.

### Pregenerated PCs

Use:

```text
Create [number] pregenerated player characters for this adventure at the declared Rank. Give each one a reason to accept the mission, a personal stake, useful relationships with other PCs, and an opportunity for spotlight play. Verify every mechanical element against the active rules authority.

Write the full mechanical sheets in this adventure's `characters/` directory. If this adventure is a campaign child under `campaigns/`, write the full sheets and the print extract in `campaigns/<campaign-slug>/characters/` instead, and keep only night hooks and links to those sheets in the child's `characters.md`.
```

Review the characters before approving them. Make sure the adventure does not depend on one specific character, Edge, power, or skill.

For table print, use the workspace sheet printer — not a character generator. It lives at [`tools/print-sheets/`](tools/print-sheets/README.md). Point the printer at the `print/chars.json` that belongs to the owning directory decided above.

For a standalone adventure:

```text
python3 tools/print-sheets/render.py adventures/<adventure-slug>/characters/print/chars.json
```

For a campaign party:

```text
python3 tools/print-sheets/render.py campaigns/<campaign-slug>/characters/print/chars.json
```

Operation Hinterland is a standalone adventure and also keeps a wrapper: `adventures/operation-hinterland/characters/print/build_sheets.py`. Call letters stay with that adventure (`handouts/print/build_letters.py`).

For the GM run packet, print the adventure's `RUN.md` with the workspace run printer:

```text
python3 tools/print-run/render.py adventures/<adventure-slug>/RUN.md --pdf
python3 tools/print-run/render.py campaigns/<campaign-slug>/<adventure-slug>/RUN.md --pdf
```

Edit `RUN.md`, not the generated `print/RUN.html` / `print/RUN.pdf`. Open the PDF on a tablet the same way you would flip paper.

### Player-supplied PCs

Add the character files or summaries to the owning directory: the standalone adventure's `characters/`, or `campaigns/<campaign-slug>/characters/` for a campaign child. Then use:

```text
Review these player-supplied characters against `ADVENTURE.md`, and against `CAMPAIGN.md` as well if this adventure is a campaign child. Check Rank, allowed sources, setting compatibility, historical equipment, mission hooks, powers, Edges, and special abilities. Identify adaptation needs, but do not change the characters without my approval.

Keep the approved full sheets in the owning `characters/` directory. For a campaign child that is `campaigns/<campaign-slug>/characters/`; the child's `characters.md` may only add night hooks and links.
```

### Supporting both

When `pc_mode: both`, pregenerated characters can also serve as replacement or reserve characters.

The adventure should avoid random opening situations likely to remove a player from most of the session. Later lethal consequences are acceptable once the players have participated meaningfully and the danger has been communicated.

Prepare a re-entry option:

```text
Review the adventure for early character removal. Prepare a fictionally appropriate reserve PC, replacement entry point, or temporary allied character so a player can return promptly if removal still occurs.
```

## 9. Verify Savage Worlds mechanics

Before final preparation, use:

```text
Perform a mechanical verification pass on this adventure.

For every stat block, modifier, hazard, item, ability, power, and subsystem:

1. Check the explicit active house rules.
2. Otherwise consult SWADE Fifth Printing (2023).
3. Consult only the setting modules activated in `ADVENTURE.md`.
4. Flag older-edition conflicts and adapt them to SWADE without silently changing the source's intent.
5. Add precise title and page or section references.
6. Mark unresolved cases as `RULE UNCLEAR - GM DECISION REQUIRED`.

Do not invent mechanics and do not reproduce long passages from the books.
```

When a decision is required, make the ruling as GM. Record situational decisions in `rules/rulings.md`. Add something to `rules/house-rules.md` only when you deliberately want a reusable standing override.

## 10. Verify historical material

If the adventure declares `cinematic`, `researched`, or `strict` historical accuracy, add relevant maps, books, articles, images, and texts under:

```text
sources/background/
```

or with the owning adventure:

```text
adventures/<adventure-slug>/sources/
campaigns/<campaign-slug>/<adventure-slug>/sources/
```

Then use:

```text
Review the historical claims in this adventure according to its declared accuracy level. Check dates, geography, units, ranks, equipment, weather, terminology, and political conditions against the listed background sources.

Separate verified fact, plausible inference, intentional alteration, and unresolved uncertainty. Do not allow historical flavor sources to overrule Savage Worlds mechanics.
```

Record provenance and usage rights for maps, photographs, and handouts when known.

## 11. Compile `RUN.md`

The modular adventure files are the maintainable preparation sources. `RUN.md` is the compiled table document.

Once the adventure is ready, send:

```text
Compile the adventure into its `RUN.md`.

Read all adventure source files and follow the compilation requirements in `GM.md`, `templates/adventure/SKELETON.md`, and `templates/adventure/RUN.md`. Do not omit required skeleton blocks.

Put verified NPC statistics, hazards, equipment, modifiers, and short rule reminders directly beside the situations where they matter, in the published stat-block layout. Include precise source-page or section references. Do not invent mechanics or copy long rules passages.

Use ALL-CAPS on first NPC mention. Write Trait tests as `Notice (-2)` with fail, success, and raise when the roll reveals information. Include quoted spoken lines and a GM Note in every situation that has a speaker or a secret.

Organize the document around objectives, story points, flexible situations, escalation, and consequences, not a mandatory scene sequence.

Include a first-15-minutes block (trouble already in motion, not only briefing) and a five-beat dashboard mapped onto story points. Prepare the climax as a situation with opposition, environment, urgency, and a secondary objective.

Define table shorthand once near the top. Include a short mood/paraphrase for the briefing and each story point. Flavor is not a scene script.

Include pacing checkpoints, a 3–4 hour core for a one-shot, optional cuts, failure-forward guidance, essential-information vectors, early-removal mitigation, replacement-character options, GM secrets, quick references, end states, and rewards or a clear stop.

Compile only after QUALITY.md is scored and Coherence (prep) has passed with a logic summary. Finish by running the complete table checklist and report anything that still requires a GM decision.
```

Before play, review the finished `RUN.md` yourself. Confirm that:

- its configuration matches `ADVENTURE.md`;
- `QUALITY.md` is scored and the band allows the intended table;
- Coherence (prep) passed and the logic summary is present;
- inactive sources do not influence the adventure;
- the compile satisfies `templates/adventure/SKELETON.md`;
- relevant statistics and rules are beside their situations, in published stat-block layout, with quoted lines and GM Notes where a speaker or secret exists;
- essential information has multiple discovery vectors;
- failure changes the situation without automatically ending progress;
- the first 15 minutes contain actual trouble;
- a climax situation is prepared (not only a last fight);
- pacing cuts and a 3–4 hour core are identified for a one-shot;
- GM-only information is clearly marked;
- early-removal mitigation and re-entry options exist;
- end states include a complete ending and rewards or a clear stop;
- planned events are not described as though they already happened.

At the table, you should be able to run most of the session from the adventure's own `RUN.md`:

```text
adventures/<adventure-slug>/RUN.md
campaigns/<campaign-slug>/<adventure-slug>/RUN.md
```

There is no campaign-root `RUN.md`. To print the file as an A4 two-column packet:

```text
python3 tools/print-run/render.py adventures/<adventure-slug>/RUN.md --pdf
python3 tools/print-run/render.py campaigns/<campaign-slug>/<adventure-slug>/RUN.md --pdf
```

Keep the SWADE PDF available for unexpected rules questions.

## 12. Record what happened after play

Do not edit `RUN.md` into a historical record. Create a separate dated recap from your notes or transcript. In linked play the recap belongs to the child adventure that was actually played, not to the campaign root.

Use:

```text
The session is finished. Here are my notes:

[Paste your notes or transcript]

Create a dated session recap using `templates/session-recap.md`. Store it in the adventure that was played: the standalone adventure folder, or `campaigns/<campaign-slug>/<adventure-slug>/` for a campaign child. Never in the campaign root.

Clearly separate:

- events that definitely happened;
- uncertain recollections;
- unused or contradicted preparation;
- character changes;
- NPC, faction, and location changes;
- rules rulings;
- unresolved threads;
- facts that are candidates for permanent canon.

Then propose the necessary repository updates, naming the exact destination file for each one. Do not change world canon until I approve the proposed canon changes. Prepared material that never occurred must not be recorded as history.
```

Review the proposed canon changes. When they are correct, use:

```text
I approve the proposed canon and state changes. Apply them to these destinations:

- Linked play: this table's established locations, factions, recurring NPCs, lore, and timeline go in `campaigns/<campaign-slug>/world/`, and party or index changes go in `campaigns/<campaign-slug>/characters/` and `CAMPAIGN.md`.
- Standalone play: keep adventure-local state in that adventure's own files.
- Repository-root `world/`: change it only for facts I deliberately declare setting-wide and shared across tables.
- Rulings go in `rules/rulings.md`; a standing override goes in `rules/house-rules.md` only if I ask for one.

Leave the session recap in the child adventure that was played as the record of what happened. Do not promote unused preparation into canon.
```

## 13. Continue a campaign or short arc

Before preparing the next session, use:

```text
Prepare the next session of this campaign.

First review `GM.md`, the campaign's `CAMPAIGN.md`, the campaign's `world/` canon, the setting-wide root `world/` canon, the relevant child `ADVENTURE.md`, and the latest recap from that child adventure — plus affected NPC and faction states, open threads, and recorded rulings.

Summarize the current state and propose the next session's focus before creating files. Build from what actually happened, not from unused preparation. Preserve the campaign throughline while allowing the players' previous decisions and failures to change circumstances.

The next session is a child adventure folder under `campaigns/<campaign-slug>/` — either a new `<adventure-slug>/` or a continuation of an existing one. Do not compile a campaign-root `RUN.md`.
```

The next session's playable material always lives in a child adventure folder. Continuing an existing child means recompiling that child's `RUN.md` rather than assuming the previous table document is still current. Starting a fresh chapter means creating a new child with the steps in "Add a child adventure to the campaign" (section 2): copy `templates/adventure/` except `SKELETON.md` into `campaigns/<campaign-slug>/<adventure-slug>/`, repeat the campaign's shared configuration in its `ADVENTURE.md`, link the campaign `characters/` sheets instead of copying them, and add the child to the adventure index in `CAMPAIGN.md`.

Create a dated session-preparation file or session directory inside the child adventure when the continuing story needs one.

After play, return to section 12: the recap stays in the child adventure that was played, and campaign state changes only after you approve the reconciliation and its named destinations.

## 14. Recommended first test

Test the framework with one concrete Weird War II one-shot rather than trying to perfect every template in advance.

A useful first cycle is:

1. Start with a one-sentence WWII premise.
2. Let Codex interview you.
3. Create the adventure directory.
4. Develop plot, locations, characters, and challenges in separate passes.
5. Verify rules and historical facts.
6. Compile and run `RUN.md`.
7. Reconcile the session afterward.
8. Note which parts of the framework helped and which felt repetitive.
9. Improve the framework based on actual table use.

The workspace should serve your GMing style. Complexity should emerge from a real adventure, not from filling every available template.
