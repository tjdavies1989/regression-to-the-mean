---
node: logic.modal
title: Modal and Intensional Logic
layer: 1
state: sketch
class: anchor
parent: logic
bridges: [metaphysics.modality, language, epistemology, ethics]
pass: 2026-08-21.1
---

# Modal and Intensional Logic

Classical logic is blind to a distinction any child can draw: between what is and what must be. "2+2=4" and "there are eight planets" are both true, but only the first could not have been otherwise. Add an operator for "necessarily" and its dual "possibly" and you have modal logic — and an immediate embarrassment: whether "necessarily P" is true does not depend only on whether P is true. Such contexts are *intensional* — substituting one truth for another inside them can breed falsehood — and the question is what modal truth does depend on.

For half a century there were only competing axiom systems. The minimal system K says necessity distributes over implication; T adds that what is necessary is actual; S4 that what is necessary is necessarily necessary; S5 that what is possible is necessarily possible. Which is *correct* seemed undecidable — until Kripke's relational semantics turned the axioms into pictures. Interpret "necessarily P" as "P is true in every accessible possible world," and each system corresponds to a condition on accessibility: T to reflexivity, S4 to transitivity, S5 to its collapse into universality. This correspondence is the field's great success: an apparently metaphysical dispute becomes a precise question about the structure of relative possibility, and different modalities plausibly get different structures — metaphysical necessity is widely held to be S5; provability, by Gödel–Löb, demonstrably is not.

The trouble begins with quantifiers. "Nine is necessarily greater than seven" seems true; "the number of planets is necessarily greater than seven" false — yet these name the same object. Quine pressed this into an indictment: quantifying into modal contexts requires objects to have some properties necessarily *in themselves*, however described, an "invidious essentialism" he took as a reductio of the enterprise. The reply that prevailed — Kripke's — embraced the essentialism: names are rigid designators, tracking one object across worlds, and objects really do have essential and accidental properties. Quantified modal logic still forces choices classical logic never faced: the Barcan formulas, merely possible objects, world-relative domains. And behind the semantics stands an unpaid ontological bill — are possible worlds concrete universes (Lewis), abstract ersatz constructions, or useful fictions? The formalism runs the same either way, which is why the question cannot resolve itself here (bridge: `metaphysics.modality`).

Necessity, meanwhile, is only the flagship of a fleet. Read the box as "it is known that" and you have epistemic logic, with contested axioms of its own (do we know what we know?); as "it is obligatory that," deontic logic, haunted by paradoxes; as "it will always be that," temporal logic. Each reading inherits the Kripke machinery and bends it. Counterfactuals resist even that machinery: "if the match had been struck, it would have lit" is no strict conditional, since strengthening its antecedent can flip it. The Lewis–Stalnaker analysis — true if the consequent holds at the *closest* antecedent-worlds — made similarity among worlds do the work, and conditional logic a discipline of its own. At the far edge, hyperintensional phenomena — necessarily equivalent contents that still differ in meaning — suggest even possible worlds are too coarse a sieve.

## Children

- `systems` — **The Modal Systems and Kripke Semantics** — K, T, S4, S5 and the correspondence of axioms with frame conditions; completeness, canonical models, provability logic. *(standard)*
- `quantified` — **Quantified Modal Logic** — Quantifying into modal contexts: Quine's objections, rigid designation, the Barcan formulas, variable domains. *(anchor)*
- `epistemic` — **Epistemic and Doxastic Logic** — Logics of knowledge and belief, the introspection axioms, common knowledge, and the problem of logical omniscience. *(standard)*
- `deontic` — **Deontic Logic** — The logic of obligation and permission, its standard system, and the paradoxes (Ross, Chisholm) that beset it. *(standard)*
- `temporal` — **Temporal Logic** — Tense operators from Prior onward, branching versus linear time, and future contingents. *(standard)*
- `conditionals` — **Counterfactuals and Conditional Logic** — The Lewis–Stalnaker similarity semantics, its rivals, and indicative versus subjunctive conditionals. *(anchor)*
- `hyperintensionality` — **Hyperintensionality** — Distinctions finer than necessary equivalence: impossible worlds, structured propositions, and truthmaker semantics. *(satellite)*

## Bridges

- **Metaphysics (`metaphysics.modality`)**: the busiest single crossing in the corpus — possible worlds, essentialism, and de re necessity are one debate seen from two sides: the formalism here, the ontology there.
- **Language**: rigid designation, the necessary a posteriori, and intensional semantics are joint property with theories of reference; Montague built natural-language semantics directly on intensional logic.
- **Epistemology**: epistemic logic formalizes knowledge and exports puzzles back — logical omniscience, the KK principle, Fitch's paradox of knowability.
- **Ethics**: deontic logic is the formal wing of the theory of obligation; its paradoxes are data for normative theory.
