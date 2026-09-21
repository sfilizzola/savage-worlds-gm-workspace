# Encounters and Challenges

This file owns every value the mill yard rolls: illumination, cover, the four crew Extras,
the crew's firing doctrine, the magazine hazard, and Len Pell's treatment clock. `plot.md`
and `locations.md` point here and must not restate a number.

The night is mostly ordinary Trait tests. Standard combat is used only if Lilly's choices
produce it, and the crew would rather drive away than fight. No setting module is active.
Active house rules are HR-NFA-001 (Lilly's build) and HR-NFA-002 (investigation
procedures); neither changes combat, and HR-NFA-002's do-not-use list explicitly excludes
Gritty Damage and Knock-Out Blows — this is a SWADE shooting, not a Deadlands one.

**Not in this file, deliberately.** Recoil (SWADE Fifth Printing (2023), p.105) and Called
Shots (p.98) are night-wide constants and belong in `RUN.md`'s rules quick reference, once.
The Wednesday/Saturday line, the go-clock, and the Len clock are `plot.md`'s. NPC voice is
in `npcs/`.

**The mill-office door is not an encounter.** It has never latched and it swings (`../world/locations/cinder-creek-lumber.md`). Do not call for `Thievery`, a Strength roll, or a
lockpick procedure on it. The spur-gate padlock is a different object and Meeks has the key.

## Yard-wide conditions

One home for everything the whole lot shares. Every encounter below assumes it.

### Illumination (SWADE p.102)

| Where | Category | Effect |
|---|---|---|
| The whole yard after 00:08, outside the work light | **Dark, −4** | Applies to attacks, Notice, and anything else sight-dependent. **Targets are not visible outside 10″ (20 yards).** |
| Inside the 500-watt clamp lamp's cone at the loading deck (~25 yards across, ~12″) | **Dim, −2** — GM's call | p.102 prints only Dim / Dark / Pitch Darkness. One clamp lamp throwing hard shadow over a 25-yard cone is read as Dim rather than unpenalized light. If the GM prefers to call the cone unpenalized, say so before play and keep it consistent. |
| Inside the shed row, a closed kiln, or the bunker with no light brought in | **Pitch Darkness, −6** | |
| Anything a flashlight or a headlight is actually on | **Dim, −2** in that beam — GM's call | p.102 gives no printed flashlight entry. Treat the beam as a Dim zone. |

**The asymmetry that runs this yard.** The crew are working inside light, so they are
visible from the dark at range. Lilly in the dark is not visible to them past 10″ (20
yards) — until she turns on a flashlight, steps into the cone, or closes inside 20 yards.
A light is the fastest way to search the shed row and the only reliable way to become the
one thing on the lot anybody can shoot at. On the dispatched-and-alone branch, that is
exactly why Kevin is fired on at 00:52: he crosses sixty yards of bare gravel with his
flashlight on.

The 10″ limit is a limit on seeing things **in the dark**. Watching the lit deck, the cone,
and the men working in it from out in the black is not restricted by it, at 30″ or 40″ or
from the fence — which is what `plot.md`'s SP4 `Notice` table already grants, including the
raise that picks Sloat out standing on the cone's edge with a long gun.

### Distances (1″ = 2 yards)

| From → to | Yards | Inches |
|---|---|---|
| Main gate → first stacks (bare apron, no cover) | 60 | 30″ |
| Main gate → loading deck | 80 | 40″ |
| Fence → scale house and car 1 | 20 | 10″ |
| Work-light cone, across | 25 | ~12″ |
| Audible range of Len banging the kiln door while conscious | 30 | 15″ |
| Yard's back corner → magazine, up the inland track | 400 | 200″ |

A pump shotgun's Short range is 12″ (24 yards) and a .38's is 10″ (20 yards) — which means
that in the dark, by the time the crew can see a target at all, almost every shot they take
is at Short range. That is the single most important lethality fact on this lot, and it is
also why the shotgun's Short-range-only +2 (p.105) will apply nearly every time Sloat
fires, even though it does not apply at Medium or Long.

### Cover (SWADE p.99)

Cover penalties are set by how much of the target is obscured: Light −2, Medium −4 (also a
prone target), Heavy −6, Near Total −8. If a miss would have hit without the cover
modifier, the obstacle acts as Armor equal to the material's Cover Bonus. The printed rows
are +2 heavy glass/drywall/wooden shield, +4 sheet metal/steel car door, +6 oak door/cinder
block, +8 brick, +10 stone wall/tree.

Yard features mapped to those printed rows. The penalty is situational; the Armor value is
the call this table makes once, here.

