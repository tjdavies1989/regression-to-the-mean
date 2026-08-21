---
node: logic.paradox.curry
title: Curry's Paradox
layer: 2
state: sketch
class: standard
parent: logic.paradox
bridges: [logic.nonclassical, logic.mathematics.incompleteness, logic.paradox.liar, logic.consequence]
pass: 2026-08-21.2
---

# Curry's Paradox

Let C be the sentence "if C is true, then everything is true." Suppose C is true. Then what it says holds: if C is true, everything is true. But we supposed C is true — so everything is true. Now discharge the supposition. We have proved outright: *if C is true, then everything is true*. That is word for word what C says, so C is true; and now, by modus ponens, everything is true.

Inventory the tools. The truth schema, in both directions. Conditional proof: derive B from the supposition A, conclude "if A then B." Modus ponens. And one move so quiet it takes effort to notice: inside the conditional proof, the supposition "C is true" was used *twice* — once to unlock the conditional, once to feed it — and discharged once. That reuse is **contraction**. Nothing else. In particular, no negation: no "false," no "not," no excluded middle, no reductio. This is what makes Curry the referee of the field. The gap theorist tamed the liar by refusing it a truth value; the glut theorist by letting it be true and false at once. Both therapies treat negation, and Curry contains none to treat: the derivation only ever needed to *suppose* C true and watch the conditional detach. Field must therefore engineer a conditional for which conditional proof plus contraction fails; Priest's dialetheism, built to absorb contradictions, must likewise refuse a contraction-valid detachable conditional, since Curry delivers not a contradiction but everything. Solutions to the liar are graded pass/fail against Curry, and the first generation mostly fails.

The clean diagnosis blames contraction itself — not a connective but a structural rule about reusing premises — and moves to a substructural logic where a premise, once spent, is spent. Its strength is uniformity: one rule, every Curry, no connective blamed. Its cost is that contraction is everywhere: ordinary reasoning, and mathematical induction above all, lean on reusing what one has, and noncontractive theories (Zardini's is the most developed) struggle to recapture arithmetic without smuggling contraction back. Ripley instead keeps contraction and drops transitivity of consequence — the little derivations no longer chain — at the price of a consequence relation that does not compose.

The modern sharpening is **validity Curry** (Beall and Murzi): an argument saying of itself, in effect, "this very argument validly yields absurdity." Run the reasoning with "valid" in place of "true" and the operative rules are no longer anyone's pet conditional but the behavior of validity itself — roughly, that valid arguments may be used, and that what is derived is validly derived. A theorist who fixed the conditional has fixed nothing here; the paradox has moved into the metatheory, where the only things left to blame are structural rules. v-Curry is the strongest argument that the substructural response is not one option among many but where the dialectic was always headed.

And yet the very same reasoning, run on "provable" instead of "true," is a celebrated theorem. Löb's sentence — "if this sentence is provable, then A" — yields, by Curry's steps formalized in arithmetic, that if a theory proves "if A is provable then A," it proves A. No disaster follows, because provability refuses the truth schema's downward half: reflection, "if provable then true," is exactly what Gödel's second incompleteness theorem withholds. The parallel is evidence that the derivation is beyond reproach and that paradox lives entirely in the bridge principles a predicate obeys: one diagonal argument, catastrophe for naive truth, theorem for provability. Curry, on this view, is not about negation, nor even about truth — it is a fact about what any self-applicable predicate with full detachment must forfeit.

## Children

- `v-curry` — **Validity Curry** — The Beall–Murzi paradox of naive validity, and the debate over whether it forces substructural revision or admits a hierarchical or restricted-detachment escape. *(satellite)*

## Bridges

- **logic.nonclassical**: the substructural logics are homed there as systems; here they appear as the diagnosis Curry extracts — contraction-free and nontransitive consequence earn their philosophical keep against this paradox above all.
- **logic.mathematics.incompleteness**: Löb's theorem is Curry's reasoning domesticated by arithmetic; the comparison between naive truth and formal provability is load-bearing in both directions.
- **logic.paradox.liar**: Curry is the liar's negation-free shadow — every classification-based solution surveyed there must be re-audited against a paradox its vocabulary cannot see.
- **logic.consequence**: v-Curry makes the nature of validity and the status of structural rules a matter of paradox, not merely of bookkeeping.
