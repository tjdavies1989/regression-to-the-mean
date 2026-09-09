---
node: logic.consequence.logical-form
title: Logical Form
layer: 2
state: sketch
class: standard
parent: logic.consequence
bridges: [language.meaning, language.reference, metaphysics.ontology, figures.russell, figures.quine]
pass: 2026-09-09.19
---

# Logical Form

Both analyses of consequence take regimented sentences as input; neither says how a sentence of English acquires a regimentation. "Logical form" names the structure in virtue of which an argument is valid, and the question is where that structure lives: in the sentence, in the competence of its speakers, or in the logician's paraphrase. Five programs answer differently.

**Russell** made the founding move in "On Denoting" (1905). "The present King of France is bald" has the grammar of subject and predicate, but taking that grammar at face value forces either a Meinongian king or a truth-value gap; analyzed as an existential quantification the sentence is simply false, and its negation acquires the two readings speakers actually hear. Grammatical form disguises logical form, which analysis uncovers — a doctrine the *Tractatus* radicalized. The best argument is diagnostic power: only a hidden-form hypothesis explains why surface-similar sentences ("Scott is the author of *Waverley*," "Scott is Scott") behave so differently under substitution.

**Davidson** ("The Logical Form of Action Sentences," 1967) supplied the method Russell lacked: a proposed form is correct when it makes the inferences speakers accept come out valid in first-order logic, and when a finite Tarskian truth theory can be built on it. "Jones buttered the toast slowly in the bathroom with a knife" entails "Jones buttered the toast"; treating *butter* as a predicate of variable adicity cannot capture this, but quantifying over events can — there was an event of buttering, and it was slow, and it was in the bathroom — and adverb-dropping becomes conjunction elimination. Form is discovered because the entailment data are real, but discovered relative to a chosen logic, and the ontology of events is earned by explaining inferences nothing else explains. The neo-Davidsonian program (Parsons) extends the treatment to thematic roles and tense, and now houses the event literature.

**Chomsky's LF** is a different thing under the same name: a level of syntactic representation, derived from surface structure by covert movement (May's Quantifier Raising), at which scope and binding are represented. Its evidence is empirical — scope ambiguities, weak-crossover effects, the island constraints that covert movement obeys exactly as overt movement does — and it belongs to the speaker's grammar, not to the logician's notation. LF is not designed to certify validity, and whether it can be identified with logical form in the philosopher's sense is itself a debate (Hornstein, Ludlow, Pietroski). The best argument for taking it seriously is that it is discovered by methods with no stake in logic, and still delivers quantifier structure.

**Quine** rejected the picture of hidden structure altogether. Regimentation into canonical notation (*Word and Object* §33) is a decision made for theoretical purposes — to simplify, to make ontological commitment explicit, to bring the resources of first-order logic to bear — and paraphrase claims no synonymy with what it paraphrases. Where several regimentations preserve the same logical relations, there is no further fact about which is *the* form; the indeterminacy of translation applies at home. Form is imposed, and the only test is fruitfulness.

**Montague** dissolved the gap Russell opened. "English as a Formal Language" (1970) treats natural language with the same model-theoretic rigor as a calculus, interpreting surface constituents directly by rule-to-rule translation into a typed intensional logic. With generalized quantifiers, "every man" is a genuine constituent denoting a set of sets; no covert restructuring is needed, and Russell's "misleading" surface was an artifact of an impoverished logic. Direct compositionality (Jacobson) makes this a research program: syntax interpreted as it stands, with no hidden level.

The question underneath is whether form is discovered or imposed. Russell, Davidson, and the Chomskyans are realists in different ways — form is a fact about the sentence or its speaker; Quine is an instrumentalist; Montague denies there is anything to find because the surface already is the form. Iacona (*Logical Form*, 2018) argues the notion has been asked to play two roles it cannot play together: a *logical* role, accounting for validity, and a *semantic* role, accounting for truth conditions. Whether "Aristotle is a philosopher, so Aristotle is a philosopher" is formally valid depends on whether the two names corefer, which no syntactic property settles; on Iacona's truth-conditional view, form is fixed by interpreted truth conditions, so validity attaches to arguments under an interpretation, not to sentence-types. Brandom's inferentialist reversal — form as what logical vocabulary makes explicit — is the other contemporary pole. The consequence relations of the sibling nodes presuppose a settled answer here; none is settled.

## Children

Thin node — no natural children yet.

## Bridges

- **language.meaning**: Davidson's truth-theoretic program and Montague's formal semantics are homed there as theories of meaning; this node takes only their bearing on validity, and the compositionality principle they share.
- **language.reference**: Russell's theory of descriptions, the founding case of grammatical versus logical form, is homed under definite descriptions.
- **metaphysics.ontology**: Quine's regimentation is the instrument of ontological commitment — to be is to be the value of a bound variable — and Davidson's events enter ontology through logical form.
- **figures.russell**, **figures.quine**: the two thinkers whose positions define the realist and instrumentalist ends of the discovered-or-imposed question.
