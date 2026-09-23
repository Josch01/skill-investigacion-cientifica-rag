# Scientific Research RAG Council v2.1.0

First stable public version of the Scientific Research RAG Council.

## Core principles

- RAG-first scientific reasoning.
- Absolute prohibition on invented theorems, references, assumptions, numerical results, APIs, novelty claims, or proof steps.
- External claims must be grounded in retrieved literature/documentation.
- Previously proved internal results may be reused only when they are CERTIFIED and their hypotheses remain compatible.
- Numerical evidence is kept distinct from mathematical proof unless a rigorous computer-assisted proof framework is used.

## Dynamic expert routing

The skill selects only the specialists required by the task.

Default:
- 1 lead expert;
- 1 independent adversarial reviewer.

Additional experts are activated only when an interdisciplinary bridge, numerical validation, optimization, ML, symbolic computation, or other specialist domain is materially required.

Included domains cover, among others:

- differential algebra;
- structural identifiability;
- dynamical systems;
- chaos and bifurcation theory;
- Lie groups, geometry and equivariant dynamics;
- inverse problems and control;
- numerical analysis and scientific computing;
- optimization;
- machine learning and PINNs;
- statistics and uncertainty quantification;
- symbolic and computer-assisted mathematics;
- scientific literature review and auditing.

## Proof certification and inheritance

New results follow:

```text
DRAFT
  -> verification
  -> applicability audit
  -> proof
  -> adversarial review
  -> counterexample search
  -> CERTIFIED
```

A certified result can be reused in later proofs without loading the complete original proof, provided that:

- the exact statement matches;
- definitions remain compatible;
- hypotheses are satisfied;
- scope is not exceeded;
- the certificate has not been superseded or invalidated.

This provides a proof cache for long-running research programs.

## Scientific RAG

The skill uses:

- Evidence Cards;
- Applicability Matrices;
- Literature Ledger;
- Search Ledger;
- semantic memory index;
- proof dependency graph.

Retrieval is dependency-driven rather than chronological.

## Token efficiency

Default retrieval path:

```text
MEMORY_CORE
  -> MEMORY_INDEX
     -> relevant nodes
        -> proof certificates
           -> original sources only when necessary
```

The goal is to preserve scientific dependencies while avoiding repeated loading of entire conversations, manuscripts, or proofs.

## Numerical rigor

Includes dedicated protocols for:

- ODE/PDE integration;
- chaotic systems;
- Lyapunov analysis;
- optimization and metaheuristics;
- neural networks and PINNs;
- structural identifiability;
- symbolic computation;
- computer-assisted proof;
- reproducibility.

The skill explicitly rejects equivalences such as:

```text
best run != proven global optimum
good fit != identifiability
positive numerical Lyapunov estimate != automatic proof of chaos
full numerical rank != structural identifiability proof
```

## Context7 integration

Context7 is used only as an optional retriever for current software/library/API documentation.

It does not replace scientific literature or mathematical sources.

## Journal compliance

The skill can retrieve current journal/editorial requirements on demand instead of hardcoding policies that may become outdated.

## Repository structure

- `SKILL.md`
- `agents/`
- `protocols/`
- `config/`
- `memory/`
- `templates/`

## Version

`v2.1.0`

This release establishes the initial stable architecture for cumulative, auditable and token-efficient scientific research workflows.
