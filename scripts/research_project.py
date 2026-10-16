#!/usr/bin/env python3
"""Small project-local CLI for lifecycle state; does not conduct research on its own."""
from __future__ import annotations

import argparse
import copy
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

if __package__:
    from .validate_research_lifecycle import STATES, TRANSITIONS, validate
else:
    from validate_research_lifecycle import STATES, TRANSITIONS, validate

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "RESEARCH_GRAPH.json"


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("project file must be a JSON object")
    return value


def atomic_write(path: Path, data: dict) -> None:
    errors = validate(data)
    if errors:
        raise ValueError("invalid lifecycle state: " + "; ".join(errors))
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, prefix="." + path.name + ".",
        suffix=".tmp", delete=False,
    ) as output:
        tmp_name = output.name
        json.dump(data, output, ensure_ascii=False, indent=2)
        output.write("\n")
    try:
        os.replace(tmp_name, path)
    finally:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)


def initialize(path: Path, project_id: str, topic: str) -> None:
    if path.exists():
        raise FileExistsError(f"project already exists: {path}")
    if not project_id.strip():
        raise ValueError("project_id cannot be empty")
    data = copy.deepcopy(load(TEMPLATE))
    data["project_id"] = project_id.strip()
    data["scoping"]["topic"] = topic.strip()
    atomic_write(path, data)


def transition(path: Path, next_state: str, reason: str) -> None:
    data = load(path)
    previous = data.get("scoping", {}).get("state")
    if next_state not in STATES:
        raise ValueError(f"unknown state: {next_state}")
    if next_state not in TRANSITIONS.get(previous, set()):
        raise ValueError(f"illegal transition {previous} -> {next_state}")
    if not reason.strip():
        raise ValueError("transition reason required")
    data["scoping"].setdefault("history", []).append({
        "from": previous, "to": next_state, "reason": reason.strip(),
        "recorded_at": datetime.now(timezone.utc).isoformat(),
    })
    data["scoping"]["state"] = next_state
    atomic_write(path, data)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init")
    init.add_argument("file", type=Path)
    init.add_argument("--project-id", required=True)
    init.add_argument("--topic", default="")
    advance = sub.add_parser("advance")
    advance.add_argument("file", type=Path)
    advance.add_argument("--to", required=True, choices=STATES)
    advance.add_argument("--reason", required=True)
    check = sub.add_parser("status")
    check.add_argument("file", type=Path)

    args = parser.parse_args()
    try:
        if args.command == "init":
            initialize(args.file, args.project_id, args.topic)
        elif args.command == "advance":
            transition(args.file, args.to, args.reason)
        else:
            data = load(args.file)
            errors = validate(data)
            print(json.dumps({"project_id": data.get("project_id"),
                              "state": data.get("scoping", {}).get("state"),
                              "literature_count": len(data.get("literature", [])),
                              "active_routes": len(data.get("routes", [])),
                              "claims": sum(isinstance(n, dict) and n.get("type") == "CLAIM"
                                            for n in data.get("nodes", [])),
                              "valid": not errors, "errors": errors}, ensure_ascii=False, indent=2))
            return 0 if not errors else 1
        print(f"OK: {args.file}")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
