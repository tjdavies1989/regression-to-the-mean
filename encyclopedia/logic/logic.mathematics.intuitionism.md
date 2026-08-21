---
node: logic.mathematics.intuitionism
title: Intuitionism and Constructivism
layer: 2
state: sketch
class: standard
parent: logic.mathematics
bridges: [logic.nonclassical.intuitionistic, logic.mathematical, language, epistemology]
pass: 2026-08-21.1
---

# Intuitionism and Constructivism

A classical mathematician can prove that a number with a certain property exists by showing that its nonexistence leads to contradiction — and finish the proof unable to name any such number, or say where to look. The constructivist finds this not merely inelegant but empty: an existence claim is redeemed only by a construction, an actual instance with a method for producing it. The culprit, on this diagnosis, is the law of excluded middle. For a finite collection, "either some element is F or none is" is backed by a procedure — check each. Applied to an infinite totality, the same disjunction asserts the outcome of a search that cannot be completed; classical logic, Brouwer charged, is the logic of finite situations illegitimately extrapolated to the infinite, treating the never-finished as finished.

Brouwer's intuitionism derives this critique from a philosophy of mind. Mathematics is not a body of truths about independent objects, nor a play of symbols, but a *mental construction*: the languageless activity of a creating subject, generated from the primordial intuition of two-ity — the falling apart of a moment of life into what was and what is. Objects exist exactly insofar as they have been constructed; a statement is true when a construction warrants it, and until one of a pair of constructions exists, neither the statement nor its negation holds. The consequences are not only subtractive. Choice sequences — infinite sequences generated freely over time, never complete — yield theorems classically false, most famously that every total function on the reals is continuous. Intuitionistic mathematics is not classical mathematics minus; it is a different subject.

Brouwer distrusted formalization, but his student Heyting supplied it: intuitionistic logic as a codified system, interpreted by the Brouwer–Heyting–Kolmogorov reading on which each connective is explained by what counts as a proof of it — a proof of "A or B" is a proof of one of them, identified; a proof of "if A then B" is a method transforming any proof of A into a proof of B. Decades later Dummett reached the same logic by an independent, semantic route. Meaning, he argued, must be exhaustively manifestable in use; a grasp of verification-transcendent truth-conditions could be neither acquired nor displayed; so the meaning of a mathematical statement can only be its proof-conditions — and a proof-conditional semantics validates intuitionistic, not classical, logic. If the argument works, revisionism follows from the theory of meaning alone, with no debt to Brouwer's solitary constructing mind.

Bishop's *Foundations of Constructive Analysis* (1967) detached the practice from every such ideology. Bishop rebuilt analysis constructively without choice sequences or antirealist polemic, so that each theorem is classically true but carries its numerical content on its face; the Russian school of Markov added a recursive reading. The price of constructivism is real — trichotomy for the reals, unrestricted intermediate value theorems, and much of set-theoretic mathematics are lost or hold only in weakened forms. But the products have proved permanent. A constructive proof is an algorithm; the Curry–Howard correspondence makes this literal, identifying proofs with programs and propositions with types, so that intuitionistic logic now thrives as the working logic of computer science, type theory, and the internal language of topoi — vindicated, ironically, on grounds Brouwer would have disowned.

## Children

- `brouwer` — **Brouwer's Program** — The creating subject, choice sequences, bar induction, and the continuity theorems: intuitionistic mathematics as a positive alternative, not a restriction. *(standard)*
- `meaning-theoretic` — **The Meaning-Theoretic Argument** — Dummett's manifestation and acquisition challenges, proof-theoretic semantics after Prawitz, and whether the case for revising logic succeeds. *(standard)*
- `bishop` — **Constructivism after Bishop** — Bishop-style analysis, the Markov school, Martin-Löf type theory, and constructive reverse mathematics as a comparative science of systems. *(standard)*

## Bridges

- **`logic.nonclassical.intuitionistic`**: the logic itself — semantics, metatheory, relations to classical logic — lives there; this node houses the mathematical and philosophical motivations that produced it.
- **`logic.mathematical`**: the Curry–Howard correspondence and realizability belong to proof theory's technical repertoire; this node interprets their philosophical weight.
- **Language**: Dummett's route runs through the theory of meaning — manifestation, verificationism, antirealism — and stands or falls with debates housed there.
- **Epistemology**: constructivism is an epistemic constraint on mathematical truth; its quarrel with platonism is a local form of the realism–antirealism dispute about truth and evidence.
