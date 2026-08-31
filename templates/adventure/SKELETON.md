# RUN.md writing contract

Do not copy this file into an adventure directory. Follow it when generating or compiling `adventures/<slug>/RUN.md`.

Modular sources remain authoritative. `RUN.md` is the table document. Story points are reachable situations, not a visit order. Flavor must not overrule predetermined truths or rules authority.

A compile that omits a required block is incomplete. Fill the block or delete the situation; do not leave a heading with no payload.

## Document order

1. Runtime header
2. Table terms
3. Notation
4. Opening mood (GM throughline; not spoken as the landing)
5. First 15 minutes
6. Mission in 30 seconds
7. Current situation
8. Pacing dashboard and five-beat dashboard
9. Climax situation
10. Story points (copy as needed)
11. Escalation and clocks
12. Failure-forward reference
13. PC spotlight and safety
14. NPC quick reference
15. Rules quick reference
16. Handouts index (omit the section if there are no handouts)
17. GM secrets
18. End states
19. Table checklist
20. After play note

## Notation

State these rules once under **Notation**. Use them throughout the file.

| Rule | Table form |
|---|---|
| First appearance of an NPC or named creature | **ALL-CAPS** on first mention in that situation; normal title case after |
| Trait test | `` `Notice (-2)` ``, `` `Persuasion` ``, `` `Survival (+1)` `` — Trait name, optional modifier, no invented skill names |
| Information rolls | Always state fail, success, and raise when the roll reveals information |
| Quoted speech | Quotation marks for lines the GM can speak. Not a read-aloud script. Omit the field if nobody speaks |
| Mood | Four labeled lines the GM paraphrases to the table **now**: **Climate**, **See**, **Hear**, **Feel**. Player-perceivable only. Not a boxed read-aloud. No secrets, unearned names, historical footnotes, or GM editorials |
| GM Note | Labeled **GM Note.** Secret or ruling. Never player-facing |
| Optional material | Label **Optional.** Side paths must not gate the main objective |
| PC-specific hook | Label **PC hook — Name.** Must not be the only vector for essential information |
| Wild Card / Extra | Label every stat block. A named Extra promoted to Wild Card uses the Extra profile and rolls a Wild Die |
| Handouts | Reference inline (`Handout A`) and list them in the Handouts index |

**Opening mood** (document section 4) is a GM throughline of the night: briefing calm → trouble. It may mention facts the players do not know yet. Do not speak it as the landing.

**Story-point Mood** is what you paraphrase to the table when that situation is on. Compile it from the location's **First impression**.

## Situation block

Use this order inside every story point and every nested location. Delete a row only when it cannot apply (for example, no one speaks).

```text
## Story Point N - <Name>

**Mood (table):** Paraphrase to the players the moment this situation is on. Not a read-aloud. Not a required recitation.

- **Climate:** weather, light, cold/heat. What the body notices first.
- **See:** what is in front of them before any roll. No unearned place-names.
- **Hear:** sound, and smell if it matters. One or two cues.
- **Feel:** temperature of the night — calm, thin, urgent, or hunt. One clause. Do not prescribe what the PCs decide.

Do not put in Mood: secrets, tells meant to be rolled, historical footnotes, “this is not the X,” map lectures, NPC locations they cannot see, or GM editorials.

- **Goal:** what this point enables; not a required method.
- **Situation now:** people, forces, and pressure present when they arrive.
- **Spoken lines:** one to four quoted lines. Attribute the speaker. Write what that person would actually say with what they know and want; not exposition or a briefing for the players. Omit if they would stay silent.
- **Discoverable:**
  | Trait | Fail | Success | Raise |
  |---|---|---|---|
  | `Notice (-2)` | | | |
- **GM Note:** secret truth for this situation. If there is no secret, write "None."
- **Pressure/escalation:** what changes if they hesitate, leave, or make noise.
- **Essential information and vectors:** at least two independent channels for anything the main plot needs.
- **Failure changes:** cost, position, time, relationship, or danger. Play continues.
- **Reachable next points:** not a mandatory next scene.
- **Optional / PC hook:** omit if none.

### <Location or immediate situation>

- Sensory frame: same four lines as Mood if this is a **different** door or room. If it is the same space as the story-point Mood, write `as story-point Mood`.
- People and forces:
- Environment/hazards:
- Spoken lines:
- Discoverable: (Trait / fail / success / raise — same table shape)
- GM Note:
- Changes if delayed:

#### At-hand statistics

One published-layout block per Wild Card or Extra profile that can matter here. Duplicate from character files rather than sending the GM elsewhere.

#### At-hand rules

Recurring or easy-to-miss procedure for this situation. Short paraphrase plus authority. Box environment rules that will be used more than once (travel, weather, drowning, thin air, darkness).
```

