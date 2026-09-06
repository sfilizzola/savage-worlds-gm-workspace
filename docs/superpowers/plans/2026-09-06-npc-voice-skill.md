# NPC Voice Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a project skill `npc-voice` that writes and repairs NPC Portrayal and situation spoken lines in adventure files, following `GM.md` speech policy.

**Architecture:** Instruction-only Cursor skill at `.cursor/skills/npc-voice/` (`SKILL.md` workflows + `EXAMPLES.md` good/bad pairs). Named-NPC pressure variants land under Portrayal in `templates/npc.md`. Agents edit adventure NPC files and `RUN.md` (or pre-compile situation drafts) in place. No scripts, no `voices.md`, no `QUALITY.md` or `GM.md` edits.

**Tech Stack:** Cursor project skills (YAML frontmatter + markdown). Adventure files already use `templates/npc.md` and `templates/adventure/SKELETON.md`.

**Spec:** `docs/superpowers/specs/2026-09-06-npc-voice-skill-design.md`

---

## File map

| File | Responsibility |
|---|---|
| `.cursor/skills/npc-voice/SKILL.md` | Triggers, required reads, write path, repair path, file mapping, language, omit/silent rule, out of scope |
| `.cursor/skills/npc-voice/EXAMPLES.md` | Invented good/bad pairs (not published adventure text) |
| `templates/npc.md` | Add Portrayal slots for the four named-NPC pressure variants |

Do not create: `voices.md`, linters, `QUALITY.md` changes, `GM.md` changes, handout/letter workflows.

---

### Task 1: Extend named-NPC template for pressure variants

**Files:**
- Modify: `templates/npc.md`

- [ ] **Step 1: Confirm current Portrayal block**

Read `templates/npc.md`. The Portrayal section today ends at `Avoid:` then `## Mechanics`.

- [ ] **Step 2: Add pressure-variant fields under Portrayal**

Replace the Portrayal section with:

```markdown
## Portrayal

Write as a person with limited knowledge, a current objective, and a fear. Lines they would actually say in this moment. Not exposition, not a briefing, not the narrator's voice.

- First impression:
- Voice/manner cue:
- Spoken lines: one to three quoted lines the GM can use at the table.
- Avoid:
- Pressure variants (one short line or action-plus-line each; same person, not a second personality):
  - Cooperate:
  - Refuse:
  - Threatened:
  - Ignored: must match **If ignored** above; not a speech to empty air unless they would shout anyway
```

Leave the header fields and `## Mechanics` unchanged.

- [ ] **Step 3: Check the template still matches the skill contract**

Confirm `templates/npc.md` still has: Canon status, Current objective, Fear, If ignored, Portrayal spoken lines, Mechanics. Confirm it does **not** mention Mood, handouts, or stats invented by the voice skill.

- [ ] **Step 4: Commit**

```bash
git add templates/npc.md
git commit -m "$(cat <<'EOF'
Add named-NPC pressure variant slots to the portrayal template.

EOF
)"
```

---

### Task 2: Write `SKILL.md`

**Files:**
- Create: `.cursor/skills/npc-voice/SKILL.md`

- [ ] **Step 1: Confirm the skill directory is empty**

```bash
ls -la .cursor/skills/npc-voice 2>&1 || true
```

Expected: directory missing, or empty. Do not put this skill in `~/.cursor/skills-cursor/`.

- [ ] **Step 2: Create SKILL.md with this exact body**

Omit `disable-model-invocation` so the agent can pick the skill from ambient requests (NPC dialogue, Portrayal, spoken lines, quest-kiosk speech).

