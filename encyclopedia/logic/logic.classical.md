---
node: logic.classical
title: Classical Logic
layer: 1
state: sketch
class: standard
parent: logic
bridges: [language, metaphysics, epistemology]
pass: 2026-08-21.1
---

# Classical Logic

For most of its history, logic was a catalogue: the syllogistic here, the Stoic inference schemes there, with no single system embracing them all. Frege's *Begriffsschrift* (1879) changed that. Treat sentences as built from atomic parts by a handful of connectives — "not," "and," "or," "if" — and, crucially, analyze generality with quantifiers binding variables ("for all x," "there is an x"), and one system suddenly captures both the old patterns and the reasoning of working mathematics, including the multiply general sentences ("every number has some successor") that had defeated the syllogistic for two millennia. Propositional logic and its extension, first-order logic, are the result: the *classical* system, so called because it has become the default — the logic students learn first, the logic against which every rival defines itself. Its distinctive commitments are bivalence (every statement is true or false), the law of excluded middle, and a negation that takes each truth value to the other. Whether these commitments are truths or merely useful idealizations is the business of the nonclassical rivals; this entry concerns what the classical system is and what its study revealed.

The revelation came through metatheory — stepping outside the system to prove things *about* it. Two properties anchor everything. Soundness: the proof rules never lead from truths to a falsehood. Completeness, proved by Gödel in 1930: every argument valid on the model-theoretic definition of consequence is provable by the rules. Together they show that two independently motivated notions — following-from as truth-preservation across all interpretations, and following-from as derivability — coincide exactly for first-order logic. This is the strongest evidence we possess that the classical analysis of consequence carves at a joint.

But the metatheory gives with one hand and takes with the other. Completeness yields compactness — if every finite subset of a theory has a model, so does the whole — and compactness generates nonstandard models: no first-order theory can pin down the natural numbers uniquely. The Löwenheim–Skolem theorems deepen the embarrassment: any first-order theory with an infinite model has models of every infinite size, so even "uncountable" gets reinterpreted in a countable model (Skolem's paradox). Skeptics have pressed these results hard — Skolem toward relativism about set-theoretic notions, Putnam toward his model-theoretic argument that reference itself is radically indeterminate. Whether the skepticism is coherent (can one even state it without using the notions it undermines?) remains disputed.

There is an escape: second-order logic, which quantifies not just over objects but over properties or sets of them, restores categoricity — arithmetic and analysis get unique descriptions. The price is steep: by Gödel's incompleteness results, second-order consequence outruns every possible proof procedure. Quine drew the moral that second-order "logic" is really mathematics — "set theory in sheep's clothing" — smuggling substantive ontology into what should be topic-neutral. Defenders answer variously: Boolos read second-order quantification as ontologically innocent plural quantification ("there are some sets such that…"); Shapiro argues that only second-order resources let logic serve mathematical practice, and that a completeness-proof requirement begs the question against them. The dispute is less about a formalism than about what logic is *for* — and so feeds directly into the monism and demarcation debates housed under philosophy of logic.

## Children

- `second-order` — **Second-Order Logic** — Quantification over properties and sets: the categoricity gains, the incompleteness costs, and the Quine–Boolos–Shapiro dispute over whether it is logic at all. *(standard)*
- `skolem` — **The Skolem Paradox** — Countable models of "uncountable" set theory, and the skeptical arguments — Skolem's relativism, Putnam's model-theoretic argument — built on Löwenheim–Skolem. *(satellite)*

## Bridges

- **Language**: first-order regimentation is Quine's "canonical notation" for serious discourse; the fit (and misfit) between quantifiers, conditionals, and their natural-language counterparts is joint property with semantics.
- **Metaphysics**: "to be is to be the value of a variable" makes the first-order apparatus the standard instrument of ontological commitment; the second-order dispute is partly a dispute about the ontology of properties.
- **Epistemology**: the Skolemite and Putnamian arguments turn model theory into an engine of skepticism about reference and realism.
- **Within logic**: the metatheory's technical home is the mathematical-logic cluster; the demarcation question ("is second-order logic logic?") belongs finally to philosophy of logic.
