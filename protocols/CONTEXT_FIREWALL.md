# Context Firewall Protocol

## Purpose

Reduce anchoring and verdict leakage between functional roles, especially in single-provider runtimes.

## General rule

Transfer scientific artifacts, not prior confidence/verdict language.

## Research Architect receives

- user objective;
- relevant source/manuscript;
- certified prior results;
- definitions.

It does not receive desired theorem outcome as a premise.

## Proof Engineer receives

- exact obligation;
- hypotheses;
- definitions;
- required dependencies;
- relevant source slices.

It should not receive prior auditor verdicts.

## Falsifier receives

- claim;
- hypotheses;
- definitions;
- candidate proof/evidence when needed to attack the argument.

It should not receive "the claim is certified/correct".

## Evidence Auditor receives

- evidence item;
- intended parent claim;
- declared role;
- computation/source artifacts.

It does not decide claim truth.

## Independent Reviewer receives

- statement;
- hypotheses;
- definitions;
- dependencies/evidence necessary to reconstruct.

It must not receive the first review verdict before issuing its own.

## Same-context fallback

If true context isolation is impossible:
1. create a verdict-blind packet;
2. start a separate pass;
3. prohibit reuse of prior verdict as premise;
4. record independence as `SAME_PROVIDER_SEQUENTIAL`.

## Rule

> Context separation can reduce correlated error; it does not create mathematical certainty.