### When a field is required

| Field | Required when |
|---|---|
| Mood (table) | Every story point. Four labeled lines: Climate, See, Hear, Feel. Player-perceivable only |
| Spoken lines | A named NPC, victim, messenger, or opposition can talk or shout |
| Discoverable table | Players can learn a fact, track, or tell here |
| GM Note | A secret, false assumption, or off-stage cause exists |
| At-hand statistics | A fight, chase, social contest, or named Wild Card/Extra is plausible |
| At-hand rules | A modifier, subsystem, or hazard will be rolled here |
| Boxed environment | The same travel, weather, or setting penalty recurs |

If a named NPC, secret, or likely fight is present and the matching field is empty, the compile fails.

## Stat block layout

```text
**NAME** — Wild Card | Extra
Attributes: Agility dX, Smarts dX, Spirit dX, Strength dX, Vigor dX
Skills: listed skills only
Pace: N; Parry: N; Toughness: N (armor)
Hindrances: only those that matter at the table
Edges: only those that matter at the table
Gear: weapons with Range, Damage, RoF, AP as needed
Special Abilities:
- Ability: one-line effect already applied to derived stats where relevant
Personality: one or two lines, or omit
Authority: SWADE p.X / active setting / house-rule ID
```

Group identical Extras as `Ute Warriors (6):` then one profile.

If a Wild Card uses an Extra profile: `Chipeta — Wild Card; same profile as warriors below; rolls a Wild Die.`

Do not invent Traits, Edges, or derived stats. If authority cannot be established, write `RULE UNCLEAR - GM DECISION REQUIRED`.

## Opening and climax

**First 15 minutes** must include trouble already in motion, not only a map or briefing. Put the first decision and the first at-hand stats in that block when the opening can become a test or a fight.

**Climax situation** must list location, opposition (Wild Cards / Extras), environment, urgency, and a secondary objective besides defeating everyone. Include spoken lines, at-hand stats, and at-hand rules in the climax block or in the story point that delivers it. Do not script the outcome.

## Handouts, pregens, re-entry

- Reference each handout at the situation that uses it.
- Pregen spotlight hooks belong under PC spotlight and safety, not as the only path through a story point.
- Name the spare / re-entry character in PC spotlight and safety.

## Compile gate

Refuse to call `RUN.md` complete unless all of the following are true:

- [ ] Document order above is present (omit Handouts index only when there are no handouts).
- [ ] Notation section is filled and followed.
- [ ] Every story point uses the situation-block order.
- [ ] Every story point has a **Mood (table)** with Climate / See / Hear / Feel; no secrets in Mood.
- [ ] Every information roll states fail, success, and raise.
- [ ] Every situation with a speaker has quoted lines.
- [ ] Every situation with a secret has a GM Note.
- [ ] Every plausible fight or named Wild Card/Extra has an at-hand stat block in published layout.
- [ ] Failure changes play; it does not stop the main plot by itself.
- [ ] Story points are not written as a mandatory sequence.
- [ ] `QUALITY.md` is scored and the band allows compile.
- [ ] Coherence (prep) passed; logic summary present in QUALITY.md.
