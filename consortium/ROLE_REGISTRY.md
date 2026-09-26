# Consortium Role Registry

Functional roles are runtime hats. Canonical authority still follows `config/AGENT_AUTHORITY.md`.

| Functional role | Canonical authority | Purpose | May certify? |
|---|---|---|---|
| Research Architect | SCIENTIFIC_LEAD | formalize objective, graph, routes | no |
| Theory Scout | bounded worker/research role | retrieve prior results | no |
| Applicability Judge | SCIENTIFIC_LEAD or AUDITOR pass | check theorem hypotheses exactly | no |
| Proof Engineer | SCIENTIFIC_LEAD for R3 reasoning | close one obligation | no |
| Tactic Selector | SCIENTIFIC_LEAD | choose closure tactic per obligation | no |
| Computational Strategist | SCIENTIFIC_LEAD + Numerical input | decide whether/how computation helps | no |
| Numerical/Symbolic Worker | NUMERICAL_WORKER/CODE_WORKER | execute bounded computation | no |
| Falsifier / Red Team | SCIENTIFIC_AUDITOR | seek counterexamples/obstructions | no |
| Adjudicator | SCIENTIFIC_LEAD | turn disagreement into resolution obligation | no |
| Independent Reviewer | SCIENTIFIC_AUDITOR with declared independence mode | rederive critical claims | no |
| Certifier | protocol/gate function | apply Certification Gate | only via gate |

## Role separation

A provider may implement several roles, but the execution report must state context separation and independence level.

## No authority drift

A worker saying "proved" or "certified" is a proposal, not canonical status.
