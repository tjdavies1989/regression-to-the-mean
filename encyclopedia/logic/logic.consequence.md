---
node: logic.consequence
title: Logical Consequence
layer: 1
state: survey
class: anchor
parent: logic
bridges: [language, metaphysics.modality, epistemology.a-priori, logic.philosophy-of-logic, logic.nonclassical]
pass: 2026-09-09.19
---

# Logical Consequence

Everyone can recognize that "Moby is a mammal" follows from "all whales are mammals" and "Moby is a whale." The problem is to say what this *following from* consists in. The pretheoretic notion weaves together three strands: the conclusion cannot be false if the premises are true (necessity); one could know this without investigating whales (apriority); and the guarantee holds in virtue of the argument's shape, not its subject matter (formality). An analysis must capture all three or explain which are dispensable, and the two great analyses divide over how to cash the modal strand without presupposing it. Since its descent this node divides the work among four studies — the two analyses, the notion of form they both presuppose, and consequence studied in the abstract.

**The model-theoretic account** (`model-theoretic`) is Tarski's 1936 analysis refined into modern model theory: a conclusion follows just in case every model — every reinterpretation of the nonlogical vocabulary over every domain — that makes the premises true makes the conclusion true. Its strength is mathematical tractability and a diagnosis of formality as invariance under reinterpretation; its deepest challenge is Etchemendy's (1990): read interpretationally, the definition is a disguised material generalization, declaring an argument valid when no actual interpretation is a counterexample, so that any extensional match with genuine consequence is a lucky accident of the set-theoretic universe — and the account threatens to overgenerate or undergenerate depending on the size of the world and the choice of constants. The defenses — Sher's invariance theory of the logical constants, Kreisel's squeezing argument trapping informal validity between proof and models, Shapiro's and Gómez-Torrente's rereadings of what Tarski meant — contest whether Etchemendy refutes the analysis or only a misreading of it. The demarcation of the logical constants, which the account presupposes, is homed at `logic.philosophy-of-logic`.

**The proof-theoretic account** (`proof-theoretic`) descends from Gentzen: consequence is derivability by the rules that constitute the meanings of the logical constants, with introduction rules as definitions and elimination rules answerable to them (Prawitz's inversion principle). Its strength is epistemic — a derivation is a surveyable object, and the account explains how we *know* that conclusions follow; its standing obligation, since Prior's "tonk," is to say which rules are meaning-conferring — harmony, in Dummett's term, and Belnap's conservativeness and uniqueness conditions. Proof-theoretic semantics (Schroeder-Heister) has made this a program, bilateralism (Rumfitt) has extended it to denial as well as assertion, and its natural alliance with intuitionism ties it to `logic.nonclassical`. For first-order logic the two analyses provably coincide — completeness, which each side reads as vindication; they come apart in second-order logic, where the dispute turns substantive.

**Logical form** (`logical-form`) is what both accounts presuppose: arguments in natural language must be regimented before either grips them, and how much theory regimentation smuggles in is where consequence borders philosophy of language. Russell's distinction between grammatical and logical form, Davidson's program for events and adverbs, Chomsky's LF in the linguists' sense, Quine's regimentation into canonical notation, and Montague's direct compositionality are the positions; whether form is discovered in the syntax or imposed by the logician's paraphrase, and how validity is properly attributed to arguments in a natural language at all (Iacona), are the live questions.

**Consequence relations** (`abstract-consequence`), at satellite depth, study the notion abstractly: Tarski's consequence operators, the structural properties — reflexivity, monotonicity, cut — and what dropping each yields, multiple-conclusion consequence (Shoesmith and Smiley), and the substructural map that connects this node to the nonclassical logics and to Curry's paradox.

Under all four runs the question the root division raised: whether consequence is one relation captured better or worse by rival analyses, or several relations each correct for a purpose — the monism-versus-pluralism dispute that `logic.philosophy-of-logic` adjudicates, with this node as its raw material.

## Children

- `model-theoretic` — **The Model-Theoretic Account** — Tarski's analysis of consequence via truth in all models, the interpretational/representational distinction, Etchemendy's critique and its answers. *(anchor)*
- `proof-theoretic` — **Proof-Theoretic Consequence** — Validity as derivability: Gentzen's legacy, proof-theoretic semantics, harmony, and the tonk problem. *(anchor)*
- `logical-form` — **Logical Form** — What regimentation reveals or imposes: form in the logician's sense versus LF in the linguist's, and how arguments in natural language get their formal skeletons. *(standard)*
- `abstract-consequence` — **Consequence Relations** — Consequence studied abstractly: Tarskian consequence operations, structural rules (reflexivity, transitivity, monotonicity), and multiple-conclusion frameworks. *(satellite)*

## Bridges

- **Language**: logical form is joint property; whether validity attaches to natural-language arguments directly or only to their regimentations is as much semantics as logic.
- **Metaphysics (`metaphysics.modality`)**: the necessity strand — what kind of modality "cannot be false" invokes, and whether models are surrogates for worlds.
- **Epistemology (`epistemology.a-priori`)**: the apriority strand — how derivations confer knowledge of validity, and whether logical knowledge is a priori at all.
- **logic.philosophy-of-logic**: the logical constants and the monism–pluralism dispute are homed there; **logic.nonclassical** houses the rival systems whose consequence relations differ.
