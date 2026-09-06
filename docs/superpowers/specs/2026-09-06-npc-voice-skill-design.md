# NPC Voice Skill - Approved Design

## Purpose

Give adventure-authoring agents a write path and a repair path for **NPC Portrayal** and **situation spoken lines**, so speakers act and talk as people with limited knowledge rather than as plot devices.

This skill implements the speech policy already in `GM.md`. It does not replace `GM.md`.

## Decision

**Workflow skill (not a thin restatement, not new quality gates).** One skill named `npc-voice` with two paths:

- **Write** — fill Portrayal and situation lines for a speaker who is new or empty.
- **Repair** — rewrite existing quotes that fail the speech policy; leave lines that already sound human.

Install at `.cursor/skills/npc-voice/`. No sidecar `voices.md`, no scripts, no `QUALITY.md` changes (missing quoted lines are already a compile/quality concern).

## Scope

**In scope**

- Named NPC Portrayal in adventure NPC/character files shaped like `templates/npc.md`.
- Situation `Spoken lines` for that beat.
- Unnamed extras who can talk or shout in a situation: one voice cue plus one shout.
- Pressure variants for **named NPCs only**: Cooperate, Refuse, Threatened, Ignored.

**Out of scope**

- Player handouts, call letters, and other in-world documents the players hold.
- Mood (table) (Climate / See / Hear / Feel).
- Stat blocks, Edges, Trait tests, and other mechanics (read `rules/RULES.md` only if a drafted line would imply a roll; do not invent statistics).
- Plot design, clue placement, and adventure structure.
- Full conversational scripts or ask-banks keyed to every likely player question.
- Promoting adventure NPCs into `world/npcs/` unless the GM asks.
- Pregenerated PC voice (PCs are not NPCs).

## Architecture

```text
GM.md (policy)
ADVENTURE.md (setting, sides, period, declared language)
situation draft + existing NPC file
        |
        v
npc-voice skill (write | repair)
        |
        +-- named: Portrayal + pressure variants --> adventure NPC file
        +-- named and extras: Spoken lines ---------> situation in RUN.md
                                                    (or plot/location draft
                                                     if RUN.md is not compiled yet)
```

Quoted lines in `RUN.md` remain table cues, not a script, as `GM.md` already states.

## Required inputs

Before writing or repairing any line, the agent must read:

1. `GM.md` section on people, speech, and behavior.
2. The adventure’s `ADVENTURE.md` (who the sides are, period, setting, what is secret vs public).
3. The situation being authored (who is present, what just happened, what this person can perceive).
4. The existing NPC file if the speaker is named.

If adventure context is missing, stop and ask. Do not invent a setting-generic watchman.

Unnamed extras do not get a biography. Derive role, knowledge, fear, and language from the situation only.

## Write path

1. Lock **this moment**: current objective, fear, leverage, what they have seen or been told, relationship to the PCs, which language(s) they would actually use here.
2. If they would stay silent: when the skeleton does **not** require the field, omit it or write `Spoken lines: none`. When a named speaker is present and the field is required, write a non-speech cue (they move, glare, keep working) rather than a fake line. Do not invent dialogue to satisfy a blank.
3. Named NPC: create `templates/npc.md` from the template if no file exists yet; fill Portrayal (first impression, voice/manner cue, 1–3 core spoken lines, avoid-list). Leave Mechanics empty or untouched; this skill does not fill stats.
4. Write situation `Spoken lines` into the beat under edit.
5. Named only: add four short pressure variants (Cooperate, Refuse, Threatened, Ignored). Ignored must match the NPC template’s “If ignored” (off-stage action or later pressure), not a speech to empty air unless they would shout anyway.
6. Self-check: would this person say this if the plot did not need it? If not, rewrite or omit.

### Named vs extra output

| Speaker | Portrayal | Situation | Pressure variants |
|---|---|---|---|
| Named NPC | Full Portrayal in their adventure NPC file | Beat-specific line(s) | Four labeled lines |
| Unnamed extra | One voice cue in the situation only; no new file | One shout | None |

