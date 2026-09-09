---
node: logic.consequence.proof-theoretic
title: Proof-Theoretic Consequence
layer: 2
state: sketch
class: anchor
parent: logic.consequence
bridges: [logic.mathematics.intuitionism, logic.nonclassical, language.meaning, logic.philosophy-of-logic]
pass: 2026-09-09.19
---

# Proof-Theoretic Consequence

Gentzen's 1934 remark that the introduction rules of natural deduction "represent, as it were, the definitions" of the connectives, while the eliminations are "only consequences" of them, is the seed of everything here. Taken as a slogan it makes consequence a matter of derivability and meaning a matter of rules; taken as a claim it raises the question that has organized the field since: if rules confer meaning, which rules confer it, and by what right?

**Inversion and normalization.** Prawitz (1965) gave Gentzen's remark technical content. His inversion principle says an elimination rule may extract from a formula no more than its introduction rule put in; a proof that introduces a connective only to eliminate it contains a "detour" that can be reduced away. Normalization — every derivation reduces to one without detours — is the proof of inversion, and the subformula property of normal proofs is the formal image of the idea that nothing in a valid inference exceeds its premises. This gives the position its epistemic strength: a canonical proof is a surveyable object whose steps are answerable to meanings the reasoner already grasps.

**Tonk and its lessons.** Prior (1960) offered "tonk," introduced from either disjunct and eliminated to either conjunct, licensing any conclusion from any premise. If rules alone define, tonk is a connective and logic is trivial. Belnap's reply (1962) is the account's founding constraint: rules define only against an antecedent context of deducibility, and a definition is legitimate only if it is *conservative* — adding the rules proves nothing in the old vocabulary that was not provable before — and *unique*, so that two connectives governed by the same rules are interderivable. Tonk fails conservativeness. The reply concedes something important: what a connective means is not fixed by its rules in isolation but by its rules together with the structural properties of the consequence relation they extend.

**Harmony.** Dummett (1991) generalized Belnap into a criterion on rule-pairs. Introductions and eliminations are in harmony when the eliminations draw out exactly what the introductions warrant — his intrinsic harmony, secured by the existence of reductions — and, more strongly, when the whole package is a conservative extension of the base, his total harmony. Later work has sharpened both directions. Read's general-elimination harmony reads off eliminations from introductions algorithmically; Steinberger argues that harmony is local while conservativeness is global, and that the two come apart (second-order quantifiers are harmonious but non-conservative over arithmetic); Tennant's "stability" adds the converse demand that introductions be recoverable from eliminations. The dispute over the right formulation is not idle, because the criterion is meant to adjudicate logic itself.

**The intuitionistic connection.** Dummett's central application is that classical negation fails harmony: double-negation elimination extracts more than the introduction rule for negation warrants, and adding classical negation to the intuitionistic implication fragment yields Peirce's law non-conservatively. Harmony, on this reading, ratifies intuitionistic logic and joins the manifestation argument as a second route to revision. Classical rejoinders take two forms: reformulate classical logic in a harmonious multiple-conclusion calculus (Read, following Gentzen's sequent calculus), or deny that single-conclusion natural deduction is the privileged format at all. Steinberger and Dummett reply that multiple conclusions have no reading in the practice of assertion they were meant to codify.

**Bilateralism.** Rumfitt (2000), developing Smiley, drops the premise that assertion is the only speech act rules answer to. Signed formulas mark assertion and denial, each connective gets rules for both, and coordination principles link the signs. Classical negation then comes out harmonious, and excluded middle is a theorem of the practice of denial rather than a metaphysical thesis about truth. The objections are that the signs reintroduce classical negation by stipulation, and that denial must be distinguished from asserting a negation without collapsing into it (Incurvati and Schlöder's weak rejection).

**Proof-theoretic semantics.** Schroeder-Heister's program takes the constitutive reading as a semantics proper: validity of an argument is defined, following Prawitz and Dummett, by reducibility to canonical form relative to atomic bases. Its striking result is negative: Piecha and Schroeder-Heister (2019) show intuitionistic logic incomplete for Prawitz–Dummett validity, so the semantics that was to vindicate it validates more. **Base-extension semantics** (Sandqvist 2015; Gheorghiu and Pym) recovers completeness by defining support over sets of atomic rules that may be extended, with disjunction treated through its elimination form — a result that relocates the meaning-constituting role from introductions to something closer to the whole consequence relation, reopening Gentzen's remark from the other side.

## Children

- `harmony` — **Harmony** — Dummett's intrinsic and total harmony, Read's general-elimination harmony, Tennant's stability, and the conservativeness/uniqueness debate descending from Belnap's reply to tonk. *(standard)*
- `bilateralism` — **Bilateralism** — Rumfitt's signed calculus of assertion and denial, coordination principles, weak and strong rejection, and whether classical negation is thereby harmonious. *(standard)*
- `base-extension` — **Base-Extension Semantics** — Prawitz–Dummett validity, the Piecha–Schroeder-Heister incompleteness result, and Sandqvist's completeness for support over extensible atomic bases. *(satellite)*

## Bridges

- **logic.mathematics.intuitionism**: Dummett's harmony argument is the proof-theoretic twin of the manifestation argument homed there; both aim to revise logic from the theory of meaning.
- **logic.nonclassical**: the harmony criterion, if sound, adjudicates between classical and intuitionistic logic, and the substructural map explains why tonk's harm depends on structural rules.
- **language.meaning**: the constitutive reading of rules is inferentialism about the logical constants; whether inferential role fixes meaning at all is contested there.
- **logic.philosophy-of-logic**: an inferentialist demarcation of the logical constants — the harmonious ones — competes with invariance criteria homed there.