```markdown
---
name: npc-voice
description: Writes and repairs NPC Portrayal and situation spoken lines for Savage Worlds adventures in this workspace so speakers sound like people with limited knowledge, not plot devices. Use when drafting or revising NPC dialogue, Portrayal, RUN.md Spoken lines, extra shouts, quest-kiosk speech, or rewriting NPC voice.
---

# NPC Voice

Implements `GM.md` people/speech policy. Does not replace `GM.md`. Does not design plot, write Mood (table), write player handouts/letters, fill stat blocks, or promote NPCs into `world/npcs/` unless the GM asks. Pregen PCs are not NPCs.

Quoted lines are table cues, not a script.

For good/bad pairs see [EXAMPLES.md](EXAMPLES.md).

## Required reads (before any line)

1. `GM.md` — people, speech, and behavior.
2. The adventure's `ADVENTURE.md` — sides, period, setting, secrets vs public facts.
3. The situation under edit — who is present, what just happened, what this person can perceive.
4. The named NPC file if it exists.

If adventure context is missing, stop and ask. Do not invent a generic watchman.

Unnamed extras get no biography. Derive role, knowledge, fear, and language from the situation only.

## Choose a path

- **Write** — speaker is new, Portrayal is empty, or `Spoken lines` is missing/empty.
- **Repair** — quoted lines exist; check them against the rubric and rewrite only failures.

## Write path

1. Lock this moment: current objective, fear, leverage, what they have seen or been told, relationship to the PCs, which language(s) they would actually use here.
2. Silence: if they would not talk and the skeleton does not require the field, omit or write `Spoken lines: none`. If a named speaker is present and the field is required, write a non-speech cue (they move, glare, keep working). Do not invent dialogue to fill a blank.
3. Named NPC: if no file exists, copy `templates/npc.md` into the adventure (not `world/npcs/` unless asked). Fill Portrayal (first impression, voice/manner, 1–3 core lines, avoid, four pressure variants). Leave Mechanics empty or untouched — do not invent stats. If a line would imply a Trait test, read `rules/RULES.md`; still do not write the roll in this skill.
4. Write beat-specific `Spoken lines` into the situation (see File mapping). One named person in several beats: Portrayal stays in the NPC file; each beat gets only the line that belongs there. Do not paste the pressure table into every story point.
5. Named only — pressure variants, one short line or action-plus-line each, same person: Cooperate, Refuse, Threatened, Ignored. Ignored must match **If ignored** on the NPC file.
6. Self-check: would this person say this if the plot did not need it? If not, rewrite or omit.

### Named vs extra

| Speaker | Portrayal | Situation | Pressure variants |
|---|---|---|---|
| Named NPC | Full Portrayal in their adventure NPC file | Beat-specific line(s) | Four labeled lines in the NPC file |
| Unnamed extra | One voice cue in the situation only; no new file | One shout | None |

Do not create one NPC file per extra shout.

## Repair path

Walk quotes in Portrayal and in the relevant situations. Rewrite in place if the line fails the rubric. Leave lines that already pass. Do not add pressure variants when existing named lines already pass, unless Portrayal is incomplete.

### Rubric — fail (must rewrite)

- Knowledge they were not in a position to have, including adventure secrets
- Briefs the party or summarizes the situation for the players
- Slogan, "as you know," or narrator voice
- Exists only to hand the next story point
- Same register as another speaker so everyone sounds like the GM
- Unnamed extra given a unique life story in the shout

### Rubric — pass (leave)

Short, specific, in that person's register, limited to their knowledge, omitted when they would not talk.

## Language

GM-facing files stay English (workspace default), including when player handouts are another language.

Other languages only when **this person, in this beat, would use them** — from `ADVENTURE.md` and the speaker, not a blanket nationality garnish. A German watch may shout a halt in German. An Italian who works in English may drop Italian under stress, not on every line.

Non-English quotes need the English meaning on the same line (or immediately beside): `"Halt! Wer da?" (Halt! Who goes there?)`

## File mapping

| What | Where |
|---|---|
| Named Portrayal + pressure variants | Adventure NPC/character file (`templates/npc.md` shape) |
| Situation `Spoken lines` | That situation in `RUN.md` if the block exists; otherwise the pre-compile situation draft (`plot.md` / location notes) using the field name `Spoken lines` |
| Extra voice cue + shout | Situation only |

Edit files in place. Do not leave the only copy in chat. Do not add `voices.md`.

Never write Mood (table). Never write `handouts/` letters.

## Skeleton note

`templates/adventure/SKELETON.md` requires `Spoken lines` when a named NPC, victim, messenger, or opposition can talk or shout. This skill fills that field. It does not change the skeleton.
```

- [ ] **Step 3: Verify frontmatter and out-of-scope guards**

