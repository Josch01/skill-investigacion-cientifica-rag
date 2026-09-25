#!/usr/bin/env python3
"""Static consistency checks for the Scientific Research RAG Council skill."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CANONICAL_SEMANTICS = (
    "exploratory_numeric|falsification_search|corroborative_numeric|"
    "symbolic_exact|exhaustive_finite|validated_numeric|"
    "rigorous_computer_assisted_proof"
)
CANONICAL_VERDICTS = "ACCEPT|REVISION_REQUIRED|SCIENTIFIC_REOPEN|BLOCKED"

REQUIRED_FILES = [
    "SKILL.md",
    "agents/ROUTER.md",
    "modules/MODULE_INDEX.md",
    "protocols/INTERPRETER.md",
    "protocols/PROOF.md",
    "protocols/PROOF_TACTICS.md",
    "protocols/NUMERICS.md",
    "protocols/CERTIFICATION.md",
    "protocols/OBJECTIVE_CLOSURE.md",
    "protocols/TASK_COMPILATION.md",
    "protocols/TASK_COORDINATION.md",
    "protocols/MULTI_AGENT_HANDOFF.md",
    "templates/TASK_PACKET.md",
    "templates/WORKER_MISSION.md",
    "templates/WORKER_RESULT.md",
    "templates/AUDIT_PACKET.md",
    "templates/PROOF_OBLIGATION.md",
    "templates/COMPUTATION_CERTIFICATE.md",
    "templates/CODEX_PLAN_DONE.json",
    "templates/WORKER_DONE.json",
    "templates/CODEX_AUDIT_DONE.json",
    "prompts/CODEX_BOOTSTRAP_LEAD_AUDITOR.md",
    "prompts/CODEX_SCHEDULED_TASK.md",
]

PATH_PREFIXES = ("agents/", "config/", "memory/", "modules/", "protocols/", "templates/", "prompts/")


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_referenced_paths(errors: list[str]) -> None:
    pattern = re.compile(r"`((?:agents|config|memory|modules|protocols|templates|prompts)/[^`\s]+)`")
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        content = md.read_text(encoding="utf-8")
        for ref in pattern.findall(content):
            ref = ref.rstrip(".,;:)")
            if ref.startswith(PATH_PREFIXES) and not (ROOT / ref).exists():
                fail(errors, f"broken reference: {md.relative_to(ROOT)} -> {ref}")


def check_json(errors: list[str]) -> None:
    for path in [
        "templates/TASK_STATE.json",
        "templates/CODEX_PLAN_DONE.json",
        "templates/WORKER_DONE.json",
        "templates/CODEX_AUDIT_DONE.json",
        "templates/MAILBOX_QUESTION.json",
        "templates/MAILBOX_ANSWER.json",
    ]:
        try:
            json.loads(text(path))
        except Exception as exc:
            fail(errors, f"invalid JSON: {path}: {exc}")


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not (ROOT / path).exists():
            fail(errors, f"missing required file: {path}")

    skill = text("SKILL.md")
    if 'version: "2.11.0"' not in skill:
        fail(errors, "SKILL.md metadata.version must be 2.11.0")

    for path in ["prompts/CODEX_BOOTSTRAP_LEAD_AUDITOR.md", "prompts/CODEX_SCHEDULED_TASK.md"]:
        content = text(path)
        if ">= 2.11.0" not in content:
            fail(errors, f"{path} must require >= 2.11.0")
        if ">= 2.10.0" in content:
            fail(errors, f"legacy version floor remains in {path}")

    for path in [
        "agents/ROUTER.md",
        "templates/MODULE_SELECTION.md",
        "templates/RESEARCH_OBJECTIVE.md",
        "templates/EXPERIMENT_RECORD.md",
        "memory/NUMERICAL_LEDGER.md",
        "templates/COMPUTATION_CERTIFICATE.md",
    ]:
        if CANONICAL_SEMANTICS not in text(path).replace(" ", ""):
            fail(errors, f"canonical Computation_semantics missing or drifted in {path}")

    for path in ["templates/AUDIT_PACKET.md", "protocols/MULTI_AGENT_HANDOFF.md", "prompts/CODEX_SCHEDULED_TASK.md"]:
        compact = text(path).replace(" ", "")
        if CANONICAL_VERDICTS not in compact:
            fail(errors, f"canonical audit verdicts missing or drifted in {path}")
        if "ACCEPT_WITH_NONSCIENTIFIC_PATCH" in compact:
            fail(errors, f"legacy audit verdict remains in {path}")

    if "CONTRACT_REVISION_REQUIRED" in text("modules/REVISION_ONLY.md"):
        fail(errors, "orphan CONTRACT_REVISION_REQUIRED remains in REVISION_ONLY")

    worker_done = json.loads(text("templates/WORKER_DONE.json"))
    if "mission_hash" not in worker_done:
        fail(errors, "WORKER_DONE.json missing mission_hash")
    if "task_execution_completed" not in worker_done:
        fail(errors, "WORKER_DONE.json missing task_execution_completed")
    if "objective_completed" in worker_done:
        fail(errors, "WORKER_DONE.json must not let worker assert objective_completed")

    mission = text("templates/WORKER_MISSION.md")
    for field in [
        "Objects_and_types:", "Success_criterion:", "Refutation_criterion_if_applicable:",
        "Proof_tactic_routing:", "Permitted_closure_methods:", "Computation_semantics_if_any:",
        "Rigorous_computation_standard_if_any:", "Allowed_actions:", "Forbidden_actions:",
        "Canonical_files_read_only:", "Worker_writable_paths:",
    ]:
        if field not in mission:
            fail(errors, f"WORKER_MISSION missing contract field {field}")

    numerics = text("protocols/NUMERICS.md")
    if "PROOF_TACTICS -> NUMERICS -> artifact/certificate -> obligation audit" not in numerics:
        fail(errors, "NUMERICS.md missing canonical acyclic proof-computation direction")

    objective = text("protocols/OBJECTIVE_CLOSURE.md")
    if "puente analítico certificado" in objective:
        fail(errors, "OBJECTIVE_CLOSURE still requires analytic-only bridge")
    if "puente matemático riguroso" not in objective:
        fail(errors, "OBJECTIVE_CLOSURE missing rigorous mathematical bridge language")

    check_json(errors)
    check_referenced_paths(errors)

    if errors:
        print("SKILL VALIDATION: FAIL")
        for item in errors:
            print(f"- {item}")
        return 1

    print("SKILL VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