| Feature | Typical penalty | Armor if it stops a hit | Printed row used |
|---|---|---|---|
| Banded lumber stack | −6 to −8 | +10 | stone wall/tree — GM's call: a banded bundle of dimensional lumber is at least as solid |
| Bundled mill deck plate on the flatbed | −4 to −6 | +10 | stone wall — GM's call: steel plate exceeds a car door |
| Flatbed body, pickup body, car 1, Len's F-100 | −4 | +4 | sheet metal, steel car door |
| Loading-deck timber edge | −4 | +6 | oak door |
| Drying-shed board wall | −4 | +2 | drywall/wooden shield |
| Mill office frame wall | −4 | +2 | drywall |
| Scale-house block wall | −4 to −6 | +6 | cinder block |
| Dry kiln wall and door | −6 | +8 | brick wall |
| Concrete magazine bunker | −6 to −8 | +10 | stone wall |
| The 60-yard apron | none | none | there is nothing on it |

### Footing, noise, and radio

- Wet gravel, standing water between the sheds, about 46°F, low overcast. Call `Athletics`
  only where the fiction genuinely crosses something — the loading deck edge, the kiln
  apron, a stack face. Failure is prone or out of position; do not invent damage.
- The inland track after rain is Difficult Ground: 2″ of Pace per inch on foot (p.92).
- The generator on the pickup bed runs the whole time and covers ordinary noise at the
  gate; it does not cover a shot, a shout, or a car door.
- Lilly's portable is patchy at the fence and much worse inside the yard; the car radio at
  the mill road works. This is position, not a roll.

### Lilly's own gear

Her sheet is the authority (`../characters/lilly-dawson.md`) and this file does not change
it. Two things the GM should have settled before the yard:

- **The vest decides how this night goes.** A Kevlar Vest is Armor +2 and reduces damage
  from bullets — which includes shot from a firearm — by a further 4 (p.70). Against
  Toughness 4 that is the difference between Shaken and the Injury Table. It also carries
  Min Str d6 against her Strength d4, so wearing it costs **−1 to Pace, Agility, and
  Agility-linked skills** (p.66), which for her means Shooting, Athletics, Stealth,
  Driving, and Fighting. Make her feel that trade at the precinct, not at the fence.
- **Her 9mm has no printed row chosen.** Glock (9mm) — 12/24/48, 2d6, AP 1, RoF 1, Shots 17
  (p.74) — is the obvious 1986 service-pistol match, but pinning it is an edit to her
  canonical sheet and is out of this file's scope. Settle it before play.

## Encounter 1 — The fence line and the apron

- **Trigger:** anyone comes up the mill road to the main gate — Lilly alone, Lilly with Kevin, Kevin ahead of her, or Kevin on his own loop at about 01:20.
- **Purpose and stakes:** deliver the reversal somewhere she can still choose. This is the last safe ground and it should stay safe long enough for her to decide something.
- **Opposition goal:** nothing here. The crew is 40″ away behind a running generator with the stacks between them and the gate. They know a cruiser lives in the scale house and have worked around it for months. They are not watching this gate.
- **PC objective:** read the yard, account for Len's truck and the empty nail, decide what to do with Earl, decide whether to call Rookton before anybody is hurt, and decide how — or whether — to cross sixty yards of bare gravel.
- **Environment and tactical facts:** Dark (−4) everywhere here, and the crew cannot see an unlit figure at the gate at all. Cover at the gate is the office wall (+2), Len's F-100 (+4), the scale-house block (+6), and the fence line. There is no cover whatsoever on the apron. The fence line around to the spur side and the inland track from the back corner are both routes that avoid the apron entirely and cost time.
- **Scaling:** one Novice Wild Card, with or without one patrol Extra. Do not add opposition.
- **Early-removal risk:** mitigated. Nothing at this gate can shoot her. The only way a round is fired here is the dispatched-and-alone branch at 00:52 with Kevin lit on the apron, or Lilly crossing the apron with a light on, or Lilly firing first.
- **Failure consequence:** being noticed costs surprise and starts Meeks's go-clock (`plot.md`, Night clock) — fifteen to twenty minutes to wheels-up from that moment. The cost of being seen is a truck that is already leaving, not gunfire.
- **Exit conditions:** she crosses the apron, works around the fence to the spur, takes the inland track, withdraws to the road to call, or stands at the gate until the flatbed pulls out.
- **Spoken lines:** nobody in the crew speaks at this range. Kevin's and Earl's lines for this ground are in `plot.md`, SP4, and `locations.md`.

### When the crew fires

This is a GM decision made from what the crew can actually see. **Do not roll for it.**

Meeks's standing instruction to his men tonight is that nobody shoots at a police officer
over scrap. Sloat fires anyway only when all three of these are true at once:

1. Something is moving at the deck that he cannot resolve — a light crossing the apron, movement inside about 10″ (20 yards) of the deck, or a shape stepping into the cone.
2. He has shouted once — "Stay off the deck!" — and got nothing back.
3. Meeks has not told him to stop.