```bash
test -f .cursor/skills/npc-voice/SKILL.md
grep -q '^name: npc-voice$' .cursor/skills/npc-voice/SKILL.md
grep -q 'quest-kiosk' .cursor/skills/npc-voice/SKILL.md
grep -q 'Never write Mood' .cursor/skills/npc-voice/SKILL.md
grep -q 'handouts/' .cursor/skills/npc-voice/SKILL.md
grep -q 'EXAMPLES.md' .cursor/skills/npc-voice/SKILL.md
```

Expected: all commands succeed (`exit 0`). `name` is lowercase hyphenated. Description includes write/repair and trigger phrases.

- [ ] **Step 4: Commit**

```bash
git add .cursor/skills/npc-voice/SKILL.md
git commit -m "$(cat <<'EOF'
Add npc-voice skill workflows for portrayal and spoken lines.

EOF
)"
```

---

### Task 3: Write `EXAMPLES.md`

**Files:**
- Create: `.cursor/skills/npc-voice/EXAMPLES.md`

- [ ] **Step 1: Create EXAMPLES.md with these invented pairs**

Do not paste Operation Hinterland, published adventures, or long rules text. These names are disposable.

```markdown
# NPC Voice examples

Invented speakers. Not canon. Not published flavor text.

## 1. Briefing kiosk vs person

**Fail (repair):** a clerk who has not been told the mission.

> "The three radio heads are in the loft, the old post, and the Feldwebel's satchel. Cut two and you win. The Rathaus is a decoy."

**Pass:** same clerk, same moment (they want to close the window and go back to sleep).

> "Board isn't here. They moved it. East rooms. I file paper. I don't run the net."

## 2. German extra shout with gloss

Situation: wet east-face watch, night, PCs approaching a stove post. Extra is a tired Landser, not a named officer.

**Fail:** English slogan, unique backstory.

> "Halt, friends of democracy! I, Johann from Stuttgart, hate this war and will show you the postern if you spare my sister."

**Pass:** one voice cue, one shout, diegetic German, English meaning.

> Voice: hoarse, close, wants the password and the stove. `"Halt! Wer da?" (Halt! Who goes there?)` If they keep coming: `"Papiere. Schnell." (Papers. Quick.)`

No NPC file for this extra.

## 3. Named NPC pressure variants

**FW. Marta Reis** — extra who becomes a named speaker at the books. Objective: keep the satchel on her route. Fear: being the one who lost the books. Knows the books move with her; does not know the PCs' mission.

Portrayal spoken lines (core):

> "The books stay with me."

Pressure variants (NPC file only — do not dump all four into every situation):

- Cooperate: "You want a look. Here. Then they go back in the bag."
- Refuse: "No. This is not your post."
- Threatened: she does not speechify; she moves. If she speaks: "Shoot and you still don't get a clerk who can read them."
- Ignored: she leaves on her round toward a gate or the board (matches **If ignored**). No speech to empty air.

Situation line for the beat where they meet her: `"The books stay with me."` If she runs: action, not a speech.

## 4. Extra who should stay silent

Situation: loft, operator hunched on a live board, PCs have not shown themselves. He would keep working.

**Fail:** invented shout to fill the field.

> "Don't cut that or the whole hydra dies, heroes!"

**Pass:** they can talk, but in this beat he would not. Required named/opposition field: non-speech cue.

> Spoken lines: he does not look up. Hands stay on the cords. If they come in loud, then: `"Board's live — don't cut that."`

If nobody has revealed themselves and the skeleton does not require a speaker: `Spoken lines: none`.

## 5. English-working foreign NPC — code-switch only when it fits

**Sgt. Luca Bianchi** — Allied NCO who briefs and works in English. Italian is home speech, not a tourist layer.

**Fail (every line garnished):**

> "Allora, the aerial is north, capisce? We jump at green light, amico."

**Pass (English in the job):**

> "Green light. Go."

**Pass (Italian under stress, glossed):** he is hit, or he is talking to another Italian when he thinks the PCs are not the audience.

> `"Madonna, non ora—" (God, not now—)` then back to English if he is still giving orders: "Move. Leave the set."
```

- [ ] **Step 2: Confirm all five required pairs exist**

