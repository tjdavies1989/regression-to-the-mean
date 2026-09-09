---
node: logic.consequence.abstract-consequence
title: Consequence Relations
layer: 2
state: sketch
class: satellite
parent: logic.consequence
bridges: [logic.nonclassical, logic.paradox.curry, logic.consequence.proof-theoretic, logic.philosophy-of-logic]
pass: 2026-09-09.19
---

# Consequence Relations

Before Tarski asked what consequence *is*, he asked what any consequence relation must *look like*. His 1930 papers define a consequence operation Cn on sets of sentences by three postulates: every set is contained in its closure (reflexivity), closing twice adds nothing (idempotence, the operator form of transitivity), and larger sets have larger closures (monotonicity), with a fourth, finitariness, requiring that whatever follows from a set follows from some finite subset. Nothing here mentions connectives, models, or proofs; a consequence operation is simply a closure operator on sentences, and a "logic" is a pair of a language and such an operator. Łoś and Suszko (1958) added structurality — closure under uniform substitution — which is formality reduced to an algebraic condition, and Scott (1974) recast the operator as a relation Γ ⊢ A satisfying identity, weakening, and cut. The abstraction is the point: the model-theoretic and proof-theoretic accounts are two ways of *generating* relations that meet these conditions, and the conditions themselves can be studied, and questioned, independently of either.

Questioning them is the field's modern shape, and each postulate has a literature devoted to its absence. Drop monotonicity and one obtains the nonmonotonic consequence relations of default and defeasible reasoning, where "Tweety flies" follows from "Tweety is a bird" but not from that together with "Tweety is a penguin"; Kraus, Lehmann, and Magidor's cumulative and preferential systems, and Makinson's bridges from classical to nonmonotonic consequence, replace monotonicity with weaker principles such as cautious monotony, and the debate over which weakening is principled rather than convenient is unfinished. Drop transitivity and consequence ceases to chain: Ripley's strict–tolerant logic validates every classically valid inference and the naive truth rules while failing cut, so that the derivation of triviality in Curry's paradox breaks at the step that composes two valid pieces. The cost, pressed by critics, is that a relation that does not compose seems to lose the very feature that makes it *consequence* rather than a list of licensed transitions. Drop reflexivity and the tolerant–strict dual and Malinowski's q-consequence appear, relations in which a premise need not follow from itself; they have few adherents but sharpen the question of which postulates are constitutive and which merely customary.

The substructural rules come into view only when Tarski's premise sets are replaced by Gentzen's sequences or multisets. Sets already build in **contraction** (a premise used twice counts once) and **exchange** (order is irrelevant); making them explicit rules that can be refused yields the substructural map. Refusing weakening gives relevance logic, whose consequence relation forbids idle premises; refusing contraction gives Girard's linear and affine logics, in which premises are resources consumed by use, and the noncontractive theories of truth (Zardini) that block Curry without touching the conditional; refusing exchange gives Lambek's calculus, where premises have grammatical order. Restall (2000) and Paoli (2002) organize the terrain, and its philosophical lesson is that the nonclassical logics differ at least as much in their structural assumptions as in their treatment of connectives — a fact invisible so long as consequence was assumed Tarskian.

**Multiple conclusions.** Shoesmith and Smiley (1978) developed a relation Γ ⊢ Δ read as "if all of Γ, then some of Δ," generalizing Gentzen's sequents into a full theory. Its strongest argument is Carnap's 1943 categoricity problem: the single-conclusion rules of classical logic admit non-normal interpretations — valuations under which negation misbehaves, or every sentence is true — so that single-conclusion consequence does not fix classical meanings, whereas multiple-conclusion consequence does. Scott's completeness theorem generalizes this: any relation satisfying identity, weakening, and cut in multiple-conclusion form is exactly the relation of truth-preservation over some class of bivalent valuations. The objection, Dummett's and Steinberger's, that no speech act corresponds to asserting "one of Δ," meets Restall's reply that Γ ⊢ Δ records the incoherence of asserting all of Γ while denying all of Δ — a reading that ties multiple-conclusion consequence to bilateralism.

The newest dispute concerns whether inferences alone individuate a logic. Since strict–tolerant logic agrees with classical logic on every inference and disagrees on metainferences (cut itself), Dicher and Paoli argue it *is* classical logic under a nonstandard notion of consequence, while Barrio, Pailos, and Da Ré construct hierarchies of logics that agree ever higher up before diverging, suggesting that a logic is its entire tower of metainferential commitments. **Abstract algebraic logic** (Blok and Pigozzi 1989; Font 2016) is the mathematical descendant of Tarski's abstraction: it classifies consequence relations by how well they can be given an algebraic semantics, and its Leibniz hierarchy — protoalgebraic, equivalential, algebraizable — is the most developed answer to which structural features of a relation determine what kind of semantics it can have.

## Children

Thin node — no natural children yet.

## Bridges

- **logic.nonclassical**: the substructural logics are homed there as systems; here they appear as the coordinates of the map, each defined by which structural rule it refuses.
- **logic.paradox.curry**: noncontractive and nontransitive consequence earn their keep against Curry; the choice of which postulate to drop is decided by that paradox above all.
- **logic.consequence.proof-theoretic**: Belnap's point that connectives are defined only against a background consequence relation, and the multiple-conclusion defense of classical harmony, both presuppose the structural analysis given here.
- **logic.philosophy-of-logic**: whether a logic is identified by its inferences or its metainferences bears directly on what monism and pluralism are disagreeing about.
