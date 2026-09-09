---
node: logic.consequence.model-theoretic
title: The Model-Theoretic Account
layer: 2
state: sketch
class: anchor
parent: logic.consequence
bridges: [logic.philosophy-of-logic, logic.classical, logic.mathematics.foundations, metaphysics.modality]
pass: 2026-09-09.19
---

# The Model-Theoretic Account

Tarski's 1936 paper "On the Concept of Logical Consequence" set out to replace a modal intuition with a mathematical definition. Partition the vocabulary into logical and nonlogical terms; then a sentence X follows from a class K of sentences just in case every model of K is a model of X, where a model is an assignment to the nonlogical terms that makes the sentences true. Tarski's own version held the domain fixed and reinterpreted only the nonlogical constants; the modern definition, settled by the 1950s, varies the domain as well and treats a model as a set-theoretic structure. Its virtues the parent article names; this sketch concerns the objections that have accumulated against the analysis and the shape of its defenses.

The decisive challenge is Etchemendy's *The Concept of Logical Consequence* (1990), which turns on a distinction between two things a model might be. On **representational semantics**, a model stands in for a way the world might have been: the same sentences, the same meanings, a different world. On **interpretational semantics**, the world stays fixed and the sentences are reinterpreted: a model is a way of reassigning meanings to the nonlogical terms. Only the interpretational reading can be Tarski's, since fixing the meanings of the logical constants while varying the rest is precisely what the partition is for. But interpretational validity, Etchemendy argues, is a disguised universal generalization: an argument is declared valid when no actual reinterpretation refutes it, and there is nothing in the definition that guarantees the conclusion *cannot* be false given the premises — only that, across the interpretations there are, it never is. The definition therefore gets the right extension, when it does, for the wrong reason. Two symptoms follow. **Overgeneration**: if the universe contains only finitely many objects, then "there are at least n things" comes out logically true for the n there are; the account makes the size of the world a logical matter. **Undergeneration**: with quantifiers among the constants, sentences true in every finite domain but false in some infinite one are misclassified in the other direction. Both symptoms display the account's dependence on which constants are held fixed, a choice the definition does not justify. The modern account escapes the finitude cases only by importing set theory's inexhaustible supply of domains — which, as Etchemendy presses, means the extension of *logical* consequence is hostage to the axioms of a substantive mathematical theory, and cannot explain why validity should hold necessarily rather than merely across all sets.

The defenses fall into three families. The first is Sher's invariance response (*The Bounds of Logic*, 1991): the logical constants are not chosen arbitrarily but demarcated as those notions invariant under all bijections of the domain, so the reinterpretations the definition surveys are the formal possibilities. On this reading the generalization is not material at all; it ranges over every formally possible structure, and that is what necessity in virtue of form comes to. The second is Kreisel's squeezing argument (1967), which sidesteps the question of what the definition means and establishes only that it gets the extension right: intuitive validity implies model-theoretic validity, because a model is a genuine case in which premises are true and conclusion false; derivability implies intuitive validity, because the rules are evidently sound; completeness closes the loop, so all three coincide. Its limits are that it presupposes the soundness of the rules, that it works only where completeness holds, and that Etchemendy can grant the coincidence while denying that the definition explains it. The third family contests the reading of Tarski. Gómez-Torrente (1996) argues that Tarski's fixed-domain definition, read alongside his practice of including domain-specifying axioms, does not overgenerate; Shapiro (1998) concedes the interpretational reading but separates two tasks the definition might discharge — analyzing consequence and proving that the analysis holds — and finds a "blended" account, in which models represent possibilities *and* reinterpretations, adequate for the second. Hanson (1997) and Priest (1995) pursue variants.

Second-order logic is where the account and its rivals stop coinciding. There is no completeness theorem; the squeezing argument fails; and model-theoretic consequence in the standard (full) semantics decides the continuum hypothesis one way or another and so inherits the open questions of set theory. Whether this shows that second-order consequence is logic at its most powerful or set theory under an alias (the Quine–Boolos–Shapiro exchange, homed at `logic.classical`) is now a dispute about the analysis itself, not about a formalism.

## Children

Thin node — no natural children yet.

## Bridges

- **logic.philosophy-of-logic**: the demarcation of the logical constants, on which Sher's response and both overgeneration charges turn, is homed there.
- **logic.classical**: the second-order case and the Quine–Boolos–Shapiro dispute over whether it is logic at all.
- **logic.mathematics.foundations**: the account's set-theoretic underwriting and the sensitivity of second-order consequence to independent set-theoretic questions.
- **metaphysics.modality**: whether models can stand in for possible worlds — Etchemendy's representational reading — and what modality "cannot be false" invokes.
