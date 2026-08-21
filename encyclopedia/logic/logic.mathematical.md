---
node: logic.mathematical
title: Mathematical Logic
layer: 1
state: sketch
class: standard
parent: logic
bridges: [logic.mathematics, mind, language]
pass: 2026-08-21.1
---

# Mathematical Logic

At the start of the twentieth century, logic stopped being only philosophy's instrument and became mathematics' subject matter: proofs, theories, and computations were themselves formalized and studied with mathematical rigor. The result is a four-limbed technical discipline — proof theory, model theory, set theory, computability theory — whose theorems keep turning out to be philosophically explosive. Strata treats the cluster here for its philosophical yield; the mathematics itself belongs to the textbooks.

**Proof theory** studies formal proofs as combinatorial objects. Its founding ambition was Hilbert's: prove, by elementary means, that mathematics can never derive a contradiction. Gödel's second incompleteness theorem broke the program in its original form — no consistent theory of the relevant strength can prove its own consistency — but Gentzen's 1936 consistency proof for arithmetic, using induction up to the ordinal ε₀, showed what survives: consistency can be established from principles *different* from, rather than weaker than, those of the theory itself. Ordinal analysis descends from this, calibrating the strength of theories on a single ordinal scale, and Gentzen's other legacy — natural deduction and the sequent calculus, with their cut-elimination theorem — supplies the inferentialist's best tools for saying what a logical constant is.

**Model theory** studies the relation between theories and the structures that satisfy them, and its philosophical dividend is a series of humbling discoveries about what axioms can and cannot pin down. The Löwenheim–Skolem theorems show that no first-order theory with an infinite model determines the size of its subject matter; compactness yields nonstandard models of arithmetic containing "infinite numbers" the axioms cannot exclude — a result Skolem read as relativism about mathematical notions and Putnam later sharpened into an argument against realist theories of reference. Categoricity results mark the other pole: second-order arithmetic pins down its structure uniquely, at the price of a logic whose own consequence relation is no longer effectively surveyable. Robinson's nonstandard analysis turned the pathology into a tool, rehabilitating infinitesimals.

**Set theory** provides mathematics' working foundation. ZFC is the de facto constitution, strong enough to encode virtually all classical mathematics — and provably unable to settle natural questions about it. Gödel and Cohen showed the continuum hypothesis independent of ZFC; the method of forcing has since generated a vast landscape of alternative set-theoretic universes. The technical response is the large cardinal hierarchy, a remarkably linear scale of strong axioms of infinity that measures the strength of independent statements and settles some of them. Whether independence shows such questions to lack determinate answers, and whether anything could justify new axioms, are questions housed under philosophy of mathematics; the machinery lives here.

**Computability theory** made "mechanically solvable" precise. Turing machines, recursive functions, and the lambda calculus, proposed independently, define exactly the same class of functions — the convergence that grounds the Church–Turing thesis, the claim (empirical? conceptual? mathematically provable?) that this class captures effective calculability as such. From it flow the undecidability results: no algorithm decides the halting problem, or first-order validity (Church), or the truths of arithmetic. Gödel's incompleteness theorems — every consistent, effectively axiomatized theory containing enough arithmetic leaves truths of its own language unprovable, its own consistency among them — sit at the junction of all four limbs. Their technical content belongs to this node; the philosophical wars over what they show — about Hilbert's program, mechanism, and the mind — are fought under philosophy of mathematics and philosophy of mind.

## Children

- `proof-theory` — **Proof Theory** — Proofs as mathematical objects: Hilbert's program, Gentzen's consistency proof, ordinal analysis, and structural proof theory. *(standard)*
- `model-theory` — **Model Theory** — Theories and their structures: Löwenheim–Skolem, compactness, categoricity, definability, and nonstandard models. *(standard)*
- `set-theory` — **Set Theory** — ZFC and its universe: the independence phenomenon, forcing, and the large cardinal hierarchy, on the technical side. *(standard)*
- `computability` — **Computability** — Turing machines, the Church–Turing thesis, undecidability, and the degrees of unsolvability. *(standard)*

## Bridges

- **Philosophy of mathematics** (`logic.mathematics`): the heaviest bridge — incompleteness, independence, and the fate of foundational programs supply that node's central evidence; the theorems live here, their import there.
- **Mind**: the Church–Turing thesis underwrites computational theories of mind, and Lucas–Penrose arguments claim incompleteness refutes mechanism.
- **Language**: Löwenheim–Skolem and Putnam's model-theoretic argument press on realist theories of reference and the determinacy of meaning.
- **Classical logic** (sibling): the celebrated metatheorems — completeness, compactness, undecidability — are stated there and proved with this node's tools.
