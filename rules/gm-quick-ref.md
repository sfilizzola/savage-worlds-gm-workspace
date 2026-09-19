# GM quick reference — SWADE core

Print **one copy for the GM** (a single A4 page). Keep it beside whatever `RUN.md` is on the table. Not for players. Not session history. Not adventure-specific.

Two print builds of the same card. Pick by the paper in the tray:

| Build | Print it on | What differs |
|---|---|---|
| `print/gm-quick-ref.pdf` | **White paper.** Backgrounds must be on | Cream page flood and tinted panels are printed as ink |
| `print/gm-quick-ref_pf.pdf` | **Cream or coloured stock**, or any time you want to spare ink | No page flood, no tinted panels — the paper supplies the warmth. Panels are outlined instead |

Layout, type, and column breaks are identical in both; only the ink differs. Printing the cream build onto cream stock muddies it and wastes toner — use `_pf` there.

Rebuild a PDF from its matching HTML (`print/gm-quick-ref.html`, `print/gm-quick-ref_pf.html`) after editing: File → Print → A4, backgrounds on, headers/footers off, or Chrome `--print-to-pdf`, the same way `RUN.md` is printed. **Edit both HTML files when the content changes** — they are twins, not generated from each other. This markdown is the source text if the HTML is unavailable; keep all three in step.

Players already have (or should have) a player card. Do not reprint those basics here except where the GM needs the NPC-facing or GM-Benny version.

No house rule is on this card. If tonight's adventure activates one, write it on the night's `RUN.md` Rules quick reference, not here.

Column order on the printed card: **how rolls work** (Trait rolls, Bennies, The round, Test & Support) · **violence** (Attacks & damage, States) · **aftermath** (Going down, Healing, At the table).

---

# SAVAGE WORLDS — GAME MASTER'S CARD

SWADE Fifth Printing (2023), core rules only. Short paraphrase for the table; the book decides.

Tie order **♠ ♥ ♦ ♣**. Countdown Ace → Deuce. Reshuffle after any Joker. **1″ = 2 yards.** Tonight's light, opposition, and house rules live on `RUN.md`, not here.

**Wild Cards** (PCs and named foes): Wild Die d6 with every Trait, keep the higher; **three** Wounds, then Incapacitated.
**Extras** (everyone else): one Trait die; **one** Wound and they are out. Like Extras roll once as a group (Trait die + a Wild Die).

## Trait rolls

TN **4** unless opposed or a listed TN (Parry). Easy **+2**, hard **−2**, very hard **−4**. Wounds and Fatigue also subtract.

- **Ace:** max on a die → roll again and add. Trait and damage Ace. The Running die does not.
- **Raise:** every **4** over the TN, after modifiers. One raise is the extra effect.
- **Wild Die:** one per action. With RoF or Frenzy it *replaces* a die — it never adds a hit.
- **Unskilled:** d4−2 (plus the Wild Die if a Wild Card).
- **Opposed:** actor rolls first, Bennies and all. Still needs a 4. Defender must meet or beat. Raises count from *their* total.
- **Critical Failure:** Wild Card rolls 1 on Trait *and* Wild Die. Fails badly, **no Benny**. Extra: a 1, then a d6 — another 1 confirms. Multiple dice: over half show 1, Wild Die included.

## Bennies

**Players start with 3.** Leftovers vanish at end of session. Award for Hindrances played, clever moves, a line that lands. Be generous early; scarcity makes them hoard.

**Spend** (own character only): reroll a Trait, keeping the best — a CF still stands · un-Shake instantly, even off-turn · Soak · draw a new Action Card after the deal · reroll damage · regain 5 Power Points with an Arcane Background · nudge the story, if you allow it.

**Your side:** one Benny per player character in a shared pool, spendable on any of yours including Extras. Each of **your** Wild Cards brings **2** of their own when they appear (plus Luck). No sharing between them without an Edge.

**Joker's Wild.** A PC Joker → every player gets a Benny. A villain Joker → one into your pool *and* one to each enemy Wild Card. Either way that side acts whenever it likes this round at **+2** Trait and damage.

## The round

About six seconds. One card per Wild Card (plus Edges); like Extras share a card.

On their turn: move Pace and take **one** action. Movement is not an action. Climbing, crawling, swimming, and Difficult Ground cost **2″** per inch.

- **Run:** add the Running die (d6, never Aces), **−2** to every action this turn.
- **Multi-action:** up to three. Two = **−2** to all, three = **−4** to all. Declare before rolling. Free actions are exempt.
- **Free:** a short line, drop an item, go prone, stand (costs 2″ Pace), ready two familiar items, resist a roll, and one attempt to shake off Shaken or Stunned at the start of the turn.
- **Hold:** wait. Interrupting is opposed Athletics. Shaken or Stunned while on Hold loses it.
- **Surprise:** ambushers are on Hold. Victims roll Notice; failure means no card that round.

## Test & Support

**Support** helps an ally: a fitting skill, success **+1** and raise **+2** to one Trait total this round, **+4** maximum from everyone (Strength Support is uncapped). A Critical Failure costs the ally 2. The bonus expires at the end of their turn.

**Test** hinders a foe: describe it, roll the skill against the attribute that skill is *linked* to — Fighting as a Test is opposed by **Agility**, never Parry. Win and choose Distracted *or* Vulnerable; with a raise, also Shaken or another subjective effect you allow, such as knocking them prone.

Repeating the same Test earns a steep penalty or a flat no. Extra dice from RoF give one result — take the highest.

## Attacks & damage

| Attack | Roll | Target number |
|---|---|---|
| Melee | Fighting | Parry — 2 + half Fighting (2 unskilled) |
| Shot | Shooting | 4 + range, cover, light |
| Thrown | Athletics | 4 + range |

