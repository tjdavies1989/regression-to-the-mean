---
node: logic.argumentation
title: Argumentation
layer: 1
state: sketch
class: satellite
parent: logic
bridges: [epistemology, mind, language]
pass: 2026-08-21.1
---

# Argumentation

An argument can be formally valid and worthless: "the moon is cheese; therefore, if inflation rises, the moon is cheese" passes every classical test. And it can be formally invalid yet excellent: nearly all real persuasion — inference from expert testimony, from analogy, from sign, from consequences — is deductively invalid, and rightly trusted anyway. Formal validity thus radically underdetermines the goodness of real-world argument. Argumentation theory is the study of what else is required, and the informal logic movement (Johnson, Blair, Govier) began from precisely this gap, proposing that premises must also be *acceptable*, *relevant*, and *sufficient* — three criteria formal logic does not touch.

The oldest branch is fallacy theory: the catalogue, descending from Aristotle's *Sophistical Refutations*, of characteristic ways arguments go wrong — ad hominem, appeal to authority, slippery slope, many questions. Hamblin's *Fallacies* (1970) broke the tradition open by observing that the standard treatment was incoherent: a fallacy was defined as an argument that seems valid but is not, yet most catalogued fallacies are not deductive failures at all, and most have reasonable instances. Attacking a witness's character is often exactly the right move; appealing to authority is how nearly all knowledge is transmitted; slippery-slope reasoning is sometimes sober policy analysis. The dominant repair, due chiefly to Walton, reconceives the fallacies as *argumentation schemes* — presumptive, defeasible forms of inference, each with attached critical questions — that are legitimate when the questions can be answered and fallacious when deployed to evade them. What was a list of sins becomes a taxonomy of risky but respectable inference, with fallaciousness relocated from form to use.

Toulmin's *The Uses of Argument* (1958) supplied the field's most famous alternative anatomy: a claim rests on data (grounds), the step is licensed by a warrant, the warrant by backing, and the whole is hedged by qualifiers and rebuttals. Two theses matter more than the diagram: warrants and standards of backing are *field-dependent* — what counts as good argument in law differs from physics — and everyday argument is irreducibly defeasible, so the geometrical ideal of formal deduction was always the wrong model. Critics note that the layout's categories blur in application — data and warrant are notoriously hard to tell apart — and that the model describes arguments better than it evaluates them.

A third axis sorts theories by what an argument *is*. Logical approaches treat it as a product — premises and conclusion on the page. Dialectical approaches treat it as a procedure: pragma-dialectics (van Eemeren and Grootendorst) models argument as a rule-governed critical discussion aimed at resolving a difference of opinion, with fallacies redefined as rule violations; formal dialectic (Hamblin, Walton and Krabbe) builds explicit dialogue games with commitment stores. Rhetorical approaches, revived by Perelman and Olbrechts-Tyteca's *new rhetoric*, treat it as a process aimed at the adherence of an audience, with Perelman's *universal audience* answering the charge of mere persuasion. The three perspectives are now usually treated as complementary.

The field's current energy is at its empirical and computational borders. Bayesian analyses (Hahn and Oaksford) show that classic "fallacies" vary in evidential strength with content in just the way probability theory predicts, vindicating the context-sensitivity Hamblin urged. Mercier and Sperber's argumentative theory of reasoning claims human inference evolved *for* argumentation, explaining both the confirmation bias of solitary reasoners and the reliability of groups. And Dung-style abstract argumentation frameworks have made defeasible argument a formal object again — inside artificial intelligence rather than logic departments. A satellite node: real, lean, and its children are few.

## Children

- `fallacies` — **Fallacy Theory** — The Aristotelian catalogue, Hamblin's demolition of the standard treatment, and the reconception of fallacies as misused presumptive inference. *(satellite)*
- `schemes` — **Argumentation Schemes** — Defeasible inference forms — expert opinion, analogy, sign, consequence — their critical questions, and their formalization in AI. *(satellite)*
- `dialectic` — **Dialectical and Rhetorical Models** — Argument as procedure and process: pragma-dialectics, formal dialogue games, and the new rhetoric's audience-based standard. *(satellite)*

## Bridges

- **Epistemology**: appeals to authority are the theory of testimony under another name; argument evaluation is applied theory of evidence, and Bayesian treatments make the link explicit.
- **Mind**: the psychology of reasoning and Mercier–Sperber's argumentative theory make argumentation a datum for cognitive science, not just a norm over it.
- **Language**: pragma-dialectics is built on speech-act theory and Gricean pragmatics; what an argument *is* depends on what utterances do.
- **Within logic**: `philosophy-of-logic` owns the general gap between formal consequence and actual reasoning; `nonclassical` and the AI formalisms meet in defeasible and nonmonotonic inference.
