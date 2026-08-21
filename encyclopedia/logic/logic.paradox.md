---
node: logic.paradox
title: Paradox and Truth
layer: 1
state: sketch
class: anchor
parent: logic
bridges: [language.truth, logic.nonclassical, logic.mathematical, metaphysics]
pass: 2026-08-21.1
---

# Paradox and Truth

"This sentence is false." If true, it is false; if false, true. The liar is not a party trick. It is a proof that three things we cannot easily surrender — classical logic, a language's ability to talk about its own sentences, and the principle that "*A*" is true if and only if *A* — are jointly inconsistent. Every theory of truth is, at bottom, a decision about which to give up and how to disguise the cost.

Tarski gave up self-reference: no consistent classical language contains its own truth predicate, so truth stratifies into a hierarchy of metalanguages. The diagnosis is exact and the logic stays classical; the cost is that natural language, which happily says "everything the oracle said is true," looks like something the theory forbids. Kripke kept a single, self-applicable truth predicate by letting truth be partial: grounded sentences get values in stages, and the liar, never grounded, gets none. The construction is beautiful — but the *revenge* liar ("this sentence is false or ungrounded") returns at the level of the theory itself, whose semantics must be stated in a metalanguage after all. The ghost of the hierarchy walks.

The radical responses keep naive truth and revise the logic. Field's paracomplete theory drops excluded middle for paradoxical sentences and engineers a new conditional, claiming — controversially — to tame revenge. Priest's dialetheism accepts that the liar is both true and false, with a paraconsistent logic to stop the contradiction from spreading; its strength is uniformity, its price true contradictions most philosophers cannot swallow. Curry's paradox — "if this sentence is true, everything is true" — is the referee: it uses no negation, so gaps and gluts alone do not block it, and it pushes many theorists toward substructural logics that restrict contraction. Any solution that survives Curry has earned something. Yablo's paradox — an infinite list of sentences, each saying that all later ones are untrue — adds a twist: paradox apparently without self-reference at all.

The sorites runs on vagueness rather than truth. One grain is not a heap; adding a grain never turns a non-heap into a heap; so no number of grains makes a heap. Epistemicism (Williamson) holds that "heap" has a sharp cutoff we cannot know, preserving classical logic at the cost of semantic incredulity. Supervaluationism says a vague sentence is true when true on every admissible sharpening — keeping penumbral truths like "nothing is both a heap and not one," while facing higher-order vagueness about "admissible." Degree theories let truth come in degrees and read the sorites as a long, slow leak of it.

Russell's paradox — the set of all sets that are not members of themselves — killed naive set theory and begot the cumulative hierarchy of ZF, whose exclusion of "too big" collections echoes Tarski's exclusion of self-applied truth. Priest's inclosure schema and the literature on indefinite extensibility press the suspicion that all these paradoxes are one paradox in different dress; whether that is depth or numerology is contested.

## Children

- `liar` — **The Liar and Revenge** — The liar paradox, its strengthened forms, and the revenge problem as the test every theory of truth must survive. *(anchor)*
- `formal-truth` — **Formal Theories of Truth** — Tarski's hierarchy, Kripke's fixed points, and the axiomatic theories (KF, FS) as precise proposals for a consistent truth predicate. *(anchor)*
- `curry` — **Curry's Paradox** — Paradox without negation, and the substructural responses that blame the conditional or the rule of contraction. *(standard)*
- `vagueness` — **The Sorites and Vagueness** — The sorites paradox and the theories of vagueness: epistemicism, supervaluationism, degree theories, and contextualism. *(anchor)*
- `set-paradoxes` — **Russell's Paradox and Indefinite Extensibility** — The set-theoretic paradoxes, the cumulative hierarchy as response, and the idea that some concepts cannot be totalized. *(standard)*
- `yablo` — **Yablo's Paradox** — The infinite liar-like sequence and the debate over whether it achieves paradox without circularity. *(satellite)*

## Bridges

- **language.truth**: the editorial split — the *nature* of truth (correspondence, coherence, deflationism, pluralism) is homed there; formal theories of truth and the paradoxes are homed here. Deflationism straddles the border, since its viability may turn on which paradox-solution works.
- **logic.nonclassical**: the paradoxes are the strongest working argument for revising logic; paracomplete, paraconsistent, and substructural systems earn their keep here or nowhere.
- **logic.mathematical**: Russell's paradox shaped axiomatic set theory, and the truth theories are themselves exercises in mathematical logic (fixed-point constructions, proof-theoretic strength).
- **metaphysics**: vagueness raises the question whether the world itself, and not just language, can be vague; indefinite extensibility bears on absolute generality and the limits of quantification.