Do not create one NPC file per extra shout.

### Where to write situation lines

- If `RUN.md` already has that situation block, edit its `Spoken lines` in place.
- If the adventure is still pre-compile, write the same field on the situation draft that will compile (`plot.md` / location notes using the skeleton name `Spoken lines`).
- After a compile, do not leave the only copy of new lines in chat. The skill edits files.

If a named person appears in several situations, Portrayal stays in the NPC file; each situation gets only the line that belongs to that beat. Do not paste the full pressure table into every story point.

## Repair path

Walk quoted lines in the NPC Portrayal and in the relevant situations. Rewrite in place when a line:

- Gives the speaker knowledge they were not in a position to have (including adventure secrets).
- Briefs the party or summarizes the situation for the players’ benefit.
- Is a slogan, “as you know,” or narrator voice.
- Exists only to hand the next story point.
- Matches another speaker’s register so everyone sounds like the same GM.
- Gives an unnamed extra a unique life story.

Leave lines that are already short, specific, in register, and limited to what that person knows. Do not add pressure variants onto a named NPC whose existing lines already pass, unless Portrayal is incomplete.

## Language

GM-facing files stay **English** (workspace default), regardless of player-handout language.

Other languages appear **only when that person would use them in this beat**, derived from `ADVENTURE.md` and the speaker (German watch shouting a halt; an Italian who works in English dropping Italian under stress). Not a blanket rule that all extras of a nationality get flavor words.

When a quoted line is not in English, put the **English meaning on the same line** (or immediately beside it) so the GM is never guessing.

Example shape: `“Halt! Wer da?” (Halt! Who goes there?)`

## Repair rubric (pass / fail)

A line **fails** (must rewrite) if any of: secret they cannot know; briefing kiosk; shared narrator voice; slogan / “as you know”; plot-only function; extra with a unique backstory in the shout.

A line **passes** if it is short, specific, in that person’s register, limited to their knowledge, and omitted when they would not talk.

## Skill package

```text
.cursor/skills/npc-voice/
  SKILL.md      # triggers, inputs, write path, repair path, file mapping, language, omit rule
  EXAMPLES.md   # good vs bad pairs in this workspace’s style; invented, not copyrighted flavor
```

`SKILL.md` description (agent trigger): third person; states that the skill writes and repairs NPC Portrayal and situation spoken lines; use when the user asks for NPC dialogue, Portrayal, spoken lines, quest-kiosk speech, or rewriting NPC voice.

`EXAMPLES.md` must include at least: briefing kiosk vs person; German extra shout with gloss; named NPC with four pressure variants; extra who should stay silent; English-working foreign NPC who code-switches only under a fitting pressure.

## Constraints from existing contracts

- `templates/npc.md` Portrayal remains the named-NPC shape.
- `templates/adventure/SKELETON.md` still requires `Spoken lines` when a named NPC, victim, messenger, or opposition can talk or shout. This skill fills that field; it does not change the skeleton.
- Do not put secrets in Mood. This skill never writes Mood.
- Do not reproduce long copyrighted rules or published adventure text in examples.

## Testing (manual, after implementation)

1. Write path: one named NPC and one unnamed extra in an existing adventure draft; files updated in place.
2. Repair path: plant a kiosk/briefing line; skill rewrites it and leaves a good neighboring line.
3. Mood and handouts/letters unchanged.
4. German extra: diegetic German plus English gloss.
5. Foreign NPC who operates in English: Italian (or similar) only when that beat justifies it, not on every line.
6. Silent extra: `none` / omit, no invented shout.

## Non-goals (YAGNI)

- `voices.md` sidecar.
- New `QUALITY.md` rows or a voices linter.
- Handout/letter branch.
- Ask-bank of answers to likely player questions.
- World-canon NPC promotion.
- Changing `GM.md` policy (the skill obeys it; it does not rewrite it).
