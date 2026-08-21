---
node: logic.mathematics.practice
title: Philosophy of Mathematical Practice
layer: 2
state: sketch
class: standard
parent: logic.mathematics
bridges: [epistemology, science, mind]
pass: 2026-08-21.1
---

# Philosophy of Mathematical Practice

Foundational philosophy of mathematics treats the subject as a finished edifice: a body of theorems awaiting an ontology and an epistemology. But mathematicians do not experience their subject that way. They distinguish proofs that *explain* from proofs that merely certify; they call some theorems deep and some definitions natural; they praise a proof of a number-theoretic result that stays within number theory and feel vaguely that Wiles's detour through elliptic curves, whatever its glory, proves Fermat's theorem without showing *why* it holds. None of these distinctions is visible from the foundational standpoint — every valid proof is equally a proof — yet working mathematicians stake careers on them. The philosophy of mathematical practice takes these appearances seriously as data. Its founding document is Lakatos's *Proofs and Refutations* (1976), which dramatized the history of Euler's polyhedron formula as a dialectic of proof, counterexample, and concept-refinement, and argued that mathematical knowledge grows by this dialectic rather than by deduction from secure axioms.

The field's core problems have each acquired a literature. **Mathematical explanation**: Steiner located explanatoriness in a proof's deployment of a characterizing property; Kitcher in unification; Lange, most influentially now, in symmetry and salient unity — while skeptics reply that "explanatory" tracks nothing more than shifting standards of taste. The strongest evidence that something objective is at stake is behavioral: mathematicians re-prove known theorems, and journals publish the re-provings, which makes no sense if verification were the whole game. **Purity of methods**, from Aristotle through Hilbert to Detlefsen and Arana, asks when a proof draws only on what the theorem is "about," and whether purity is an epistemic virtue or an aesthetic one; the Erdős-style elementary proof of the prime number theorem is the standard case study. **Depth and naturalness** are the field's frontier and its methodological test: either philosophy can say what makes the Langlands program deep and the definition of a group natural, or these are sociological facts about prestige — and the discipline's claim to be more than commentary rides on the answer.

**Diagrams** were expelled from proof by the nineteenth-century rigorization — Pasch's dictum that a proof must not depend on the figure — and rehabilitated a century later: Manders's analysis of the *Elements* showed Euclid's diagram use to be rule-governed and rigorous, tracking exactly the diagram's stable ("co-exact") features, and formal systems by Mumma and others vindicate the practice. The live question is whether visualization merely aids discovery or can constitute justification — Giaquinto argues carefully for the latter, within limits.

**Computer-assisted proof** posed the field's sharpest epistemological jolt. Appel and Haken's 1976 proof of the four-color theorem was checkable by no human; Tymoczko argued this made mathematics a posteriori and quasi-empirical, importing testimony and instrument-trust into the one discipline thought free of them. Formal verification answered rather than deepened the worry: the Flyspeck project machine-checked Hales's proof of the Kepler conjecture down to the axioms, arguably yielding *more* certainty than referees provide. Machine-generated mathematics now reopens every question at once — proofs found by search or by language models, correct but perhaps permanently unexplanatory, force the field to say whether understanding, and not mere truth, is something mathematics can be obligated to produce.

## Children

- `explanation` — **Mathematical Explanation** — Why some proofs explain while others only verify: characterizing properties, unification, Lange's symmetries, and the skeptical dissent. *(standard)*
- `purity` — **Purity, Depth, and Mathematical Virtues** — When a proof should stay on its own topic, and whether depth and naturalness are discoveries or reputations. *(satellite)*
- `diagrams` — **Diagrammatic Reasoning** — From Pasch's ban to Manders's Euclid: whether the figure can carry justificatory weight. *(satellite)*
- `computerproof` — **Computer-Assisted and Machine-Generated Proof** — Four-color, Flyspeck, and formal verification; what surveyability, testimony, and AI-found proofs do to mathematical knowledge. *(standard)*

## Bridges

- **Epistemology**: surveyability, testimony, and instrument-trust in computer proof import the general theory of evidence into mathematics; understanding versus knowledge is joint property.
- **Science**: the mathematical-explanation literature runs on rails laid by scientific explanation — and repays the debt in the enhanced indispensability argument treated in `logic.mathematics.ontology`.
- **Mind**: visualization and diagram use tie proof to theories of perception and mental representation; machine-generated mathematics ties it to machine cognition.
- **Within logic**: `logic.mathematics.foundations` is the counterpoint — univalent foundations is itself a practice-driven reform of foundations.