**He does not fire when:**

- There are visibly **two badges** — two lights, two voices, or a marked car at the gate. Meeks calls rope-and-go and Sloat's job becomes carrying. **Two badges buy a departure, not a firefight. Shots are not the automatic price of being seen.**
- A police officer is standing still in the open, identified, at any distance.
- Meeks has already started the go-clock and said the word.

Once anyone in the crew has been fired at, or once somebody is physically between the
flatbed and the spur gate, all four will shoot to break contact — and only to break
contact. They fire from the deck, the stacks, and the truck; they do not advance on the
gate, do not pursue into the dark, and do not take hostages. Runkle goes to the pickup's
door pocket only at that point, and would rather not.

### Runtime statistics

All four crew profiles live once under Encounter 2. Earl Voss and car 1 are in
`locations.md`; he stays in or behind the car.

### Rules verification

- **SWADE authority:** p.102 Illumination; p.99 Cover & Obstacles; pp.87–88 Wild Cards and Extras; p.100 The Drop; p.108 Surprise.
- **Active setting authority:** none.
- **House rule:** none applies at the fence.
- **Adaptation notes:** the crew's firing doctrine is fiction and GM judgement, not a subsystem. Do not convert it into a Notice contest or a morale roll; SWADE has neither here.

### Difficulty review

- **Expected pressure:** a decision under a clock, not a fight.
- **Volatility or swing risk:** low, unless she crosses 30″ of open gravel with a light on.
- **Resource drain:** minutes, and the surprise she still has.
- **Player-count adjustment:** written for one Novice Wild Card. Do not add enemies at either end of the range.

## Encounter 2 — The load-out at the deck

- **Trigger:** she crosses the fence line by any route and closes on the loading deck, or the crew becomes aware of police on the ground.
- **Purpose and stakes:** the climax. A truck that wants to leave, four men who would rather be on the highway, a man behind a barred door, and six cases moving toward the flatbed.
- **Opposition goal:** the flatbed loaded and eastbound on 328. Meeks gives up copper before the truck and the truck before a man to a shooting charge. Nobody here wants a gunfight and one of them has already panicked once tonight.
- **PC objective:** any of — stop the load, take the crew, reach Len, keep the cases in the county, keep Kevin upright, and leave a scene that can be written. They will not all fit into the same minutes and they are not all required.
- **Environment and tactical facts:** Dark (−4) outside the cone, Dim (−2) inside it, 10″ sight limit on unlit targets, the cover table above, a running generator, wet ground between the sheds, and the mill pond south of the stacks — deep at the old log dump and not somewhere to back a vehicle. The spur road puts a moving truck on 328 in under a minute.
- **Scaling:** four Extras against one Novice Wild Card, possibly with Kevin. **Do not add opposition and do not promote anyone to Wild Card.** If Lilly arrives hurt or alone, start Ned already off the winch and looking at the shed row, and have Meeks open with rope-and-go rather than a stand.
- **Early-removal risk:** real, and deliberately telegraphed before she crosses the fence (`characters.md`, Later lethality). Mitigations: the crew shoots to break contact and stops shooting the moment the truck can move; one Wound Incapacitates each of them (p.95), so she can end a shooter with a single good hit; Kevin can carry the scene; the vest exists.
- **Failure consequence:** she can win the yard and lose the powder, hold the powder and lose the truck, take the crew and reach Len late, or go down and come to behind the scale house with the load gone. None of it closes the case (`plot.md`, SP5).
- **Exit conditions:** the flatbed leaves or is stopped; the crew surrenders, scatters, or is Incapacitated; Lilly withdraws; the spur road is blocked and Meeks starts looking for a trade.
- **Spoken lines:** Meeks, to his own men: "Rope it. We're going." Sloat, into the dark before he fires: "Stay off the deck!" Ned Colfax, cornered: "He came round the sheds. He wasn't supposed to be here. Nobody's supposed to be here." Full Portrayal and pressure variants are in `npcs/`.

### Interrogating Ned Colfax

The Trait table for Ned — fail, success, raise, and the unsigned Wednesday/Saturday line —
is `plot.md`'s, SP5, and is not repeated here. Mechanically it is an ordinary opposed
`Persuasion` or `Intimidation` test. If the table wants it played out at length, HR-NFA-002
allows the Interrogations procedure — a three-round Social Conflict using Intimidation,
Persuasion, or Taunt (*Deadlands Noir*, PEG 2012, p.31; SWADE Social Conflict, p.143). A
failure costs time and how tomorrow morning goes; it never deletes the vector. Meeks is not
a valid target for it — he does not repeat the arrangement to police under any procedure.