```bash
grep -c '^## ' .cursor/skills/npc-voice/EXAMPLES.md
grep -q 'Briefing kiosk' .cursor/skills/npc-voice/EXAMPLES.md
grep -q 'German extra' .cursor/skills/npc-voice/EXAMPLES.md
grep -q 'pressure variants' .cursor/skills/npc-voice/EXAMPLES.md
grep -q 'should stay silent' .cursor/skills/npc-voice/EXAMPLES.md
grep -q 'code-switch' .cursor/skills/npc-voice/EXAMPLES.md
```

Expected: first command prints `5`. Remaining greps succeed. File must not contain `operation-hinterland`, `Ward`, or long SWADE page quotes.

- [ ] **Step 3: Commit**

```bash
git add .cursor/skills/npc-voice/EXAMPLES.md
git commit -m "$(cat <<'EOF'
Add npc-voice good/bad examples for write and repair.

EOF
)"
```

---

### Task 4: Spec coverage check and dry-run (no adventure commit)

**Files:**
- Read: `docs/superpowers/specs/2026-09-06-npc-voice-skill-design.md`
- Read: `.cursor/skills/npc-voice/SKILL.md`
- Read: `.cursor/skills/npc-voice/EXAMPLES.md`
- Read: `templates/npc.md`

Do not commit Operation Hinterland or any real adventure. If you plant a kiosk line for a dry-run, revert it.

- [ ] **Step 1: Tick spec requirements against files**

From the spec, each item must be true:

| Spec item | Where it lives |
|---|---|
| Write + repair paths | `SKILL.md` Choose a path / Write path / Repair path |
| Named Portrayal + extras one shout | `SKILL.md` Named vs extra |
| Pressure variants named only | `SKILL.md` + `templates/npc.md` |
| English + diegetic gloss | `SKILL.md` Language |
| In-place NPC file + `RUN.md` / pre-compile draft | `SKILL.md` File mapping |
| No `voices.md`, Mood, handouts, stats, world promotion | `SKILL.md` header + File mapping |
| Five example types | `EXAMPLES.md` sections 1–5 |
| Skeleton unchanged | skill fills `Spoken lines`; do not edit `templates/adventure/SKELETON.md` |
| `GM.md` / `QUALITY.md` unchanged | `git diff -- GM.md templates/adventure/QUALITY.md` empty |

```bash
git diff -- GM.md templates/adventure/QUALITY.md templates/adventure/SKELETON.md
```

Expected: no diff. If any spec row is missing, fix the skill files and amend only if the previous commit is yours, unpushed, and the user asked; otherwise make a new commit.

- [ ] **Step 2: Dry-run write (discard)**

In a throwaway buffer (do not save over a real adventure), take one named speaker and one unnamed extra from `EXAMPLES.md` and produce: NPC Portrayal block including four pressure variants; situation `Spoken lines`; extra voice cue + glossed shout. Check the self-check question. Discard the buffer.

- [ ] **Step 3: Dry-run repair (discard)**

Take example 1 Fail line. Apply the repair rubric. Result must match the shape of example 1 Pass (limited knowledge, not a hydra briefing). Confirm a neighboring Pass line would be left alone.

- [ ] **Step 4: Dry-run silence and code-switch (discard)**

Example 4: no invented shout. Example 5: English on the job; Italian only under stress with gloss.

- [ ] **Step 5: Final commit only if Step 1 required file fixes**

If Step 1 found gaps, commit the fixes:

```bash
git add .cursor/skills/npc-voice/SKILL.md .cursor/skills/npc-voice/EXAMPLES.md templates/npc.md
git commit -m "$(cat <<'EOF'
Close npc-voice skill gaps found in the spec coverage check.

EOF
)"
```

If nothing changed, do not create an empty commit.

---

## Self-review (plan vs spec)

- Write path, repair path, named vs extra, pressure variants, language/gloss, file mapping, silence/non-speech cue, no Mood/handouts/stats/world promotion: Task 2 `SKILL.md`.
- Template slot for variants: Task 1.
- Required example pairs: Task 3.
- Manual tests 1–6 from the spec: Task 4 dry-runs (write named+extra, repair kiosk, Mood/handouts not in skill output, German gloss, code-switch, silent extra). Real adventure files are not modified in this plan.
- Non-goals respected: no `voices.md` task, no QUALITY/linter, no letter branch, no `GM.md` rewrite.
