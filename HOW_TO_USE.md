# How to Use the Savage Worlds GM Authoring Workspace

This workspace is designed to be used as an ongoing Codex project. Each adventure lives inside `adventures/`, while the rest of the repository provides instructions, rules authority, reusable world canon, sources, and templates.

The normal lifecycle is:

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
5. Do not treat preparation as established canon or session history.
6. When generating or substantially revising an adventure, fill and score `QUALITY.md` from `templates/adventure/QUALITY.md` before compiling `RUN.md`.
7. When compiling `RUN.md`, follow `templates/adventure/SKELETON.md`. Do not omit required blocks.
8. Pregen A4 print uses `tools/print-sheets/` (sheet printer, not a generator). Do not put a sheet renderer inside an adventure.
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

## 2. Start an adventure from a premise

Start one Codex task for each adventure. Keeping the adventure in one task makes its design discussion easier to follow, while the files preserve the lasting state.

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

## 3. Configure `ADVENTURE.md`

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

## 4. Activate Weird War II only when needed

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

## 5. Develop the adventure in focused passes

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

## 6. Create or integrate player characters

### Pregenerated PCs

Use:

```text
Create [number] pregenerated player characters for this adventure at the declared Rank. Give each one a reason to accept the mission, a personal stake, useful relationships with other PCs, and an opportunity for spotlight play. Verify every mechanical element against the active rules authority.
```

Review the characters before approving them. Make sure the adventure does not depend on one specific character, Edge, power, or skill.

For table print, use the workspace sheet printer — not a character generator. It lives at [`tools/print-sheets/`](tools/print-sheets/README.md). Put mechanical stats in `characters/<name>.md`, a print extract in `characters/print/chars.json`, then:

```text
python3 tools/print-sheets/render.py adventures/<adventure-name>/characters/print/chars.json
```

Operation Hinterland also keeps a wrapper: `adventures/operation-hinterland/characters/print/build_sheets.py`. Call letters stay with that adventure (`handouts/print/build_letters.py`).

### Player-supplied PCs

Add the character files or summaries to the adventure and use:

```text
Review these player-supplied characters against `ADVENTURE.md`. Check Rank, allowed sources, setting compatibility, historical equipment, mission hooks, powers, Edges, and special abilities. Identify adaptation needs, but do not change the characters without my approval.
```

### Supporting both

When `pc_mode: both`, pregenerated characters can also serve as replacement or reserve characters.

The adventure should avoid random opening situations likely to remove a player from most of the session. Later lethal consequences are acceptable once the players have participated meaningfully and the danger has been communicated.

Prepare a re-entry option:

```text
Review the adventure for early character removal. Prepare a fictionally appropriate reserve PC, replacement entry point, or temporary allied character so a player can return promptly if removal still occurs.
```

## 7. Verify Savage Worlds mechanics

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

## 8. Verify historical material

If the adventure declares `cinematic`, `researched`, or `strict` historical accuracy, add relevant maps, books, articles, images, and texts under:

```text
sources/background/
```

or:

```text
adventures/<adventure-name>/sources/
```

Then use:

```text
Review the historical claims in this adventure according to its declared accuracy level. Check dates, geography, units, ranks, equipment, weather, terminology, and political conditions against the listed background sources.

Separate verified fact, plausible inference, intentional alteration, and unresolved uncertainty. Do not allow historical flavor sources to overrule Savage Worlds mechanics.
```

Record provenance and usage rights for maps, photographs, and handouts when known.

## 9. Compile `RUN.md`

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

At the table, you should be able to run most of the session from:

```text
adventures/<adventure-name>/RUN.md
```

Keep the SWADE PDF available for unexpected rules questions.

## 10. Record what happened after play

Do not edit `RUN.md` into a historical record. Create a separate dated recap from your notes or transcript.

Use:

```text
The session is finished. Here are my notes:

[Paste your notes or transcript]

Create a dated session recap using `templates/session-recap.md`.

Clearly separate:

- events that definitely happened;
- uncertain recollections;
- unused or contradicted preparation;
- character changes;
- NPC, faction, and location changes;
- rules rulings;
- unresolved threads;
- facts that are candidates for permanent canon.

Then propose the necessary repository updates. Do not change world canon until I approve the proposed canon changes. Prepared material that never occurred must not be recorded as history.
```

Review the proposed canon changes. When they are correct, use:

```text
I approve the proposed canon and state changes. Update the affected world, NPC, faction, location, timeline, ruling, and active-thread files. Preserve the session recap as the record of what happened. Do not promote unused preparation into canon.
```

## 11. Continue a campaign or short arc

Before preparing the next session, use:

```text
Prepare the next session of this adventure or campaign.

First review `GM.md`, `ADVENTURE.md`, established world canon, the latest session recap, affected NPC and faction states, open threads, and recorded rulings.

Summarize the current state and propose the next session's focus before creating files. Build from what actually happened, not from unused preparation. Preserve the main throughline while allowing the players' previous decisions and failures to change circumstances.
```

Create a new dated session-preparation file or session directory when the continuing adventure needs it. Recompile `RUN.md` for the upcoming session rather than assuming the previous table document remains current.

## 12. Recommended first test

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