### Runtime statistics

All four are **Extras**: one Wound Incapacitates (p.95), they roll a single Trait die with
no Wild Die (pp.87–88), and a group with identical Traits may share one Action Card (p.91).
Built freehand under SWADE's Creating Extras guidance (p.202) rather than with character
creation. Derived statistics follow pp.10–11.

**ROY MEEKS** — Extra
Attributes: Agility d6, Smarts d8, Spirit d8, Strength d6, Vigor d6
Skills: Athletics d4, Common Knowledge d6, Driving d8, Fighting d4, Intimidation d8, Notice d6, Persuasion d6, Repair d4, Shooting d6, Stealth d4
Pace: 6; Parry: 4; Toughness: 5
Hindrances: none needed at table
Edges: none
Gear: Police Revolver (.38) in his coat — 10/20/40, 2d6, AP —, RoF 1, Shots 6, reloaded one round at a time (p.74); flatbed keys; spur-gate padlock key; work gloves; a watch he keeps checking
Special Abilities: none
Personality: arithmetic, not anger. Gives up the small charge fast to keep clear of the large one.
Authority: SWADE Fifth Printing (2023), pp.10–11, 74, 87–88, 95, 202

**NED COLFAX** — Extra
Attributes: Agility d6, Smarts d6, Spirit d4, Strength d8, Vigor d6
Skills: Athletics d6, Common Knowledge d6, Driving d4, Fighting d4, Notice d6, Persuasion d4, Repair d8, Stealth d4
Pace: 6; Parry: 4; Toughness: 5
Hindrances: none needed at table
Edges: none
Gear: bolt cutters, cable knife, flashlight, mill coat. **No firearm.** The 24-inch pry bar is lying across the latch of dry kiln No. 2 where he threw it at 00:02; if he ever picks it up it is a Medium improvised weapon — Range 2/4/8, Damage Str+d6, Min Str d6, **−2 to the attack roll** (p.102)
Special Abilities: none
Personality: will not fight and will not run well. Talks about the job freely and stops dead on who guaranteed the day of the week.
Authority: SWADE Fifth Printing (2023), pp.10–11, 87–88, 95, 102, 202

**DALE RUNKLE** — Extra
Attributes: Agility d6, Smarts d4, Spirit d6, Strength d8, Vigor d8
Skills: Athletics d6, Common Knowledge d4, Driving d8, Fighting d6, Notice d4, Repair d4, Shooting d4, Stealth d4
Pace: 6; Parry: 5; Toughness: 6
Hindrances: none needed at table
Edges: none
Gear: crew-cab pickup with the generator on the bed; chains, rope, hand winch; Ruger (.22) **in the driver's door pocket, not on his person** — 10/20/40, 2d4, AP —, RoF 1, Shots 9 (p.74)
Special Abilities: none
Personality: talks to the truck. Will not drive at a badge and will not fight over somebody else's load.
Authority: SWADE Fifth Printing (2023), pp.10–11, 74, 87–88, 95, 202

**JIMMY SLOAT** — Extra
Attributes: Agility d8, Smarts d4, Spirit d6, Strength d6, Vigor d6
Skills: Athletics d6, Common Knowledge d4, Driving d6, Fighting d4, Notice d6, Shooting d6, Stealth d6
Pace: 6; Parry: 4; Toughness: 5
Hindrances: none needed at table
Edges: none
Gear: Pump Action shotgun — 12/24/48, Damage 3d6/2d6/1d6 at Short/Medium/Long range, RoF 1, Shots 6, Min Str d4 (pp.74, 105); a coat pocket of shells, reloaded one shell as a free action once per action (p.105)
Special Abilities:
- Shotgun (p.105): **+2 to his Shooting roll at Short range only** — inside 12″ (24 yards). At Medium and Long he rolls with the ordinary range penalties and **no shotgun bonus**. Damage by band — **3d6 Short, 2d6 Medium, 1d6 Long**. No Extreme range. On a miss, each skill die showing a **1 or a 2** may hit a bystander in or adjacent to the line of fire (p.102) — which matters with Kevin, Earl, or Ned anywhere near her.
Personality: shouts a boundary before he does anything. Fires at noise and movement, not at people he has identified.
Authority: SWADE Fifth Printing (2023), pp.10–11, 74, 87–88, 95, 102, 105, 202

### Allied and civilian runtime profiles

Written here because this night rolls them. The campaign files in `../world/npcs/` remain
the owners of who these people are; do not copy these blocks back there without GM sign-off.

