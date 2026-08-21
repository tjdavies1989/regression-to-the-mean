---
node: logic.nonclassical
title: Nonclassical Logics
layer: 1
state: sketch
class: anchor
parent: logic
bridges: [logic.philosophy-of-logic, logic.paradox, logic.mathematics, language]
pass: 2026-08-21.1
---

# Nonclassical Logics

Classical logic makes commitments that look unavoidable at the blackboard and doubtful in the wild. Every statement is true or false, with nothing in between. A contradiction entails absolutely everything — from "it is raining and not raining" infer "the moon is cheese" (*explosion*). And "if A then B" comes out true whenever A is false, so "if 2+2=5, then grass sings" is a logical truth. Nonclassical logics are systems built by revising one or more of these commitments — not *extending* classical logic, as modal logic does, but contradicting it, declaring some classically valid arguments invalid. The governing question is blunt: could one of these rivals be *correct* — the true account of consequence — and what would that even mean? The paradoxes give the question teeth: the liar and the sorites arise inside classical logic from apparently innocent principles, and revising the logic is one of the standing escape routes.

**Intuitionistic logic** rejects the law of excluded middle: it will not assert "A or not-A" without a warrant for one disjunct. It has two independent motivations, which is part of its strength. The first is Brouwer's constructive mathematics: if mathematical truth is provability, then an undecided conjecture is neither true nor false, and existence claims demand witnesses — a demand with real mathematical content, since constructive proofs compute. The second is Dummett's semantic antirealism: meaning must be publicly manifestable, so truth cannot outrun our capacity to verify — an argument that, if sound, forces intuitionistic revision everywhere, not just in mathematics. **Relevance logic** attacks the material conditional and explosion at once: a valid argument should require some real connection between premises and conclusion, formally enforced by variable-sharing. Its strength is diagnostic — it locates exactly which classical structural assumptions smuggle in irrelevance. **Paraconsistent logics** block explosion so that theories can contain contradictions without collapse; the strongest motivation is that we reason productively inside inconsistent theories (naive set theory, early calculus) all the time. Its radical wing is Priest's **dialetheism**: some contradictions are actually *true* — the liar sentence being the star exhibit — a view whose strength is that it takes the paradoxes at face value where every rival must explain something away. **Many-valued and fuzzy logics** add truth values or degrees of truth, most plausibly for vagueness: a man losing hairs is not suddenly bald, so perhaps truth comes in degrees. **Substructural logics** generalize the whole landscape from proof theory: dropping structural rules such as contraction or weakening yields relevance logic, linear logic, and — strikingly — resources for blocking Curry's paradox. **Quantum logic** was once the boldest proposal of all: Putnam argued that quantum mechanics empirically refutes the distributive law, just as relativity refuted Euclidean geometry. Its fall — few now think lattice structure in Hilbert space tells us how to *reason* — is itself instructive about what it takes for physics to revise logic.

What would make a rival correct? A monist must say classical logic (or the rival) gets consequence right and the others model something else; a pluralist, following Beall and Restall, says several logics are equally correct relative to different precisifications of validity. That dispute is philosophy of logic's problem; the rivals are its raw material.

## Children

- `intuitionistic` — **Intuitionistic Logic** — Logic without excluded middle, motivated by constructive mathematics and Dummett's antirealist theory of meaning. *(anchor)*
- `relevance` — **Relevance Logic** — Systems requiring a real connection between premises and conclusion, against explosion and the paradoxes of material implication. *(standard)*
- `paraconsistent` — **Paraconsistency and Dialetheism** — Logics that tolerate contradiction without collapse, and Priest's thesis that some contradictions are true. *(anchor)*
- `many-valued` — **Many-Valued and Fuzzy Logic** — More than two truth values, from Łukasiewicz's third value to degree-theoretic treatments of vagueness. *(standard)*
- `substructural` — **Substructural Logics** — What follows when structural rules like contraction and weakening are dropped: linear logic and the proof-theoretic map of the nonclassical terrain. *(standard)*
- `quantum` — **Quantum Logic** — Putnam's proposal that physics revises logic, its distributive-law target, and why the program stalled. *(satellite)*

## Bridges

- **Philosophy of logic** (`logic.philosophy-of-logic`): whether any rival is *correct* is the monism–pluralism debate; anti-exceptionalism about logic's revisability is the background of the whole field.
- **Paradox and truth** (`logic.paradox`): the liar motivates paraconsistency and dialetheism, the sorites motivates many-valued and fuzzy logics, and Curry pressures substructural revision.
- **Philosophy of mathematics** (`logic.mathematics`): constructivism is intuitionistic logic's first home; what revising logic does to mathematical practice is contested there.
- **Language**: Dummett's manifestation argument makes the choice of logic turn on the theory of meaning; the conditional and vagueness are joint property with natural-language semantics.
