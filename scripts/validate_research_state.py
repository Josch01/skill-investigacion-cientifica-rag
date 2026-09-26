#!/usr/bin/env python3
"""Validate a v3.0 Scientific Consortium blackboard JSON file."""

from __future__ import annotations

import json
import sys
from pathlib import Path

NODE_TYPES = {
    "OBJECTIVE", "CLAIM", "OBLIGATION", "ROUTE", "EVIDENCE",
    "OBJECTION", "DISPUTE", "COMPUTATION", "CERTIFICATE",
}

INDEPENDENCE = {
    "CROSS_PROVIDER_SEPARATE_CONTEXT",
    "SAME_PROVIDER_SEPARATE_CONTEXT",
    "SAME_PROVIDER_SEQUENTIAL",
    "NONE",
}

EXECUTION_MODES = {
    "AUTO",
    "LEGACY_V2_12",
    "MULTI_PROVIDER_COUNCIL",
    "SINGLE_PROVIDER_MULTI_CONTEXT",
    "SINGLE_PROVIDER_SEQUENTIAL",
    "LIGHTWEIGHT",
}

CLOSED_OBLIGATION = {"RIGOROUSLY_CLOSED", "REFUTED"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_research_state.py PATH_TO_BLACKBOARD.json")
        return 2

    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"BLACKBOARD VALIDATION: FAIL\n- cannot read JSON: {exc}")
        return 1

    errors: list[str] = []

    if data.get("framework_version") != "3.0.0":
        fail(errors, "framework_version must be 3.0.0")

    if data.get("execution_mode") not in EXECUTION_MODES:
        fail(errors, f"invalid execution_mode: {data.get('execution_mode')}")

    if data.get("independence_level") not in INDEPENDENCE:
        fail(errors, f"invalid independence_level: {data.get('independence_level')}")

    nodes = data.get("nodes")
    edges = data.get("edges")
    if not isinstance(nodes, list):
        fail(errors, "nodes must be a list")
        nodes = []
    if not isinstance(edges, list):
        fail(errors, "edges must be a list")
        edges = []

    ids: set[str] = set()
    node_map: dict[str, dict] = {}
    for node in nodes:
        if not isinstance(node, dict):
            fail(errors, "every node must be an object")
            continue
        nid = node.get("id")
        ntype = node.get("type")
        if not nid:
            fail(errors, "node missing id")
            continue
        if nid in ids:
            fail(errors, f"duplicate node id: {nid}")
        ids.add(nid)
        node_map[nid] = node
        if ntype not in NODE_TYPES:
            fail(errors, f"{nid}: invalid node type {ntype}")
        if not node.get("status"):
            fail(errors, f"{nid}: missing status")
        if "provenance" not in node:
            fail(errors, f"{nid}: missing provenance")

    for edge in edges:
        if not isinstance(edge, dict):
            fail(errors, "every edge must be an object")
            continue
        source = edge.get("source")
        target = edge.get("target")
        if source not in ids:
            fail(errors, f"edge source not found: {source}")
        if target not in ids:
            fail(errors, f"edge target not found: {target}")
        if not edge.get("relation"):
            fail(errors, f"edge {source}->{target} missing relation")

    # Certification invariant:
    # a CERTIFIED claim cannot require an essential open obligation.
    for node in nodes:
        if node.get("type") != "CLAIM" or node.get("status") != "CERTIFIED":
            continue
        cid = node.get("id")
        for edge in edges:
            if edge.get("source") != cid:
                continue
            if edge.get("relation") != "requires":
                continue
            if not edge.get("essential", False):
                continue
            target = node_map.get(edge.get("target"), {})
            if target.get("type") == "OBLIGATION" and target.get("status") not in CLOSED_OBLIGATION:
                fail(errors, f"{cid}: CERTIFIED but essential obligation {target.get('id')} is {target.get('status')}")

    for dispute in data.get("disputes", []):
        if not isinstance(dispute, dict):
            fail(errors, "every dispute must be an object")
            continue
        status = dispute.get("status")
        if status and status.startswith("RESOLVED") and not dispute.get("resolution_artifact"):
            fail(errors, f"{dispute.get('id','<dispute>')}: resolved without resolution_artifact")

    if errors:
        print("BLACKBOARD VALIDATION: FAIL")
        for item in errors:
            print(f"- {item}")
        return 1

    print("BLACKBOARD VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