**LEN PELL** — Extra; behind the barred door of dry kiln No. 2
Attributes: Agility d6, Smarts d6, Spirit d6, Strength d6, Vigor d6
Skills: Athletics d4, Common Knowledge d6, Fighting d4, Notice d6, Persuasion d4, Repair d6, Shooting d4, Stealth d4
Pace: 6; Parry: 4; Toughness: 5
Gear: Rennick key on his belt; flashlight, dropped on the kiln apron
Current state: **one Wound and therefore Incapacitated** (p.95) since 00:02. See Encounter 4 for the treatment clock.
Authority: SWADE Fifth Printing (2023), pp.10–11, 87–88, 95, 202

**KEVIN ALDER** — Extra; Ashgrove PD night patrol
Attributes: Agility d6, Smarts d6, Spirit d6, Strength d6, Vigor d6
Skills: Athletics d6, Common Knowledge d6, Driving d8, Fighting d6, Notice d6, Persuasion d4, Shooting d6, Stealth d4
Pace: 6; Parry: 5; Toughness: 5
Gear: service revolver — Police Revolver (.38), 10/20/40, 2d6, AP —, RoF 1, Shots 6 (p.74); flashlight; portable and car radio; car 2
Authority: SWADE Fifth Printing (2023), pp.10–11, 74, 87–88, 95, 202

**Earl Voss** has no written statistics and does not need any. By prep he stays in or behind
car 1, holds a radio, and takes no action that would be rolled. If the table puts him
somewhere dangerous, build him freehand under p.202 before resolving anything.

### Rules verification

- **SWADE authority:** pp.10–11 derived statistics; p.74 modern firearms; pp.87–88 Wild Cards and Extras; p.91 Action Cards and grouped Extras; p.92 movement and Difficult Ground; p.93 ranged attacks and range penalties (Short 0 / Medium −2 / Long −4); p.95 Wounds and Incapacitation; p.99 Cover; p.100 The Drop; p.102 Illumination, Improvised Weapons, Innocent Bystanders; p.103 Multi-Actions; p.105 Shotguns and Reloading; p.143 Social Conflict; p.202 Creating Extras.
- **Active setting authority:** none.
- **House rule:** HR-NFA-001 governs Lilly's build only. HR-NFA-002 permits the Interrogations procedure for Ned and forbids importing Gritty Damage or Knock-Out Blows.
- **Adaptation notes:** all four opponents are custom civilian Extras with no combat Edges, no armor, and no invented gear. No opposing Wild Card appears on this yard. Suppressive Fire (p.107) is technically legal for Meeks's revolver and Runkle's .22 — the rule only asks that a weapon fire at least as rapidly as a revolver and need no reload between shots — but neither man uses it: it burns three times the Rate of Fire in ammunition and always causes Recoil, out of six and nine rounds respectively, and these two are breaking contact rather than pinning anybody. Sloat's pump gun is a GM's call the other way; do not let it suppress.

### Difficulty review

- **Expected pressure:** high for a solo Toughness-4 Wild Card the moment she is visible at Short range. Four Extras, of whom one is genuinely armed and willing, one is armed and reluctant, one is armed and ten feet from a truck door, and one is not armed at all.
- **Volatility or swing risk:** the shotgun is the swing. Inside 12″ it is 3d6 with the Short-range +2 to hit (p.105); beyond that it drops to 2d6 with no bonus and ordinary range penalties. Against Toughness 4 the average Short-range roll Shakes her and a good one puts her on the Injury Table. **With the Kevlar vest she is Toughness 6 and takes 4 fewer from any bullet or shot (p.70), which converts most of those results back into Shaken.** The other two guns are 2d6 and 2d4 in nervous hands. Reduce the swing by playing Dark honestly — the crew genuinely cannot see her past 10″ — and by having Sloat shout before he shoots, every time.
- **Resource drain:** Bennies, Wounds, ammunition, minutes off Len's clock, and position on the spur road.
- **Player-count adjustment:** written for one Novice Wild Card, with Kevin as an ally Extra the player may direct (p.202, Allies). Do not add opposition at any player count.

## Encounter 3 — The inland track and the magazine

