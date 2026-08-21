# Strata: A Layered Encyclopedia of Philosophy

## Method

This document is the constitution. Every article in the encyclopedia is written under it, and no article — however deep the tree eventually grows — may violate it. When the corpus and this document disagree, this document wins and the corpus gets fixed.

### 1. Purpose

Strata is an encyclopedia of philosophy written by a single author (an AI) over many sessions, with an effectively unlimited word budget and therefore exactly one scarce resource: **judgment about depth**. The design problem is not "what to say" but "how to stop." Everything below exists to make stopping decisions explicit, auditable, and made in cold blood — at the map level, not mid-article when enthusiasm is high.

The encyclopedia is organized by **problems**, not by chronology. Thinkers and traditions are real subjects too, but they live in cross-cutting registers and link into the problem tree, rather than serving as its spine.

### 2. The shape

**Divisions (Layer 0)** — the ten primitive problem-families. These are fixed; changing them is a constitutional amendment:

1. `logic` — Logic (including philosophy of mathematics)
2. `metaphysics` — Metaphysics
3. `epistemology` — Epistemology
4. `mind` — Philosophy of Mind (including action)
5. `language` — Philosophy of Language
6. `science` — Philosophy of Science
7. `ethics` — Ethics
8. `politics` — Political and Social Philosophy
9. `aesthetics` — Aesthetics
10. `religion` — Philosophy of Religion

**Registers (cross-cutting)** — three parallel structures that link into the tree rather than sitting inside it:

- `figures/` — persons as subjects in themselves, written to a fixed template (§7).
- `traditions/` — periods, schools, regional traditions, and movements (Hellenistic philosophy, Nyāya, the Kyoto School, phenomenology, critical theory) treated as living wholes.
- `meta/` — metaphilosophy: what philosophy is, its methods, whether it makes progress.

A topic that seems to belong to two divisions is assigned one **home** and declared as a **bridge** everywhere else (frontmatter `bridges:`). Free will lives in metaphysics and bridges to mind and ethics; philosophy of mathematics lives in logic and bridges to metaphysics and epistemology. Home assignment is an editorial decision recorded once, in the parent's article, not renegotiated per session.

### 3. States: the depth ladder

Every node is in exactly one state. States only move up, one rung per pass.

| State | Meaning | Typical size |
|---|---|---|
| `stub` | Named and glossed in its parent's Children list. **No file exists.** A stub is a claim that the child exists, not a promise of depth. | 1 line |
| `sketch` | A file. The problem stated so a newcomer feels its pull; main positions named; its own Children proposed as stubs. | 300–700 words |
| `survey` | Positions with their best arguments; the live debate; the node rewritten as a map of its children. | 1,500–3,000 words |
| `article` | A full entry: state of the debate, history, literature, bridges made explicit in prose. | 4,000–8,000 words |
| `deep` | Monograph-adjacent treatment. Anchor-class nodes only, and only once the node's whole division is at survey or better. | open |

### 4. Classes: depth ceilings assigned in cold blood

Every node gets a class **at creation time** — that is, when it first appears as a stub in its parent's Children list, before anyone is excited about it:

- `anchor` — may eventually reach `deep`. The load-bearing problems and figures.
- `standard` — ceiling at `article`.
- `satellite` — ceiling at `survey`. Real, but thin.

Promotions and demotions happen only **between** passes, recorded in the INDEX changelog, and the usual evidence for promotion is structural: the bridge graph shows the node carrying more load than its class allows.

### 5. The pulse: descend, then consolidate upward

Growth proceeds in **pulses**, not sweeps. A pulse:

1. **Choose one node** (editorial decision, recorded in INDEX under NEXT).
2. **Descend**: promote its stub children to sketches. Each new sketch must in turn propose *its* children as stubs — the tree discovers its own next layer at every step.
3. **Consolidate upward**: rewrite the chosen node one state higher, now as a genuine map of its children. Then touch every ancestor up to the division root, revising each so it correctly summarizes what now lies beneath it.

Rule: **descent creates a debt, and the debt is upward.** A node whose children have grown since its last revision is *in debt*, and audit flags it. No new pulse may begin in a region that carries unpaid consolidation debt.

Invariant: a child's state never exceeds its parent's state. Depth is earned top-down.

Asymmetry is not merely permitted but expected: the tree should **branch monstrously wherever the field genuinely articulates**, and nowhere else. A division at layer 5 next to a division at layer 1 is a finding, not a failure.

### 6. Stub honesty

The single most important rule: **the next layer down must be discovered, not invented.** A node may be expanded only when its children can be named from the actual articulation of the field — real subfields, real debates with their own literatures. If you cannot name a node's children without straining, it has none; write "thin node — no natural children" in its Children section and let it rest. A satellite that stays a sketch forever is a correct outcome. Padding a thin node to match its siblings' depth is the cardinal sin of this project.

The converse rule: a stub may be created only on **demand** — because its parent's articulation requires it or because two or more existing articles want to bridge to it. No entries for pet topics.

### 7. Voice

Strata is written in **encyclopedia voice**: an entry reports the state of a debate, names the positions, and gives each its best argument — steelmanned, in original prose. An entry is *done* (for its state) when a reader can (a) state the problem, (b) name the main positions and what is strongest in each, and (c) see where to go next.

The author has views. They are quarantined: a marked **Assessment** section, clearly editorial, at most one per article, never load-bearing for the exposition above it. Original argumentation is the most unbounded source of depth; the quarantine is a depth-limiter as much as an honesty device.

Figures articles follow a fixed template: *Why they matter* (one paragraph) → *Life* (brief) → *Works* (the load-bearing texts) → *Thought* (subsections per doctrine, each ending in bridge links into the problem tree) → *Influence and reception* (including who pushed back) → *Reading path* → optional *Assessment*. A figures article is an **edge**: its job is to connect a person to the problems, in both directions.

### 8. Files and frontmatter

- Each division is a directory: `encyclopedia/logic/`. The division's own article is `logic.md` inside it. Descendants are single files with **dotted node paths**: `logic.mathematics.md`, `logic.mathematics.structuralism.md`. Files never move when the tree grows.
- Registers: `figures/frege.md`, `traditions/phenomenology.md`, `meta/metaphilosophy.md`.
- Stubs are lines in their parent's Children section, not files.

Every file opens with YAML frontmatter:

```yaml
---
node: logic.mathematics        # dotted path; must match filename
title: Philosophy of Mathematics
layer: 1                       # 0 for divisions; registers use 0
state: sketch                  # stub|sketch|survey|article|deep (stubs have no file)
class: anchor                  # anchor|standard|satellite
parent: logic                  # or register name: figures, traditions, meta
bridges: [metaphysics, epistemology]
pass: 2026-08-21.1             # date.pulse of last revision
---
```

`tools/encyc.py` regenerates `INDEX.md` from frontmatter and audits the invariants (states valid, parent exists, child ≤ parent, node matches filename). Run it before every commit.

### 9. Session protocol

Work is time-boxed. Each session: (1) read INDEX's NEXT queue; (2) pay any consolidation debt first; (3) run one or more pulses; (4) regenerate INDEX, run audit, record the next session's NEXT; (5) commit and push. Anything not finished when time runs out becomes debt in NEXT — visible, not silent. The encyclopedia must always be leavable: coherent read top-down at every moment, whatever its unevenness of depth.
