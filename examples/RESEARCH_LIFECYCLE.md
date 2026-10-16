# v3.1 project starter — demonstration only

The v3.1 project graph is a local evidence/decision index, not scientific certification. Do not place an active user's memory in the global skill templates.

## Initialize a project

~~~sh
python scripts/research_project.py init projects/jerk-sinh/research_graph.json --project-id JERK-SINH-01 --topic "Jerk sinh system"
python scripts/research_project.py status projects/jerk-sinh/research_graph.json
~~~

The first content state is TOPIC_UNDELIMITED. The scientific assistant should run RESEARCH_INTAKE to establish article identity and user-selected property, then update the project document and move **one justified transition at a time**.

~~~sh
python scripts/research_project.py advance projects/jerk-sinh/research_graph.json --to PROPERTY_SELECTED --reason "Researcher selected unstable periodic orbits"
python scripts/validate_research_lifecycle.py projects/jerk-sinh/research_graph.json
~~~

To approve a research objective, first include a verified published literature map, selected research route with gap/countersearch and an objective with domain/quantifiers/hypotheses/criterion. The deterministic validator prevents arbitrary promotion.

External scholarly search and full-text analysis require an agent runtime with those tools. Numerical work and LaTeX rendering use the existing PROOF/NUMERICS/MANUSCRIPT_EDIT and journal policies. Tests: python -m unittest discover -s tests -v.
