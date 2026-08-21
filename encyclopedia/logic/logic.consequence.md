---
node: logic.consequence
title: Logical Consequence
layer: 1
state: sketch
class: anchor
parent: logic
bridges: [language, metaphysics, epistemology]
pass: 2026-08-21.1
---

# Logical Consequence

Everyone can recognize that "Moby is a mammal" follows from "all whales are mammals" and "Moby is a whale." The problem is to say what this *following from* consists in. The pretheoretic notion seems to weave together three strands: the conclusion cannot be false if the premises are true (necessity); one could know this without investigating whales (apriority); and the guarantee holds in virtue of the argument's shape, not its subject matter (formality). An analysis of consequence must either capture all three or explain which are dispensable — and the two great analyses on offer divide precisely over how to cash the modal strand without simply presupposing it.

The dominant account is Tarski's, refined into modern model theory: a conclusion is a logical consequence of premises just in case every model — every reinterpretation of the argument's nonlogical vocabulary over every domain — that makes the premises true makes the conclusion true. The strength of the account is its mathematical tractability and its diagnosis of formality: validity is invariance under reinterpretation, so the valid arguments are exactly those that owe nothing to the meanings of their nonlogical parts. Its rival descends from Gentzen: consequence is a matter of proof, of what can be derived using the rules that constitute the meanings of the logical constants. Its strength is epistemic — a derivation is a surveyable, step-by-step object, and the account explains how we *know* that conclusions follow, something a totality of models seems ill-placed to do. Prawitz and Dummett built on this an entire theory of meaning; its standing problem, since Prior's connective "tonk," is to say which rules are meaning-conferring — the demand usually called harmony. For first-order logic the two analyses provably coincide (completeness), which each side reads as vindication; they come apart in second-order logic and beyond, where the disagreement turns substantive.

Both accounts inherit the demarcation question: invariance under reinterpretation of the *nonlogical* vocabulary is empty until one says which expressions are logical. Tarski's own late proposal — logical notions are those invariant under all permutations of the domain — has been developed by Sher and others into a full theory of formality, and contested as counting too much (cardinality quantifiers) or resting on the wrong kind of criterion.

The deepest challenge to the Tarskian analysis is Etchemendy's. The model-theoretic definition, he argues, is a materially disguised universal generalization: it declares an argument valid when no *actual* interpretation is a counterexample, and any extensional match with genuine — necessary, a priori — consequence is a lucky accident of the set-theoretic universe. Depending on the size of the world and the choice of logical constants, the account threatens to overgenerate (blessing merely true generalizations as logic) or undergenerate. Defenders respond that Etchemendy conflates interpretational with representational readings of models, or invoke Kreisel's squeezing argument, which traps the informal notion between proof and models and certifies the extension after all. Whether the argument certifies the *analysis*, or merely its extension, is the live question.

Behind all of this stands logical form. Arguments in natural language must be regimented before either analysis grips them, and how much theory that regimentation smuggles in — whether the forms are discovered in the syntax, as linguists' LF suggests, or imposed by the logician's paraphrase, as Quinean regimentation has it — is where consequence borders the philosophy of language.

## Children

- `model-theoretic` — **The Model-Theoretic Account** — Tarski's analysis of consequence via truth in all models, the interpretational/representational distinction, Etchemendy's critique and its answers. *(anchor)*
- `proof-theoretic` — **Proof-Theoretic Consequence** — Validity as derivability: Gentzen's legacy, proof-theoretic semantics, harmony, and the tonk problem. *(anchor)*
- `logical-form` — **Logical Form** — What regimentation reveals or imposes: form in the logician's sense versus LF in the linguist's, and how arguments in natural language get their formal skeletons. *(standard)*
- `abstract-consequence` — **Consequence Relations** — Consequence studied abstractly: Tarskian consequence operations, structural rules (reflexivity, transitivity, monotonicity), and multiple-conclusion frameworks. *(satellite)*

## Bridges

- **Language**: logical form is joint property — whether validity attaches to natural-language arguments directly or only to their regimentations is as much semantics as logic, and truth-in-a-model borders theories of truth and meaning.
- **Metaphysics**: the necessity strand of consequence — what kind of modality "cannot be false" invokes, and whether models are surrogates for possible worlds — runs straight into the metaphysics of modality.
- **Epistemology**: the apriority strand — how derivations confer knowledge of validity, and whether logical knowledge is a priori at all — ties the proof-theoretic account to the theory of justification.