- **Trigger:** she walks or drives the track from the yard's back corner, blocks it, or is on it when Runkle brings the pickup up between about 00:45 and 01:10.
- **Purpose and stakes:** the clock inside the climax and, optionally, a second problem. Keeping six cases of 1978 ammonia stumping powder off a flatbed that is about to drive 22 miles of two-lane.
- **Opposition goal:** Runkle wants three two-case loads down the track without bogging the pickup. Meeks stays at the deck.
- **PC objective:** secure, delay, or simply occupy the track. Standing on it is enough — Runkle will not drive at a badge — and it is a legitimate, quiet way to spend the climax that costs her the deck.
- **Environment and tactical facts:** Pitch Darkness (−6) under the second growth with no light brought in; Dim (−2) in whatever beam anyone carries. 400 yards (200″) from anyone who could help. Soft ruts after rain: Difficult Ground on foot at 2″ of Pace per inch (p.92), and a real prospect of bogging a loaded pickup. The bunker is concrete — Heavy to Near Total Cover, +10 as Armor if it stops a hit. Sound carries down to the deck; the track cannot be seen from it.
- **Scaling:** one Extra, one truck, and a hazard. Do not staff the bunker.
- **Early-removal risk:** Runkle is the least dangerous man in the crew and his gun is in the truck. The hazard is the risk here, and the fiction must say so — the smell, the greasy cases, the taped tin of caps in the same room — before anybody points a weapon in that building.
- **Failure consequence:** the cases reach the flatbed and, if the truck goes, leave the county. That is a failure state the adventure is allowed to have.
- **Exit conditions:** the track is held, Runkle is stopped or taken, the cases are secured where they are, or the last two go down the track and onto the tarp.
- **Spoken lines:** Runkle, backing the pickup, to nobody: "Slow. Slow. Slow." Runkle, when a light is on the track ahead of him: "I'm stopped. I'm stopped, look — I'm stopped." Ned, if he is present and thinks anyone is about to drive it: "That stuff up the track is seventy-eight. You don't put seventy-eight on a truck."

### What the powder resolves as — and what it does not

**Decided and usable at the table:**

- **Finding and reading it.** `plot.md`'s SP5 table owns the `Notice` on the load and the `Common Knowledge` on the cases. Do not duplicate them.
- **Handling and carrying.** Ordinary `Athletics`. A drop is a fiction event that raises the question below; it is not a damage roll.
- **Driving the track.** Ordinary `Driving`. A bogged pickup is lost position and lost time, not a wreck.
- **Burning.** Fire is fully covered: a flammable target hit by fire catches on a d6 roll of 6, a very flammable one on 4–6, a volatile one on 2–6, and the Fire Damage table runs 1d6 spot contact / 2d6 burning room / 3d6 flamethrower, growing on a 6 and dropping on a 1 at the start of the victim's turns, with `Athletics` as an action to put it out and Armor protecting normally (p.127).
- **Securing it.** Standing on the track works and needs no roll at all.

**Not decided, because no active authority establishes it:**

> **RULE UNCLEAR - GM DECISION REQUIRED**
>
> **Question.** If a round strikes a case, a case is dropped or driven off the pickup bed,
> or fire reaches the bunker with the taped tin of caps in it, does anything detonate
> tonight — and if so, with what damage, what template, and how many cases?
>
> **Sources checked.** SWADE Fifth Printing (2023): p.34, the Repair skill "covers the use
> of demolitions and explosives" but supplies no yield; pp.78–79, the only printed bulk-blast
> gear in core is military grenades and mines, every row tagged Heavy Weapon; pp.97–98, Area
> Effect Attacks and Blast Templates are a delivery method and carry no yield for this
> material; p.127, Fire covers burning but not detonation; p.125, Hazards has no explosion
> entry. No setting module is active. HR-NFA-001 and HR-NFA-002 do not touch explosives.
> There is no SWADE profile for commercial blasting agent, for blasting caps, or for
> degraded stock.
>
> **Options, clearly labeled. Do not blend them and do not invent a fourth.**
>
> - **Option A — no detonation tonight. This is the default if the GM does not rule before play.** The cases burn under Fire (p.127) and never go off. The hazard is fire, smoke, a building to get people out of, and a 22-mile ambulance. Every clock, vector, and end state in this adventure still works.
> - **Option B — the GM names one printed profile and applies it unchanged.** For example, one case resolved as an Anti-Tank Mine, 4d6 in a Medium Blast Template (p.79), or as an Anti-Personnel Mine, 2d6+2 in a Small Blast Template (p.79). If this is chosen, the GM must state which row, whether the Heavy Weapon tag applies, and how many cases are involved — and must not scale, average, or homebrew a row.
> - **Option C — narrative resolution.** A detonation ends the scene without a damage roll; the GM adjudicates who was where and what survives.
>
> **Afterwards.** Record the decision in [`../../../rules/rulings.md`](../../../rules/rulings.md) per [`rules/RULES.md`](../../../rules/RULES.md), "Unclear rules". Promote it to `house-rules.md` only if the GM explicitly wants a standing override.

**Regardless of the option chosen:** the magazine is a clock and a hazard. **Prep never
detonates it.** No entry on the night clock, no escalation, and no failure state may fire
it on its own. Only a player or crew action, adjudicated under the option above, can.

### Runtime statistics

Runkle's profile is under Encounter 2. Nothing else out here has statistics, because
nothing else out here is a creature.

### Rules verification

