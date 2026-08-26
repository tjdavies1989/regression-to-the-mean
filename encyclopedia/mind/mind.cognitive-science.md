---
node: mind.cognitive-science
title: Foundations of Cognitive Science
layer: 1
state: sketch
class: standard
parent: mind
bridges: [science, mind.mind-body, mind.intentionality, mind.artificial-minds]
pass: 2026-08-26.8
---

# Foundations of Cognitive Science

Cognitive science was founded on a bet: that thinking is a kind of computation, and that a mind can therefore be studied the way software is studied — by asking what it computes, not what it is made of. The bet paid for the cognitive revolution against behaviorism, and Marr's three levels became its grammar: specify the *computational* problem a system solves and why, then the *algorithm* and representations that solve it, then the *implementation* in wetware. The scheme licensed a psychology autonomous from neuroscience — the same computation could run on neurons or silicon — and every foundational quarrel since can be stated as a dispute about what happens at which level, or whether the levels carve anything at all.

The first quarrel is over the shape of the software. The classical view (Fodor's language of thought) holds that cognition is rule-governed manipulation of symbols with syntactic structure, and its best argument is systematicity: anyone who can think *John loves Mary* can think *Mary loves John*, which is inevitable if thoughts are built from recombinable constituents and a mystery otherwise. Connectionism replaces symbols with networks of simple units and learned, distributed representations; its strengths — learning from examples, graceful degradation, something like neural plausibility — are exactly where classicism is weakest. Fodor and Pylyshyn's dilemma (1988) charged that networks either fail to explain systematicity or succeed only by implementing a classical architecture in disguise; Smolensky answered that distributed vectors can encode constituent structure without any discrete symbols being tokened. Whether that is a refutation or a concession is still contested, and the argument has been rerun wholesale over deep learning.

A second quarrel concerns architecture. Fodor's modularity thesis holds that input systems — vision, parsing — are fast, domain-specific, and informationally encapsulated (the Müller-Lyer illusion survives your knowing better), while central cognition is a holistic free-for-all he thought science might never crack. Evolutionary psychology's massive modularity turns the exception into the rule: central cognition, too, is a bundle of task-specific devices, since a general-purpose learner is computationally intractable. Critics reply that the flexibility of human thought — its ability to combine anything with anything — is precisely what modules cannot deliver.

The 4E movement rejects the shared premise that cognition happens inside. Cognition is *embodied* (shaped by the body's morphology), *embedded* (offloaded onto scaffolding), *enactive* (constituted by sensorimotor engagement), and *extended*: Clark and Chalmers argue that Otto's notebook, playing the functional role of Inga's memory, is part of his mind — parity of role, parity of status. The coupling-constitution objection (Adams and Aizawa, Rupert) answers that a resource's being causally coupled to cognition does not make it a constituent of cognition, any more than the pencil is part of the mathematician.

Predictive processing is the current candidate for grand unification: the brain as a hierarchical prediction machine that minimizes error between expected and incoming signal, with perception, action, and learning as three faces of one imperative. Enthusiasts read it as the field's Newtonian moment; deflationists note that a framework compatible with any evidence explains none, and that its "predictions" may be redescription. Beneath everything runs the representation war: radical enactivists (Hutto and Myin's hard problem of content), dynamicists, and ecological psychologists deny that brains traffic in representations at all, while defenders reply that error signals are contentful or they are nothing.

## Children

- `computation` — **Classical and Connectionist Architectures** — the language of thought, neural networks, and the systematicity debate over whether thought requires constituent structure. *(standard)*
- `levels` — **Levels of Explanation** — Marr's hierarchy and the autonomy of psychology from neuroscience. *(satellite)*
- `modularity` — **Modularity of Mind** — Fodor's encapsulated input systems, massive modularity, and the tractability of central cognition. *(standard)*
- `4e` — **Embodied and Extended Cognition** — the 4E program, the extended-mind thesis, and the coupling-constitution objection. *(standard)*
- `predictive-processing` — **Predictive Processing** — the brain as prediction-error minimizer, and whether the framework unifies or merely redescribes. *(standard)*
- `representation` — **The Representation Wars** — radical enactivism, dynamicism, and ecological psychology against cognitive science's central posit. *(standard)*

## Bridges

- To `science`: the empirical study of cognition is homed there; this node keeps what the science must presuppose about the mind — computation, representation, levels.
- To `mind.mind-body`: the computational theory of mind is functionalism made concrete, and inherits its promise and its critics.
- To `mind.intentionality`: the representation wars turn on whether content can be naturalized — Hutto and Myin's hard problem of content is the disjunction problem redeployed as a weapon.
- To `mind.artificial-minds`: whether machines can think and whether thinking is computation are one bet run in two directions.
