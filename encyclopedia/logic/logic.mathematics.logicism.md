---
node: logic.mathematics.logicism
title: Logicism and Neo-Logicism
layer: 2
state: sketch
class: standard
parent: logic.mathematics
bridges: [epistemology, language, logic.mathematical]
pass: 2026-08-21.1
---

# Logicism and Neo-Logicism

If arithmetic is just logic, the deepest puzzles about mathematical knowledge dissolve at a stroke. Logical truth is as a priori and as topic-neutral as truth gets; nobody demands a causal route to the fact that whatever follows from true premises is true. So the logicist thesis — that arithmetic's concepts are definable in logical terms and its theorems derivable from logical laws — would pay Benacerraf's bill in full, and refute Kant's claim that arithmetic is synthetic in the bargain. Frege built the program: in the *Grundlagen* (1884) he defined the numbers as extensions of concepts — the number of Fs is the extension of "equinumerous with F" — and in the *Grundgesetze* he undertook the formal derivation, resting on Basic Law V, which says that concepts have the same extension just when the same things fall under them. In 1902 Russell's letter arrived: consider the extension of "is an extension not belonging to itself." Basic Law V yields a contradiction in a few lines. Frege's appendix conceding the point — arithmetic "totters" — is the most famous collapse in the history of the subject.

Russell and Whitehead rebuilt on stratified ground. The theory of types blocks the paradox by making "class of all classes not members of themselves" ungrammatical, and *Principia Mathematica* carried the derivation of mathematics further than anyone had. But the rescue betrayed the thesis it rescued. The ramified hierarchy was too weak for classical analysis without the axiom of reducibility, a postulate with no claim to logical truth even in Russell's eyes; the axiom of infinity — that there are infinitely many individuals — looks like a contingent claim about the world's population, not a law of logic; the axiom of choice was needed and equally unearned. Russell's retreat was to conditionalize: mathematics asserts only what follows *if* the axioms hold. What survives, and it is not nothing, is the technical demonstration that mathematics can be regimented in a single interpreted system — the indispensable background to every later foundational debate.

The neo-Fregean revival (Wright 1983, then Wright and Hale) begins from a discovery in Frege's own text: Basic Law V is not needed for arithmetic. Hume's Principle — the number of Fs equals the number of Gs iff the Fs and Gs correspond one-to-one — suffices. Frege's Theorem, reconstructed by Parsons, Wright, and Boolos, shows that second-order logic plus Hume's Principle yields full second-order arithmetic; and Hume's Principle, unlike Law V, is consistent. If the principle can be had a priori — as an implicit definition that fixes the concept *cardinal number*, with Frege's context principle licensing reference to the objects it introduces — then arithmetical knowledge is a priori after all, won by stipulation plus logic. The strongest card is the theorem itself: even critics grant it shows arithmetic flowing from astonishingly thin resources.

The objections define the current debate. The **bad company** problem: Basic Law V is an abstraction principle of exactly the same form, and inconsistent; other principles are individually consistent but jointly unsatisfiable with Hume's Principle; so form alone cannot confer good standing, and the criteria proposed to separate good abstractions from bad — conservativeness, stability — look like substantive mathematics, not innocent stipulation. The **Caesar problem**: Hume's Principle is silent on whether the number two is Julius Caesar, so it seems not to fix its concept completely. And Quine's old charge stands sentry: if second-order logic is set theory in disguise, the derivation borrows the mathematics it claims to ground. Extending the program beyond arithmetic — to real analysis and set theory — has proved hard, and abstractionism's most active current form (Linnebo's dynamic abstraction) trades the analyticity claim for a predicative, iterative picture closer to set theory's own.

## Children

- `abstraction` — **Abstraction Principles** — The general theory of abstraction: which principles are legitimate, the bad-company criteria (conservativeness, stability), and dynamic abstraction. *(satellite)*

## Bridges

- **Epistemology**: the program is an epistemological wager — that implicit definition and stipulation can yield a priori knowledge of objects; its fate is a test case for analyticity itself.
- **Language**: Frege's context principle and the semantics of singular terms carry the neo-Fregean argument; the philosophy of language was invented partly to serve this program.
- **Within logic**: `logic.mathematical` houses type theory and second-order logic, whose disputed status — logic or set theory in sheep's clothing — decides how much the logicist may claim.
- **Figures**: `frege` and `russell` in the figures register; this node is the problem-side of their story.
