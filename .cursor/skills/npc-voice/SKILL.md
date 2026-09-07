---
name: npc-voice
description: Writes and repairs NPC Portrayal and situation spoken lines for Savage Worlds adventures in this workspace so speakers sound like people with limited knowledge, not plot devices. Use when drafting or revising NPC dialogue, Portrayal, RUN.md Spoken lines, extra shouts, quest-kiosk speech, or rewriting NPC voice.
---

# NPC Voice

Implements `GM.md` people/speech policy. Does not replace `GM.md`. Does not design plot, write Mood (table), write player handouts/letters, fill stat blocks, or promote NPCs into the repository-root `world/npcs/` unless the GM asks. Pregen PCs are not NPCs.

Destination rules, used the same way in the write path, the named-vs-extra table, and File mapping:

- a named NPC file that already exists (anywhere except pregen sheets): edit that Portrayal in place;
- a named NPC who should persist for this campaign: `campaigns/<campaign-slug>/world/npcs/<name>.md`;
- otherwise: `<adventure>/npcs/<name>.md`, whether that adventure is standalone or a child of a campaign;
- never player sheets, and never the repository-root `world/npcs/` unless the GM asks.

An adventure-local named NPC is fine inside a campaign child. Only promote to campaign `world/npcs/` when the person is meant to recur beyond this night.

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
3. Named NPC: apply the destination rules above. If a named NPC file already exists (wherever it is — except pregen sheets, which are not Portrayal targets), edit that Portrayal in place. Otherwise create the file from `templates/npc.md`: `campaigns/<campaign-slug>/world/npcs/<name>.md` when this person should persist for the campaign, else `<adventure>/npcs/<name>.md` — the same for a standalone adventure and a campaign child. Do not put NPC Portrayal in `characters/` or player sheets (`characters/` is pregenerated PCs). Do not promote to the repository-root `world/npcs/` unless the GM asks. Fill Portrayal (first impression, voice/manner, 1–3 core lines, avoid, four pressure variants). Leave Mechanics empty or untouched — do not invent stats. If a line would imply a Trait test, read `rules/RULES.md`; still do not write the roll in this skill.
4. Write beat-specific `Spoken lines` into the situation (see File mapping). One named person in several beats: Portrayal stays in the NPC file; each beat gets only the line that belongs there. Do not paste the pressure table into every story point.
5. Named only — pressure variants, one short line or action-plus-line each, same person: Cooperate, Refuse, Threatened, Ignored. Ignored must match **If ignored** on the NPC file.
6. Self-check: would this person say this if the plot did not need it? If not, rewrite or omit.

### Named vs extra

| Speaker | Portrayal | Situation | Pressure variants |
|---|---|---|---|
| Named NPC | Full Portrayal in their own NPC file — the existing one, else campaign `world/npcs/` for a persisting person, else `<adventure>/npcs/` | Beat-specific line(s) | Four labeled lines in the NPC file |
| Unnamed extra | One voice cue in the situation only; no new file | One shout | None |

Do not create one NPC file per extra shout.

## Repair path

Walk quotes in Portrayal and in the relevant situations. Rewrite in place if the line fails the rubric. Leave lines that already pass. Add the four pressure slots only on **Write**, when the GM asked for pressure variants, or when Portrayal has no first impression and no core spoken lines. Missing pressure slots alone do not count as incomplete Portrayal on Repair. Do not add them while repairing a passing named speaker.

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
| Named Portrayal + pressure variants | Existing named NPC file if one exists (not pregen sheets in `characters/`); otherwise `campaigns/<campaign-slug>/world/npcs/<name>.md` if the person should persist for this campaign, else `<adventure>/npcs/<name>.md` — standalone or campaign child — from `templates/npc.md`. Never `characters/` or player sheets. Never the repository-root `world/npcs/` unless the GM asks. |
| Situation `Spoken lines` | That situation in `RUN.md` if the block exists; otherwise the pre-compile situation draft (`plot.md` / location notes) using the field name `Spoken lines` |
| Extra voice cue + shout | Situation only |

Edit files in place. Do not leave the only copy in chat. Do not add `voices.md`.

Never write Mood (table). Never write `handouts/` letters.

## Skeleton note

`templates/adventure/SKELETON.md` requires `Spoken lines` when a named NPC, victim, messenger, or opposition can talk or shout. This skill fills that field. It does not change the skeleton.
