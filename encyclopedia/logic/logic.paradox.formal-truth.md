---
node: logic.paradox.formal-truth
title: Formal Theories of Truth
layer: 2
state: sketch
class: anchor
parent: logic.paradox
bridges: [language.truth, logic.mathematical, logic.mathematics.incompleteness]
pass: 2026-08-21.2
---

# Formal Theories of Truth

The parent article diagnosed the liar; this node collects the cures, stated with enough precision to be billed. The task: a theory of a predicate T for which T("A") and A are equivalent, in a language rich enough to build the liar — saying exactly what the theory proves, what it cannot say, and what it costs. Here costs are measured, in expressive power and, increasingly, in proof-theoretic strength.

Tarski's hierarchy is remembered as a moral — "ascend to the metalanguage" — but it is first a theory, and the only one here that *defines* truth outright. Convention T fixes adequacy: a definition must entail every biconditional "*A*" is true iff *A*. Tarski then delivers one, by recursion through satisfaction, for any object language not containing the predicate being defined; his indefinability theorem shows the restriction is forced — a classical language defining its own truth proves the liar. The strength of the view is that within each level nothing is revised: classical logic, full compositionality, truth eliminable by definition. The hierarchy's descendants (Burge, Glanzberg) make the levels contextual and shifting rather than fixed, to soften the parent article's complaint about natural language.

Kripke kept one self-applied predicate by letting truth be partial and *grounded*. Start with T empty; the jump operator declares true whatever sentences already come out true under the current partial interpretation (evaluated in Strong Kleene logic), false whatever come out false. The operator is monotone, so transfinite iteration closes off at fixed points; in the minimal fixed point a sentence has a value just when asking "is it true?" bottoms out in the world — the grounded sentences. The liar is simply never reached. The confession comes at the end: "the liar is ungrounded" is true, and inexpressible in the object language; groundedness and the fixed point are described in a classical metalanguage. Kripke said it himself — the ghost of the Tarski hierarchy is still with us.

The axiomatic turn (Feferman, Friedman–Sheard, Cantini, Halbach) stops defining truth and takes it as primitive: add axioms for T to arithmetic and measure the result. Typed theories: TB, the Tarski biconditionals for truth-free sentences, is conservative over PA — it proves nothing new about numbers; CT, compositional axioms with truth allowed into induction, proves Con(PA). Type-free: FS keeps full classical symmetry between A and T("A") at the price of ω-inconsistency; KF axiomatizes Kripke's fixed points inside classical logic, is far stronger than CT, and proves the liar sentence while proving it is not true — the external theory outrunning its internal notion; VF does the same for supervaluational fixed points, stronger again. Conservativeness is where deflationism is scored: if truth is thin, a device for generalization, adding it should prove nothing new — TB obliges, CT does not, and Shapiro and Ketland press the point as an argument that truth is substantial. Deflationists reply that the strength comes from extending induction, not from truth.

The revision theory (Gupta–Belnap) holds that truth is a *circular* concept and that circular concepts are respectable: governed not by fixed points but by revision. Hypothesize any extension for T; revise it by the biconditionals used as a rule; iterate. Grounded sentences stabilize; the liar oscillates forever — instability is its signature, explained rather than silenced, with classical logic untouched. The costs are contested limit rules and staggering computational complexity.

## Children

- `tarski-hierarchy` — **Tarski's Definition and Hierarchy** — Convention T, truth via satisfaction, the indefinability theorem, and the contextualist hierarchies of Burge and Glanzberg. *(standard)*
- `kripke` — **Kripke's Theory of Truth** — Grounding, the jump operator, the lattice of fixed points, choice of evaluation scheme, and the metalanguage problem. *(standard)*
- `axiomatic` — **Axiomatic Theories of Truth** — TB, CT, KF, FS, and VF as formal systems; proof-theoretic strength as the measure of a truth theory. *(standard)*
- `conservativeness` — **Conservativeness and Deflationism** — The Shapiro–Ketland argument that non-conservative truth is substantial, and the deflationist replies. *(satellite)*
- `revision` — **The Revision Theory of Truth** — Gupta and Belnap on circular concepts: revision sequences, stability, and the limit-rule disputes. *(standard)*

## Bridges

- **language.truth**: the nature-of-truth debate is homed there, but its deflationist wing is refereed here — conservativeness results are the formal battlefield for whether truth is "thin."
- **logic.mathematics.incompleteness**: Tarski's indefinability theorem is Gödel's diagonalization turned on semantics, and the axiomatic theories are calibrated against arithmetic.
- **logic.mathematical**: fixed-point constructions, ordinal analysis, and ω-models — the machinery of this node is working mathematical logic.
- **Within logic**: the sibling `liar` node owns revenge, the test all these theories face; the nonclassical escapes (Field, Priest) are homed at `logic.nonclassical`.
