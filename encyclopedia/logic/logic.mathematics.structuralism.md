---
node: logic.mathematics.structuralism
title: Structuralism
layer: 2
state: sketch
class: standard
parent: logic.mathematics
bridges: [metaphysics, epistemology, science]
pass: 2026-08-21.1
---

# Structuralism

The founding text is Benacerraf's "What Numbers Could Not Be" (1965). Two children are taught arithmetic through set theory: one learns von Neumann's ordinals, on which 2 is {∅, {∅}} and each number contains all its predecessors; the other Zermelo's, on which 2 is {{∅}} and each contains only its predecessor. Both count, add, and prove flawlessly. Asked whether 1 is a member of 3, one says yes, the other no — and arithmetic cannot arbitrate, because it never needed an answer. Any identification of numbers with particular sets is arbitrary; and since the argument generalizes to any candidate objects, Benacerraf concluded that numbers are not objects at all. All arithmetic demands of its subject is that it form a progression — a first element, a unique successor for each, no circling back. The number 2 is not a thing but a position: second place in any such progression. Mathematics is the science of structure. The thought fits mathematical practice — no number theorist cares *what* the numbers are — but turning the slogan into theory forces a choice about what structures themselves are.

Ante rem structuralism (Shapiro, Resnik) takes structures to be genuine abstract entities, universals existing "before the things" that instantiate them, with positions that are bona fide objects. Its strength is semantic conservatism: "2 is prime" is an ordinary true predication about an object, and mathematical discourse needs no paraphrase. The cost is that Benacerraf's other problem — how creatures like us know about the abstract — returns at one remove, now aimed at structures; Shapiro answers with pattern recognition and implicit definition: a coherent axiom system characterizes a structure and thereby yields knowledge of it.

Eliminative and modal structuralism (Hellman, developing Putnam) refuses the new ontology. Talk of numbers is disguised generalization: an arithmetic sentence says that, *necessarily, anything whatever forming a progression* satisfies the corresponding condition. No structures, no positions — only possible systems under a primitive modal operator. The strength is a clean answer to the access problem: there is nothing abstract to access. The costs are the primitive modality itself and the non-vacuity problem: if no infinite system is even possible, every arithmetic sentence comes out vacuously true, so the view must posit the possibility of infinite systems — which critics find no easier to know than the platonism it replaced.

The sharpest internal objection is the identity problem (Keränen, Burgess). If a position has only the properties conferred by its structure, then structurally indiscernible positions should be identical. But complex conjugation is an automorphism of the complex field swapping i and −i: the two square roots of −1 are perfectly indiscernible by structural properties, yet they are two. Replies divide: the roots are *weakly* discernible (an irreflexive relation holds between them); identity facts are primitive, needing no grounding in properties; or, with Leitgeb and Ladyman, mathematics simply tolerates bare distinctness, as unlabeled graphs already show.

Category theory is often called structuralism's natural language: it characterizes objects only up to isomorphism, through their morphisms, never their membership — the "arrows only" perspective on which asking what an object *is made of* is ungrammatical. Awodey argues that this gives structuralism a working mathematical form with no background ontology; Hellman presses the autonomy question — what, then, are categories? — and univalent foundations, by making "identity is isomorphism" an axiom, has reopened the debate in a new idiom. Whether the framework vindicates structuralism or merely restates its promise is the live edge of the field.

## Children

- `ante-rem` — **Ante Rem Structuralism** — Shapiro's and Resnik's realism about structures and positions, and the epistemology of pattern recognition and implicit definition. *(standard)*
- `modal` — **Modal and Eliminative Structuralism** — Hellman's structuralism without structures: modal generalization over possible systems, and the non-vacuity problem. *(standard)*
- `identity` — **The Identity Problem** — Whether purely structural positions can be distinct yet indiscernible: the two roots of −1, weak discernibility, and primitive identity. *(satellite)*
- `categorical` — **Categorical Structuralism** — Category theory as the mathematics of structure: the arrows-only perspective, the autonomy debate, and univalent foundations as structuralism formalized. *(standard)*

## Bridges

- **Metaphysics**: ante rem structures are universals under another name, and the identity problem is the identity of indiscernibles applied inside mathematics.
- **Epistemology**: the position is scored on whether structures evade or merely relocate the parent's access problem.
- **Science**: ontic structural realism in physics borrows these moves wholesale — indiscernible quantum particles play the role of i and −i.
- **Within logic**: `logic.mathematics.foundations` houses category theory and univalent foundations as rival frameworks; this node treats only their philosophical use as structuralism's formalism.