- **SWADE authority:** p.34 Repair; p.92 Difficult Ground; p.99 Cover; p.102 Illumination; pp.78–79 and pp.97–98 checked and found not to cover this material; p.125 Hazards; p.127 Fire; p.202 Creating Extras.
- **Active setting authority:** none.
- **House rule:** none. Neither active house rule covers explosives.
- **Adaptation notes:** no homebrew blast value is written anywhere in this adventure. `plot.md` and `locations.md` both already point here and both already say not to invent one.

### Difficulty review

- **Expected pressure:** low combat pressure, high consequence pressure. The scariest thing on this track is the building.
- **Volatility or swing risk:** entirely contained by the ruling above. Under Option A there is no swing at all.
- **Resource drain:** time — and the deck, which is the real cost of choosing this ground.
- **Player-count adjustment:** none.

## Encounter 4 — Dry kiln No. 2 and Len Pell's clock

Not a combat. This is the treatment procedure `plot.md` and `locations.md` both defer to.

- **Trigger:** she reaches the shed row, hears banging, or follows the blood on the kiln apron.
- **Purpose and stakes:** the human objective under the firefight, and the thing that makes elapsed time cost something real.
- **Opposition goal:** none. Nobody is guarding him and nobody has looked at him since 00:02.
- **PC objective:** get the bar off the door, get him warm, and get Rookton rolling.
- **Environment and tactical facts:** north side of the shed row, out of the light, Pitch Darkness (−6) inside the kiln. The outside bar lifts by hand — this is not a `Thievery` test and not a Strength contest. `plot.md`'s SP5 `Notice (−2)` table owns finding him; it is not repeated here.
- **Early-removal risk:** none to Lilly.
- **Failure consequence:** time, which is the only currency here.
- **Exit conditions:** he is out and warm, he is out and unconscious, or he is still behind the door when the night ends.
- **Spoken lines:** Len, if he is still conscious: "Whoever that is — the bar's on the outside."

### Condition and treatment values

He took a 24-inch pry bar above the left ear at 00:02. As an Extra, that single Wound
**Incapacitates** him (p.95), and p.95 leaves consciousness to the GM. This prep decides two
things so the clock runs the scene instead of a die rolled hours before the table:

1. **He is Incapacitated and not Bleeding Out.** Do not roll his Incapacitation Vigor as prep.
2. **He is conscious until roughly 01:05 and unconscious after** — matching the fiction in `plot.md`'s Len clock.

Conscious-and-Incapacitated is printed-legal: he can talk, he can bang the door, and he
cannot take a useful action until somebody treats him.

**The Golden Hour is the mechanical version of the whole clock.** Healing may only remove
Wounds within the hour they were sustained (p.96). His injury is at 00:02, so that window
closes at about **01:02**. The consciousness clock is separate: he may remain awake and
banging until roughly 01:05, but consciousness does not extend the Healing window.

| When he is reached | State | What resolves it |
|---|---|---|
| Early enough to complete treatment by 01:02 (normally reached by about 00:52) | Conscious, furious, concussed | `Healing` takes 10 minutes per Wound level, **−1 without a first aid kit** (p.96). If completed by 01:02, a success removes the Wound and with it the Incapacitated state (p.96): he can stand with help and hold a flashlight. No survival roll is needed if he is warmed and Rookton has been called. |
| About 00:52 to 01:02 | Conscious, furious, concussed; Golden Hour not yet closed, but fewer than 10 minutes remain | Get him out, warm him, and get Rookton rolling. There is not enough time to complete the 10-minute `Healing` procedure before the window closes, so do not roll it to remove the Wound. He remains Incapacitated and cannot walk merely because the door is open. |
| About 01:02 to 01:05 | Conscious, concussed, still able to talk and bang | The Golden Hour has closed; no `Healing` roll can remove the Wound (p.96). Get him warm and get him to the ambulance. He remains Incapacitated. |
| About 01:05 to 02:00 | Unconscious, breathing, cold | The Golden Hour has closed; no `Healing` roll can remove the Wound (p.96). Survival resolves with a **`Vigor`** roll under Aftermath & Extras (p.96) when he reaches the ambulance. GM's call: no modifier. `Healing` can still stabilize him if the GM has put him into Bleeding Out (pp.95–96). |
| After about 02:00, or found by Kevin or Earl later | Deep cold on top of a head injury | The same **`Vigor`** under Aftermath & Extras (p.96), at a GM's-call **−2** for elapsed exposure. **This is the branch where he can die, and it is elapsed time doing it, not prep.** |
| Not reached tonight | Morning, by Daisy or by whoever comes for his truck | Same roll, same GM's-call penalty, no worse than −2. |

**The printed Cold hazard does not apply and should not be reached for.** SWADE's Cold rule
is a Vigor roll every four hours in weather **below freezing** (p.125). Tonight is about
46°F and the whole night is under five hours. The cold in this scene is fiction and
pressure; the only die it touches is the Aftermath & Extras Vigor above. The −2 in the
table is a GM's call for that reason — if it is used, record it in `rules/rulings.md`.