**Range:** Short —, Medium **−2**, Long **−4**, Extreme **−8** (needs Aim; never thrown). **Recoil −2** for more than one shot in an action.

A raise on the *attack* adds **+1d6** damage, once. Damage Aces. Melee damage is Strength + weapon, with **no Wild Die**.

**Against Toughness** — finish each hit, Soak included, before the next:

- Under it → nothing that counts.
- Success, 0–3 over → **Shaken**. Already Shaken and hit by *physical* damage → a Wound, still Shaken. A Test that only Shakes never Wounds.
- Each raise → that many **Wounds**, and Shaken.

**Soak.** After damage, before Wounds land: a Benny and a Vigor roll. Each success and raise soaks one Wound from that hit. Soak them all and the Shaken goes too, even an older one. Once per attack; Bennies may reroll the Vigor. Do not count this hit's Wound penalties yet.

## States

| State | Effect and recovery |
|---|---|
| **Distracted** | −2 all Trait rolls. Ends: their next turn. |
| **Vulnerable** | Others attack and act at +2 against them. Ends: their next turn. Never stacks with The Drop — take the higher. |
| **Entangled** | Cannot move; Vulnerable. Break free: Athletics, or Strength at −2. |
| **Bound** | Cannot move; Distracted and Vulnerable; no physical action but breaking free. Success → Entangled, raise → free. |
| **Fatigued** | −1 all Trait rolls. One level per hour unless the source says otherwise. |
| **Exhausted** | −2 all Trait rolls. Another level Incapacitates. |
| **Shaken** | Move and free actions only; may still Run. Spirit free at start of turn, or a Benny anytime. |
| **Stunned** | Distracted, Vulnerable, prone, no move or action, no Gang Up. Vigor free at start of turn: success ends Stunned but Vulnerable lasts to end of next turn; a raise ends it this turn. |
| **Wounds** | Each is −1 Pace (min 1″) and −1 Trait, to a maximum of −3. |
| **Incapacitated** | No actions, still dealt cards. Healing one Wound clears it. |

## Going down

Incapacitated by damage → immediate Vigor:

- **Critical Failure** → dead.
- **Failure** → Injury Table, permanent, and Bleeding Out.
- **Success** → Injury Table until every Wound heals.
- **Raise** → Injury Table for 24 hours, or until the Wounds heal.

**Bleeding Out:** Vigor at the start of each turn, or each minute outside combat. Failure kills. Success buys another roll; a raise stabilises. An ally may stabilise with a Healing action.

**Finishing Move:** a wholly helpless victim can be dispatched as an action — automatic unless you see a reason otherwise.

Roll the Injury Table as printed (p. 95); do not invent rows. Fatigue Incapacitation runs on its own track (p. 100), not this one.

## Healing

**Healing skill:** ten minutes per Wound level, **−1** without a kit. Success removes one Wound, a raise two, a Critical Failure adds one.

**Golden Hour:** one attempt per healer per patient within the first hour — a different healer may still try. After that only natural healing or the *healing* power (greater healing) works. Healing may also stabilise someone Bleeding Out, as an action.

**Natural:** Vigor every five days. Success recovers one Wound, a raise two, a Critical Failure adds one. Let allies Support that roll.

## At the table

- **Aim** — whole turn, stationary: the next first shot ignores 4 points of range, cover, Called Shot, Scale, or speed, or simply takes +2.
- **Defend** — whole turn, no extra actions, no Run: **+4** Parry until the next turn.
- **Wild Attack** — **+2** Fighting and damage; Vulnerable until the end of the *next* turn.
- **Called Shot** — limb **−2**; head or vitals **−4** for **+4** damage; the face of an open helmet **−5**, and the helmet does not count.
- **Cover** — **−2 / −4 / −6 / −8**. Where cover should have stopped a hit, it acts as Armor of that value. Prone against ranged fire at 3″+ is −4 and does not stack with cover; prone in melee is −2 Parry and −2 Fighting.
- **The Drop** — **+4** attack and damage for one action. Shaken or worse then forces Vigor or a knockout.
- **Gang Up** — **+1** Fighting per extra adjacent attacker who is not Stunned, to **+4**; each adjacent ally of the defender cancels one.
- **Grapple** — opposed Athletics. Win Entangles; a raise, or a second success, Binds. The grappler is Vulnerable while holding someone Bound. Crush is a Strength roll as damage.
- **Withdraw** — every adjacent foe who is not Shaken or Stunned gets a Free Attack.
- **Unarmed defender** — an armed melee attacker gets **+2**; does not stack with The Drop.
- **Unstable platform** — **−2** to shoot or throw from a mount or moving vehicle. **Off-hand −2** unless Ambidextrous.
- **Illumination** — Dim **−2**, Dark **−4** with nothing visible past 10″, Pitch **−6**.

Do not import Explorer-era skills, percentile helmet saves, or an inactive setting module. If the book does not settle it: `RULE UNCLEAR - GM DECISION REQUIRED`.

---

## GM — do not print

```text
Authority: SWADE Fifth Printing (2023), pp. 87–109 (Rules, Combat, Healing, Situational Rules), p. 203 (State Summaries)
Setting: none on this card
House rule: none on this card
Ruling: none
Summary: Workspace GM one-pager. Short paraphrase of core rolls, Bennies, damage, and states. PDF remains authoritative.
Applied here: any table using this workspace; adventure-specific numbers stay on that night's RUN.md / adventure GM card
```

Do not copy long rules text from the PDF onto the printed page. Do not put hydra trackers, tonight's light, or named opposition on this card — those belong to the adventure.
