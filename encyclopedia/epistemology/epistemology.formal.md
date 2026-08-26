---
node: epistemology.formal
title: Formal Epistemology
layer: 1
state: sketch
class: standard
parent: epistemology
bridges: [logic.modal.epistemic, science.confirmation, epistemology.social, epistemology.disagreement]
pass: 2026-08-26.6
---

# Formal Epistemology

Belief is not on or off. You believe your train leaves at noon, but not the way you believe you have hands; a weather forecast can shift your confidence without flipping any belief from absent to present. Formal epistemology takes this seriously: rationality is a matter of *degrees* of belief, and the degrees obey mathematics. The wager is that once credences are numbers, the vague injunction "be reasonable" becomes a set of theorems — and violations of reason become calculable mistakes.

The dominant program is Bayesianism, built on two norms. Synchronically, your credences at a time must be probabilities — sum to one over exhaustive alternatives, never exceed certainty. Diachronically, you must update by conditionalization: on learning E, your new credence in H becomes your old credence in H given E. Two vindications give the norms teeth. The Dutch book argument shows that anyone whose credences violate the probability axioms will accept a set of bets each of which looks fair by their own lights and which jointly guarantee a loss — incoherence made purchasable. Joyce's accuracy-first argument drops the betting and treats credences as estimates aiming at truth: any non-probabilistic credence function is *accuracy-dominated* — some probability function is closer to the truth however the world turns out — so probabilism falls out of the sheer aim of getting things right, and conditionalization follows from expected accuracy. The strongest thing in Bayesianism is this convergence: independent arguments, one pragmatic and one alethic, land on the same norms.

Its two famous wounds are priors and old evidence. Conditionalization says how to move but not where to start: subjective Bayesians allow any coherent priors, at the cost of licensing wildly divergent rational agents; objective Bayesians constrain priors by symmetry or indifference principles, which notoriously give inconsistent answers under redescription. And evidence already known — Mercury's perihelion when Einstein arrived — has probability one, so conditionalizing on it can raise no hypothesis; yet it plainly confirmed general relativity.

A second front asks how graded credence relates to plain, outright belief. The natural bridge is the Lockean thesis: believe whatever you assign credence above some threshold. But the lottery paradox shows any threshold short of certainty licenses believing of each ticket that it will lose, hence — under closure — the absurdity that no ticket wins; the preface paradox shows a scrupulous author rationally believing each sentence of her book while believing the conjunction false. Positions divide: keep both notions and drop closure for belief, reduce belief to high credence and accept the costs, or (Ross and Schroeder, and normative reasoning accounts) treat belief as a distinct attitude answering to different work.

Precision itself is contested. Assigning 0.5 to rain on unexamined evidence and 0.5 after exhaustive study look different; imprecise Bayesians represent belief by sets of probability functions, gaining a model of ambiguity at the price of puzzles about decision (dilation, and how imprecise credences license action at all).

Finally the machinery scales socially. Condorcet's jury theorem shows majorities of independent, better-than-chance voters approaching infallibility as the group grows — the founding result of formal social epistemology — while opinion pooling and judgment aggregation study how a group's credences or verdicts can be built from its members' without paradox.

## Children

- `bayesianism` — **Bayesian Epistemology** — probabilism and conditionalization, the Dutch book and accuracy-first vindications, and the problems of priors and old evidence. *(anchor)*
- `belief-credence` — **Belief and Credence** — the Lockean thesis, the lottery and preface paradoxes, and whether outright belief reduces to degrees. *(standard)*
- `imprecise` — **Imprecise Credences** — sets of probability functions as models of ambiguous evidence, and the dilation and decision problems they raise. *(satellite)*
- `social` — **Formal Social Epistemology** — the Condorcet jury theorem, opinion pooling, judgment aggregation, and network models of inquiry. *(standard)*

## Bridges

- To `logic.modal.epistemic`: epistemic logic is homed there; its axioms (KK, logical omniscience) formalize the qualitative side of what this node treats quantitatively.
- To `science.confirmation`: confirmation theory is homed in philosophy of science; the Bayesian machinery is shared, and old evidence is a joint wound.
- To `epistemology.social`: formal social epistemology supplies the theorems for that node's questions about testimony, expertise, and group belief.
- To `epistemology.disagreement`: peer disagreement's conciliationism is often modeled as opinion pooling; higher-order evidence strains conditionalization itself.