**The cheapest thing Lilly can do is the telephone.** Rook County's ambulance is about 30
minutes out from Rookton and 30 back (`plot.md`). Calling it at 00:25 costs nothing and is
worth more to Len than any roll in this file.

### Rules verification

- **SWADE authority:** p.95 Wounds, Incapacitation, Bleeding Out; p.96 Healing, the Golden Hour, Natural Healing, Aftermath & Extras; p.102 Illumination; p.125 Cold, checked and found not to apply above freezing.
- **Active setting authority:** none.
- **House rule:** none. HR-NFA-002's do-not-use list keeps *Deadlands Noir* Gritty Damage and Knock-Out Blows out of this scene.
- **Adaptation notes:** the elapsed-time penalty on the Aftermath & Extras roll is a GM's call, flagged as such, and is the only non-printed number in this encounter. No hypothermia track, no bespoke bleed clock, and no invented head-injury rule is used.

## Encounter 5 — If the flatbed rolls

- **Trigger:** Meeks's go-clock runs out, or the spur road is open and he decides the copper aboard is enough.
- **Purpose and stakes:** the load, and whether the cases are on it.
- **Opposition goal:** the spur gate, then 328 eastbound.
- **PC objective:** her own call — block the spur road, take the men on the ground, or follow.
- **Environment and tactical facts:** the spur road puts a moving truck on 328 in under a minute. If the road is blocked before he moves, Meeks cannot use the clock at all and starts thinking about what he will trade; that is the single highest-value piece of ground on the lot.
- **Scaling:** no additional opposition.
- **Early-removal risk:** standing in front of a loaded flatbed is exactly as dangerous as it sounds; say so before she does it.
- **Failure consequence:** part or all of the load, and possibly the powder, leaves the county. The case still closes on what is left behind (`plot.md`, end states).
- **Exit conditions:** the truck is stopped, blocked, abandoned, or gone east.
- **Spoken lines:** Meeks, to his men: "Rope it. We're going."

### Chase or no Chase

**Do not force a subsystem** (`GM.md`). If nobody is in a position to pursue, the truck
simply leaves and the night moves to SP6; that is a consequence, not an encounter.

Run SWADE's **Chases** (p.113) only if the fiction is an active pursuit — Lilly in the day
car behind a flatbed on gravel and then two-lane. If it is run, vehicle rows must be chosen
before play and are not decided here: p.83's Ground Vehicles table has **Mid-Sized Car**,
Handling 0, Toughness 11 (2), for the day car, and no row at all for a 1970s flatbed or a
crew-cab pickup. **Semi-Truck**, Handling 0, Top Speed 75, Toughness 14 (2), and **Sports
Utility Vehicle**, Handling 0, Toughness 14 (2), Four-Wheel Drive, are the nearest printed
analogues; if the GM uses them, name the substitution out loud rather than inventing a row.

### Rules verification

- **SWADE authority:** p.83 Ground Vehicles; p.113 Chases; pp.113–121 vehicle procedure.
- **Active setting authority:** none.
- **House rule:** none.
- **Adaptation notes:** the pickup and the flatbed have no printed rows. Substituting named rows is a labeled GM's call; do not write a homebrew vehicle profile into this adventure.

## Lethality, early removal, and re-entry

Restated here in mechanical terms; the fiction is in `characters.md`.

- **The precinct, Main Street, Daisy's, and the West End houses carry no threat at all.** Nothing in the opening can remove her.
- **The yard becomes lethal the moment she crosses the fence, and only then.** The transition is announced by the fiction — light where there should be none, a diesel idling, men loading in the dark, sixty yards of gravel with nothing on it — not by a roll.
- **What keeps it survivable:** the crew shoots only to break contact and stops as soon as the truck can move; one Wound Incapacitates every one of them; Dark honestly applied means they cannot see her past 10″; and the vest is available if she took the minute for it.
- **If Lilly is Incapacitated:** resolve her Incapacitation normally (p.95) and then hand the scene to Kevin for a short transition — he drags her behind the scale house while the clock advances and the load gets further gone. Control returns to the player with lost position, not a lost session. Sgt. Doyle is reachable by radio at about 40 minutes to the fence. Len is a pair of hands only after successful treatment removes his Wound, or if the table's fiction otherwise justifies equivalent support; opening the kiln alone is not enough. A terminal removal ends the night in a consequence-defined failure state; there is no replacement PC in this campaign.
- **Capture or separation:** the crew shuts somebody in only long enough to move the truck. No hostages, no holding ground. Give her the inside of wherever she is put and put her back in the night within a scene.
