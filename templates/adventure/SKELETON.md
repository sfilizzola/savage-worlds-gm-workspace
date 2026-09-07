# RUN.md writing contract

Do not copy this file into an adventure directory. Follow it when generating or compiling `<path-to-adventure>/RUN.md`, whether that adventure is a standalone unit or a child of a campaign.

Modular sources remain authoritative. `RUN.md` is the table document. Story points are reachable situations, not a visit order. Flavor must not overrule predetermined truths or rules authority.

A compile that omits a required block is incomplete. Fill the block or delete the situation; do not leave a heading with no payload.

## Table flow (one home)

The GM must be able to stay on the situation that is on the table. Do not require two sections open for one beat.

- **One home per payload inside `RUN.md`.** Speech, marks, Trait tables, stat blocks, and situation procedure appear once, in the story point (or nested door) where they are used. Pointers may name that home. Do not paste the same beats into First 15 minutes, Climax situation, a nested “as above” room, and the NPC appendix.
- **`RUN.md` may duplicate modular sources** (`plot.md`, NPC files, `encounters.md`). That is compile. Duplication *inside* `RUN.md` is a compile fail.
- **First 15 minutes** and **Mission in 30 seconds** are GM intro (checklist + five-bullet brief). They are not scenes. No quoted briefing, no at-hand boards, no fight extras. Name the opening story points and the trouble already in motion; play those story points.
- **Current situation** is the table-start clock. If play later jumps (briefing then drop), use labeled phases (Phase A table start / Phase B after the jump). Do not describe a later phase as if it has already happened at minute zero.
- **Climax situation** is an index: location, opposition, environment, urgency, secondary objective, and which story point holds speech and stats. Put spoken lines and at-hand boards in the story point that delivers the climax, not in the index.
- **Extra GM lookups** (what the players know and when, how to find a target, travel/gates/circuit) go **after** the story points, not before Opening mood. Play the SPs; flip to lookups when needed.
- **Nested locations** exist only when they are a **different** door or room. If the story point *is* the room, do not add a nested heading that repeats Mood, speech, rolls, or stats. A nested door fills only what is new; shared rolls stay on the parent.
- **NPC quick reference** is an index (name, type, start pin, which SP holds the block). Do not reprint spoken lines or full stat blocks there.
- **Rules quick reference** holds night-wide constants (Called Shots, Recoil, “do not import”). Situation procedure (this jump, this kit ask, this illumination at the LZ) lives in the SP that rolls it.
- Story-point **titles** may keep numbers for compile; name the place so skippable points do not read as a tour. A jumplist under “Not a scene script” is allowed.

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
11. Optional GM lookups (omit the heading if none): player-knowledge, finding a target, travel/gates/circuit — after story points, never before Opening mood
12. Escalation and clocks
13. Failure-forward reference
14. PC spotlight and safety
15. NPC quick reference
16. Rules quick reference
17. Handouts index (omit the section if there are no handouts)
18. GM secrets
19. End states
20. Table checklist
21. After play note

## Notation

State these rules once under **Notation**. Use them throughout the file.

| Rule | Table form |
|---|---|
| First appearance of an NPC or named creature | **ALL-CAPS** on first mention in that situation; normal title case after |
| Trait test | `` `Notice (-2)` ``, `` `Persuasion` ``, `` `Survival (+1)` `` — Trait name, optional modifier, no invented skill names |
| Information rolls | Always state fail, success, and raise when the roll reveals information |
| Quoted speech | Quotation marks for lines the GM can speak. Not a read-aloud script. Omit the field if nobody speaks. Carry speech in a **Spoken lines** field or a blockquote that opens with the quotation mark, so the printer can tint it |
| Mood | Four labeled lines the GM paraphrases to the table **now**: **Climate**, **See**, **Hear**, **Feel**. Player-perceivable only. Not a boxed read-aloud. No secrets, unearned names, historical footnotes, or GM editorials |
| GM Note | Labeled **GM Note.** Secret or ruling. Never player-facing |
| Optional material | Label **Optional.** Side paths must not gate the main objective |
| PC-specific hook | Label **PC hook — Name.** Must not be the only vector for essential information |
| Wild Card / Extra | Label every stat block. A named Extra promoted to Wild Card uses the Extra profile and rolls a Wild Die |
| Handouts | Reference inline (`Handout A`) and list them in the Handouts index |

**Opening mood** (document section 4) is a GM throughline of the night: briefing calm → trouble. It may mention facts the players do not know yet. Do not speak it as the landing.

