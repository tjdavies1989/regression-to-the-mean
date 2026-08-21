---
node: logic.paradox
title: Paradox and Truth
layer: 1
state: survey
class: anchor
parent: logic
bridges: [language.truth, metaphysics, logic.nonclassical, logic.mathematical]
pass: 2026-08-21.2
---

# Paradox and Truth

"This sentence is false." If true, it is false; if false, true. The liar is not a party trick. It is a proof that three things we cannot easily surrender — classical logic, a language's ability to talk about its own sentences, and the principle that "*A*" is true if and only if *A* — are jointly inconsistent. Every theory of truth is, at bottom, a decision about which to give up and how to disguise the cost. This node maps the paradoxes as a family and the theories built to survive them; since its descent it divides the work among six studies, and the survey below is their map.

**The liar itself** is subtler than its slogan. The comfortable reply — the sentence is neither true nor false — dies against the *strengthened* liar, "this sentence is not true," which quantifies over every way of failing to be true, gaps included. The liar's undervalued twin, the truth-teller ("this sentence is true"), is consistent either way and therefore answerable to nothing — showing that ungroundedness, not contradiction alone, is the underlying pathology. And Kripke's Nixon–Dean cases show paradox cannot be quarantined among syntactically funny sentences: whether an ordinary truth attribution is paradoxical can depend on contingent facts its speaker cannot survey, so everyday semantic talk is intrinsically risky. What now organizes the literature is *revenge*: every solution classifies the liar somehow (ungrounded, unstable, indeterminate, both true and false), each classification is new vocabulary, and each vocabulary funds a new liar one level up. Whether revenge is an engineering problem — Field's paracomplete theory is the flagship claim that a theory can consistently express its own defectiveness predicate — or the phenomenon itself, every consistent theory buying safety with silence, is the deepest open question here; both readings, and the contingent liars, are treated in `liar`.

**The cures, stated precisely enough to be billed**, are collected in `formal-truth`. Tarski's hierarchy is not just the moral "ascend to the metalanguage" but the only theory that *defines* truth, with the indefinability theorem showing its restriction is forced. Kripke's fixed-point construction keeps one self-applied predicate by letting truth be partial: grounded sentences acquire values in stages, the liar never does — and the theory's own key notion, groundedness, lives confessedly in a classical metalanguage; the ghost of the hierarchy walks. The axiomatic turn takes truth as primitive and measures theories by proof-theoretic strength, where deflationism is scored: if truth is a thin device for generalization, adding it should prove nothing new — the disquotational theory TB obliges, the compositional theory CT proves the consistency of arithmetic, and whether that strength refutes deflationism or merely reflects extended induction is a live dispute. The revision theory (Gupta–Belnap) reads truth as a respectable *circular* concept whose signature is the liar's eternal oscillation.

**Curry's paradox** is the referee. "If this sentence is true, everything is true" derives triviality using only the conditional and the structural rule of contraction — no negation anywhere — so every gap and glut theory that tames the liar stands helpless before it, and its validity form (v-Curry) chases the paradox into the metatheory. Substructural logics that restrict contraction earn their philosophical keep here or nowhere; the disquieting parallel with Löb's theorem, where the same reasoning is a celebrated result, is the node's standing puzzle. See `curry`.

**The sorites** runs on vagueness rather than self-reference: one grain is not a heap, one grain never makes the difference, so there are no heaps. The theories divide by where they lodge the blame. Epistemicism (Williamson) keeps classical logic and posits sharp cutoffs unknowable for margin-of-error reasons — maximal conservatism, maximal incredulity. Supervaluationism identifies truth with truth on every admissible sharpening, preserving penumbral connections while higher-order vagueness leaks through "admissible." Degree theories let truth come in degrees and buy a sharp 0.5 for their trouble; contextualist views have the cutoff flee wherever attention lands; nihilism concludes there are no heaps and pays retail. Whether vagueness is semantic, epistemic, or — most radically — in the world itself is adjudicated partly in metaphysics. See `vagueness`.

**The set-theoretic paradoxes** — Russell's class of non-self-membered classes, Burali-Forti's greatest ordinal, Cantor's largest cardinal — killed naive comprehension and begot the two great diagnoses: limitation of size, and the iterative conception of set, defended by Boolos as principled rather than ad hoc. Dummett's *indefinite extensibility* — some concepts, like *set* and *ordinal*, cannot be totalized, since any candidate totality immediately generates a new instance — feeds the absolute-generality debate: whether quantification over absolutely everything is so much as coherent. See `set-paradoxes`.

**Yablo's paradox** — an infinite sequence of sentences, each saying that all later ones are untrue — appears to achieve paradox without self-reference, and the dispute over whether circularity hides in its satisfaction conditions (Priest) or is genuinely absent (Sorensen, Yablo) is a controlled experiment on what actually powers the semantic paradoxes. See `yablo`.

Behind the whole family stands the unity question. Priest's inclosure schema exhibits liar, Russell, Burali-Forti, and their kin as instances of one form — a totality, an operation that diagonalizes out of it, contradiction at the limit — and argues that structurally identical paradoxes deserve a uniform solution, which only dialetheism provides. Critics reply that the schema fits loosely, omits Curry (the case that least resembles the others and most resists everyone), and that "same form" underdetermines "same cure." Depth or numerology remains the right question, and it is not rhetorical.

By editorial decision, the *nature* of truth — correspondence, coherence, deflationism, pluralism — is homed at `language.truth`; this node and its children own the paradoxes and the formal theories. The border is busy in both directions: deflationism's viability may turn on which formal theory works, and which formal theory one accepts constrains what truth can be.

## Children

- `liar` — **The Liar and Revenge** — The strengthened liar, the truth-teller, contingent liars, and revenge as the structural problem every theory of truth must face. *(anchor)*
- `formal-truth` — **Formal Theories of Truth** — Tarski's definition, Kripke's fixed points, the axiomatic theories and their proof-theoretic scorecard, and the revision theory. *(anchor)*
- `curry` — **Curry's Paradox** — Paradox from the conditional alone: v-Curry, the case against contraction, and the Löb parallel. *(standard)*
- `vagueness` — **The Sorites and Vagueness** — Epistemicism, supervaluationism, degree theories, contextualism, and nihilism as rival lodgings for the blame. *(anchor)*
- `set-paradoxes` — **The Set-Theoretic Paradoxes** — Russell, Burali-Forti, and Cantor; the iterative conception; indefinite extensibility and absolute generality. *(standard)*
- `yablo` — **Yablo's Paradox** — Paradox apparently without self-reference, and what the circularity dispute reveals about the family. *(satellite)*

## Bridges

- **language.truth**: the home split — nature of truth there, paradoxes and formal theories here — with deflationism as the doctrine that cannot be assessed without both.
- **logic.nonclassical**: the paradoxes are the strongest working argument for revising logic; paracomplete, paraconsistent, and substructural systems earn their keep against the liar and Curry.
- **logic.mathematical**: the truth theories are exercises in mathematical logic — fixed-point constructions, proof-theoretic strength — and Russell's paradox shaped axiomatic set theory.
- **metaphysics**: ontic vagueness, absolute generality, and the limits of quantification carry the family's weight beyond language.
