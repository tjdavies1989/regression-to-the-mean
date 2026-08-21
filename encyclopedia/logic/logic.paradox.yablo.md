---
node: logic.paradox.yablo
title: Yablo's Paradox
layer: 2
state: sketch
class: satellite
parent: logic.paradox
bridges: [logic.paradox.liar, logic.paradox.formal-truth, logic.mathematics.incompleteness]
pass: 2026-08-21.2
---

# Yablo's Paradox

Consider an infinite list of sentences, one for each natural number, where each sentence says only this: *every sentence later in this list is untrue*. No sentence mentions itself. No sentence mentions a predecessor. Each looks strictly forward, at sentences that in turn look only further forward; the reference relation contains no loop of any length. Now suppose some sentence S*n* is true. Then everything after it is untrue — in particular S*n*+1. But everything after S*n*+1 is *also* untrue, since those sentences lie among S*n*'s successors; and that is exactly what S*n*+1 says, so S*n*+1 is true after all. Contradiction. So no sentence in the list is true. But then, for any *n*, all sentences after S*n* are untrue — which is precisely what S*n* says, so S*n* is true. Contradiction again. Since Yablo published the sequence in 1985 and drew the moral in 1993 — "paradox without self-reference" — it has served as the family's controlled experiment: every diagnosis that blames the liar on self-reference or circular reference must here confront a paradox that apparently runs without either.

The live dispute is whether the appearance survives scrutiny. Priest argues it does not. The contradiction is not derived sentence by sentence but by a general argument about an arbitrary S*n*, and that argument needs the sentences given uniformly, by a schema — S*x* says that for all *k* > *x*, S*k* is not true — whose satisfaction conditions involve the very predicate being characterized. The circularity is real but relocated: not in any sentence, but in the fixed-point predicate that generates the list, exactly the kind of fixed point the diagonal lemma delivers for the liar. (Beall presses the companion point: try to pick out the infinite list without such a schema, and you cannot.) The position's strength is that the *paradoxical reasoning*, as opposed to the paradoxical feeling, demonstrably routes through the self-applicable schema. Sorensen and Yablo reply that the sentences alone carry the paradox: the list exists whether or not we describe it uniformly, a being with infinite patience could assert each sentence separately, and circularity in our finite means of access is a fact about us, not about the sequence. Their strength is the bare structure: no cycles anywhere, yet contradiction — so what powers the semantic paradoxes is plausibly not circularity but *ungroundedness*, reference chains that never bottom out, a diagnosis (developed by Leitgeb and Cook) under which liar and Yablo are the looped and unlooped cases of one disease. Cook's generalization sharpens the challenge: standard paradoxes can be systematically "unwound" into Yablo-style infinite sequences, and if unwinding preserves paradox while deleting circularity, circularity was never the operative feature.

A third angle cuts underneath the dispute. Formalize the sequence in arithmetic with a truth predicate and local disquotation for each Yablo sentence, and the resulting theory is not inconsistent at all — it is ω-inconsistent (Ketland; Barrio). Every finite initial segment is satisfiable; indeed the whole first-order theory has models, just no standard one: nothing explodes until the infinite totality is taken at standard face value, via an ω-rule or a uniform satisfaction principle (with genuinely uniform disquotation, inconsistency does return). On this view Yablo's discovery is not quite a paradox but a new species of semantic pathology — consistency purchased at the price of the natural numbers — which links it to the ω-inconsistency that McGee exposed in seemingly innocent truth theories, and reopens the question of what, exactly, a solution to it would even owe us.

## Children

Thin node — no natural children yet.

## Bridges

- **logic.paradox.liar**: the control case — if Yablo is genuinely non-circular, diagnoses of the liar that blame self-reference are treating a symptom, and ungroundedness is the better name for the disease.
- **logic.paradox.formal-truth**: in Kripke's construction every Yablo sentence is ungrounded despite referring to nothing circularly; the ω-inconsistency results live in the axiomatic theories' scorecard.
- **logic.mathematics.incompleteness**: the diagonal lemma supplies the fixed-point schema on which Priest's circularity charge turns, and ω-inconsistency and nonstandard models are that node's stock in trade.
