---
node: science.confirmation
title: Confirmation and Induction
layer: 1
state: sketch
class: anchor
parent: science
bridges: [epistemology.formal, epistemology.skepticism, metaphysics.properties]
pass: 2026-08-26.9
---

# Confirmation and Induction

A thousand emeralds have been examined, and every one is green. Conclude that all emeralds are green — including the ones no one will ever dig up — and you have performed the basic move of science. Nothing in the premises guarantees the conclusion, yet the evidence surely *supports* it. Confirmation theory is the attempt to say what that support is: when evidence counts for a hypothesis, how much, and with what right.

The ground floor is Hume. Any justification of induction must be either demonstrative or itself inductive. Demonstrative it cannot be: there is no contradiction in nature changing course tomorrow. Inductive it cannot be without circularity: "induction has worked so far" supports "induction will work" only by induction. The escape routes — Strawson's dissolution (inductive standards partly *constitute* rationality, so demanding a further warrant is confused), Reichenbach's pragmatic vindication (if any method can find the regularities, induction can), externalist accounts on which induction is justified if in fact reliable, whether or not we can certify it — each purchases relief at a price, and none commands the field.

Hempel changed the question: describe the logic of confirmation rather than justify it. His instance criterion — universal hypotheses are confirmed by their instances — promptly generated the ravens paradox: "all ravens are black" is logically equivalent to "all non-black things are non-ravens," so a white shoe confirms it. Goodman then showed that instances alone cannot even fix *which* hypothesis they confirm: the same green emeralds equally instantiate "all emeralds are grue" (green if examined before some future time, otherwise blue). The new riddle asks what privileges projectible predicates over gerrymandered ones — Goodman's own answer, entrenchment in past practice, strikes many as naming the problem rather than solving it. Hypothetico-deductivism — a theory is confirmed when its predictions pan out — fares no better: if a theory entails the evidence, so does the theory conjoined with any irrelevance, and statistical hypotheses strictly entail nothing at all.

Bayesian confirmation theory is now the leading framework: evidence confirms a hypothesis when it raises its probability. It dissolves the ravens paradox gracefully (the shoe confirms, but minutely), blocks the irrelevant-conjunction problem, and delivers degrees of support where its rivals delivered only a yes or no. The probabilistic machinery — probabilism, conditionalization, and their Dutch book and accuracy vindications — is homed at `epistemology.formal`; what bites here is its two standing wounds in scientific dress: old evidence (Mercury's perihelion confirmed general relativity though Einstein already knew it) and the priors, on which rational agents may apparently diverge without limit.

Two rivals refuse the confirmational picture altogether. Popper denied that evidence ever supports theories: science conjectures boldly and refutes; surviving tests yields "corroboration," not confirmation. The standard objection is that this is no solution: either corroboration gives reason to rely on a theory tomorrow — induction under a new name — or it gives none, and the choice of a bridge design becomes rationally arbitrary. Mayo's error statistics is the serious frequentist heir: a hypothesis is warranted when it passes a *severe* test, one that would very probably have exposed it were it false. Its strength is fidelity to actual statistical practice and its refusal of priors; its critics ask whether severity can be assessed without the very background probabilities it disclaims.

## Children

- `humes-problem` — **The Problem of Induction** — Hume's dilemma and the main escape routes: dissolution, pragmatic vindication, and externalist reliabilism. *(anchor)*
- `qualitative` — **Qualitative Confirmation** — Hempel's instance criterion, the ravens paradox, and the troubles of hypothetico-deductivism. *(standard)*
- `grue` — **The New Riddle of Induction** — Goodman's grue, projectibility, and entrenchment against appeals to natural properties. *(standard)*
- `bayesian` — **Bayesian Confirmation Theory** — probability-raising as confirmation, the rival measures of support, and old evidence and the priors in scientific practice. *(anchor)*
- `severe-testing` — **Error Statistics and Severe Testing** — Mayo's frequentist program and the philosophy of statistical inference. *(standard)*
- `ibe` — **Inference to the Best Explanation** — explanatory virtues as a guide to truth, and whether IBE rivals or reduces to Bayesian updating. *(standard)*

## Bridges

- To `epistemology.formal`: the Bayesian apparatus and its vindications are homed there; the priors and old-evidence problems are jointly owned wounds.
- To `epistemology.skepticism`: Hume's problem is inductive skepticism, and the responses to it track that node's map of skeptical strategies.
- To `metaphysics.properties`: the new riddle demands a distinction between natural and gerrymandered properties — projectibility is naturalness put to inductive work.
- To the registers: Hume and Popper among `figures`; Carnap's inductive logic places the Vienna Circle in `traditions` at this node's modern origin.
