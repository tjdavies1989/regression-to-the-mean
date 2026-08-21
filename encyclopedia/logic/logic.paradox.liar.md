---
node: logic.paradox.liar
title: The Liar and Revenge
layer: 2
state: sketch
class: anchor
parent: logic.paradox
bridges: [language.truth, logic.nonclassical, logic.paradox.formal-truth]
pass: 2026-08-21.2
---

# The Liar and Revenge

"This sentence is false" invites a comfortable reply: perhaps it is neither true nor false — gappy, defective, excused from the exam it cannot pass. The *strengthened* liar removes the comfort. Consider "this sentence is not true." Declare it gappy and you have declared it, in particular, not true; but that is exactly what it says, so it is true after all. Falsity is one way of failing to be true; the strengthened liar quantifies over all of them. The simple liar refutes the naive theory of truth; the strengthened liar refutes the first generation of repairs, and it is the form every serious theory must face.

The liar has an undervalued twin. "This sentence is true" — the truth-teller — generates no contradiction: call it true and all is well, call it false and all is equally well. That is precisely the trouble: both assignments are consistent, and nothing favors either — the sentence's truth value answers to nothing outside itself. Inconsistency, then, is not the only pathology in the neighborhood; ungroundedness is a condition the two sentences share, and a diagnosis that speaks only of contradiction has treated a symptom. Kripke's fixed-point construction earns much of its reputation here: it classifies both as ungrounded while still distinguishing the liar (no fixed point evaluates it) from the truth-teller (evaluable either way, in different fixed points — consistent but arbitrary).

Kripke's deeper lesson is that paradox cannot be quarantined among funny sentences. Dean says, "Everything Nixon says about Watergate is false"; Nixon says, "Everything Dean says about Watergate is false." Neither utterance is syntactically exotic, yet if the *other* things each man said about Watergate all happen to be false, the pair is paradoxical — while under luckier distributions of fact, one comes out straightforwardly true and the other false. Whether an ordinary truth attribution is paradoxical can depend on contingencies its speaker cannot survey. Everyday semantic talk is risky, and a theory that merely bans sentences flagged in advance by their form has banned nothing that matters.

The structural problem that now organizes the field is *revenge*. Every solution earns its keep by classifying the liar somehow: ungrounded (Kripke), unstable under revision (Gupta and Belnap), indeterminate (Field), both true and false (Priest), context-shifted (Parsons, Glanzberg). Each classification is a piece of vocabulary, and each vocabulary funds a new liar. "This sentence is false or ungrounded": if ungrounded, then true — contradiction restored, one level up. Kripke conceded the point in advance: the ghost of the Tarskian hierarchy walks in his own theory, whose notion of groundedness lives in a richer metalanguage. Even dialetheism, built to welcome contradiction, meets a strengthened guest: "this sentence is false *only*."

Two readings of revenge divide the literature. On the first, it is a technical artifact — an engineering problem, hard but tractable. Field's paracomplete theory is the flagship claim: a theory can consistently express its own defectiveness predicate, and the liars that remain deploy notions (a single exhaustive "determinately," a classical exclusion negation) that the theory argues no consistent language could express — so their inexpressibility is a discovery, not an evasion. On the second reading, revenge *is* the phenomenon: the liar is not one sentence but an engine that converts any semantic classification into a new paradox, so every consistent theory buys safety with silence, and theories differ only in where they hide what they cannot say. On this reading the choice among solutions is a choice of which inexpressibility one can live with — and the dialetheist adds that there is exactly one theory that hides nothing, if you can stomach its price.

## Children

- `contextualism` — **Contextualist Solutions** — Parsons, Burge, and Glanzberg defuse the liar by letting the extension of "true" shift with context, so each liar is truly assessed only from a later standpoint — a Tarskian hierarchy reborn in pragmatic dress. *(standard)*
- `groundedness` — **Groundedness and the Truth-Teller** — What it is for a sentence's truth to depend on the world: Kripke's fixed points as one precise account among rivals (Yablo, Leitgeb), tested against the truth-teller and its kin. *(satellite)*

## Bridges

- **language.truth**: deflationism stakes everything on the unrestricted truth schema, so its fate hangs on the liar; conversely, any account of the *nature* of truth owes a story about what "not true" means when the strengthened liar wields it.
- **logic.nonclassical**: paracomplete and paraconsistent logics are the machinery of the radical solutions; revenge is the test each must survive, and the substructural turn is largely a response to failing it.
- **logic.paradox.formal-truth**: the constructions this article treats diagnostically — fixed points, revision sequences, Field's models — are homed there as mathematics; here they appear only as bearers of revenge-prone vocabulary.
