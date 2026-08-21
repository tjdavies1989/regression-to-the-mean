---
node: logic.paradox.set-paradoxes
title: The Set-Theoretic Paradoxes
layer: 2
state: sketch
class: standard
parent: logic.paradox
bridges: [logic.mathematics.foundations, logic.mathematics.logicism, metaphysics, logic.paradox.liar]
pass: 2026-08-21.2
---

# The Set-Theoretic Paradoxes

Naive comprehension does not look like a theory. It looks like a definition: for any condition, there is a set of exactly the things satisfying it — what else could "set" mean? Russell's paradox refutes it in two lines. Take the condition "is not a member of itself" and ask whether its set belongs to itself: if it does, it doesn't; if it doesn't, it does. Nor is Russell's set an isolated freak. Burali-Forti had already found trouble at the top of the ordinals: the set of all ordinals would be well-ordered, hence would have an ordinal — one greater than every ordinal, itself included. Cantor found the same cliff among the cardinals: the set of everything would be at least as big as any set, yet his own theorem makes its power set bigger. The three are one family, each a totality together with an operation that manufactures a member the totality cannot contain. What fell was not a technical conjecture but something that had passed for analytic; the paradoxes are the standing proof that self-evidence is not a safe-conduct.

Two diagnoses divide the aftermath. **Limitation of size** — Cantor's instinct, sharpened by von Neumann — blames bigness: a collection goes wrong exactly when it is as large as everything, so the guilty parties (all sets, all ordinals) fail sethood for the same reason, and the axiom of replacement falls out as a bonus. Its weakness is that it names the symptom: why should *size*, of all things, be what membership cannot survive? The **iterative conception** answers with a picture instead of a threshold: sets are formed in stages, each from elements already available, and the cumulative hierarchy never completes. The Russell set never forms because no stage contains all sets. Boolos's defense is the load-bearing text: the conception is not an ad hoc fence thrown up around the paradoxes but an independently natural idea from which most of the Zermelo axioms simply follow. His honesty is equally load-bearing: iteration does not deliver replacement or choice, limitation of size does not deliver power set, and Boolos concluded that set theory rests on two heuristics, neither reducible to the other — a settlement, not a solution.

Dummett's diagnosis cuts deeper than both. Some concepts — *set*, *ordinal*, *interpretation* — are **indefinitely extensible**: any definite totality of their instances immediately generates a further instance outside it. If so, the paradoxes are not accidents of a bad axiom but the signature of concepts that cannot be totalized, and the casualty is quantification itself. Hence the absolute-generality debate: Williamson argues that unrestricted quantification must be coherent, since even the relativist needs it to state her own thesis — "every domain can be extended" quantifies over what, exactly? — while relativists from Parsons to Fine and Linnebo reply that the hierarchy's endless extendability is a datum, not an appearance, and rebuild generality as modal or schematic. Each side's best argument is the other's self-undermining.

Priest's inclosure schema then bids for everything: one form — a totality, an operation that transcends it yet stays within it, contradiction at the limit — instantiated alike by Russell, Burali-Forti, the liar, and Berry. The stakes are Ramsey's old partition of the paradoxes into logical and semantical, which for a century licensed separate cures; if the schema is right, the partition is superficial and the principle of uniform solution demands one remedy — Priest's candidate being dialetheism. Whether the schema is depth or numerology is adjudicated at the parent; what this node owes it is the set-theoretic half of the evidence.

## Children

- `iterative-conception` — **The Iterative Conception of Set** — Boolos's defense, the division of labor with limitation of size, and Linnebo's potentialist reworking of stage-talk. *(standard)*
- `absolute-generality` — **Absolute Generality** — Whether quantification over absolutely everything is coherent: Williamson's absolutism against relativism, and the relativist's self-statement problem. *(standard)*

## Bridges

- **logic.mathematics.foundations**: ZFC is the post-paradox settlement; whether the iterative conception justifies its axioms or merely rationalizes them is the live wire between the two nodes.
- **logic.mathematics.logicism**: Russell's letter felled Basic Law V, and the bad-company problem is the paradoxes recurring inside neo-Fregean abstraction.
- **metaphysics**: indefinite extensibility and absolute generality are questions about quantification and ontology, not notation; potentialism imports modality into the hierarchy itself.
- **logic.paradox.liar**: the inclosure schema stakes the unity claim that binds this family to the semantic one, against Ramsey's partition.