**Story-point Mood** is what you paraphrase to the table when that situation is on. Compile it from the location's **First impression**.

**Speech carriers.** `tools/print-run/` tints NPC speech so the GM can find a voice mid-scene. Two carriers get that tint:

- A **Spoken lines** field (list item or paragraph). An attribution parenthetical is allowed: `**Spoken lines (CAPT. ELLIS WARD):**`.
- A blockquote whose first character is the quotation mark, used for a longer beat the GM speaks as written.

Quotation marks used for paraphrase, idiom, or a nickname stay in ordinary prose and are deliberately left untinted. Do not put speech only in a table cell or an unlabeled paragraph; label it or blockquote it.

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

Omit this heading when it is the same space as the story point. Use it only for a different door or room. Fill only fields that are new; do not repeat parent speech, Trait tables, or stat blocks.

- Sensory frame: four Mood lines for this door. Do not write `as story-point Mood` as a substitute for omitting a same-space nest.
- People and forces:
- Environment/hazards:
- Spoken lines: only lines that belong to this door
- Discoverable: only rolls that are unique here; otherwise point at the parent table
- GM Note:
- Changes if delayed:

> [!IMPORTANT]
> #### At-hand statistics
>
> One published-layout block per Wild Card or Extra profile in this `RUN.md`. Compile from character files rather than sending the GM to those files at the table. Do not paste the same block into First 15 minutes, Climax situation, and the story point.

> [!TIP]
> #### At-hand rules
>
> Recurring or easy-to-miss procedure for this situation. Short paraphrase plus authority. Box environment rules that will be used more than once (travel, weather, drowning, thin air, darkness).
```

Use GitHub-style Markdown alerts for both at-hand boards. Prefix every content line and every blank line inside the board with `>` so the heading and all of its content stay inside one alert. End the board with a normal unquoted blank line before another alert or heading:

- `> [!IMPORTANT]` contains the complete **At-hand statistics** board.
- `> [!TIP]` contains the complete **At-hand rules** board.

Do not use a plain heading for either board. The alert is semantic source Markdown: compatible viewers highlight it, and `tools/print-run/` maps it to a high-attention, keep-together PDF card.

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

**First 15 minutes** must name trouble already in motion, not only a map or briefing: what they are handed, where they are, the trouble, the first decision, and which story points to open. A map-only briefing is not the opening. This block is a checklist. Do **not** put briefing speech, marks, or at-hand statistics here — those belong in the opening story point(s).

**Climax situation** must list location, opposition (Wild Cards / Extras), environment, urgency, and a secondary objective besides defeating everyone. Do not script the outcome. Spoken lines, at-hand stats, and at-hand rules live in the story point that delivers the climax. The front block is an index (name that story point). Do not copy the fight into both places.

## Handouts, pregens, re-entry

- Reference each handout at the situation that uses it.
- Pregen spotlight hooks belong under PC spotlight and safety, not as the only path through a story point.
- Name the spare / re-entry character in PC spotlight and safety.

## Compile gate

Refuse to call `RUN.md` complete unless all of the following are true:

- [ ] Document order above is present (omit Handouts index only when there are no handouts; omit optional GM lookups when there are none).
- [ ] Notation section is filled and followed.
- [ ] Table flow (one home): no payload copied across First 15 minutes, Climax situation, nested same-space rooms, and the story point that uses it.
- [ ] First 15 minutes is a checklist that points at opening story points; it contains no Spoken lines and no at-hand boards.
- [ ] Current situation is the table-start clock (phased if the start later jumps).
- [ ] Climax situation is an index; speech and stats are in the delivering story point.
- [ ] Extra GM lookups, if any, sit after the story points.
- [ ] Nested locations are different doors only; no “as above” repeats of parent speech or stats.
- [ ] Every story point uses the situation-block order.
- [ ] Every story point has a **Mood (table)** with Climate / See / Hear / Feel; no secrets in Mood.
- [ ] Every information roll states fail, success, and raise.
- [ ] Every situation with a speaker has quoted lines **in that situation**.
- [ ] Every situation with a secret has a GM Note.
- [ ] Every plausible fight or named Wild Card/Extra has an at-hand stat block in published layout **once**, in the situation where it matters.
- [ ] Failure changes play; it does not stop the main plot by itself.
- [ ] Story points are not written as a mandatory sequence.
- [ ] `QUALITY.md` is scored and the band allows compile.
- [ ] Coherence (prep) passed; logic summary present in QUALITY.md.
