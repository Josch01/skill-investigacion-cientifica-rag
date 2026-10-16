#!/usr/bin/env python3
"""Deterministic v3.1 lifecycle invariants. Scientific correctness still needs human review.

Usage: python scripts/validate_research_lifecycle.py path/to/research_graph.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

VERSION = {"3.1.0"}
STATES = (
    "TOPIC_UNDELIMITED",
    "SOURCE_VERIFICATION_PENDING",
    "PROPERTY_SELECTED",
    "SCOPE_PROVISIONAL",
    "LITERATURE_REVIEW_PENDING",
    "ROUTES_PENDING",
    "OBJECTIVE_PROPOSED",
    "OBJECTIVE_APPROVED",
)
TRANSITIONS = {
    "TOPIC_UNDELIMITED": {"SOURCE_VERIFICATION_PENDING", "PROPERTY_SELECTED"},
    "SOURCE_VERIFICATION_PENDING": {"PROPERTY_SELECTED", "SCOPE_PROVISIONAL"},
    "PROPERTY_SELECTED": {"SOURCE_VERIFICATION_PENDING", "SCOPE_PROVISIONAL"},
    "SCOPE_PROVISIONAL": {"LITERATURE_REVIEW_PENDING"},
    "LITERATURE_REVIEW_PENDING": {"ROUTES_PENDING"},
    "ROUTES_PENDING": {"OBJECTIVE_PROPOSED", "LITERATURE_REVIEW_PENDING"},
    "OBJECTIVE_PROPOSED": {"OBJECTIVE_APPROVED", "ROUTES_PENDING"},
    "OBJECTIVE_APPROVED": {"ROUTES_PENDING", "OBJECTIVE_PROPOSED"},
}
NODE_TYPES = {"OBJECTIVE", "CLAIM", "OBLIGATION", "EVIDENCE", "ROUTE", "OBJECTION", "COMPUTATION", "CERTIFICATE"}
APP_STATUSES = {"APPLICABLE", "CONDITIONALLY_APPLICABLE", "NOT_APPLICABLE", "UNVERIFIED"}
CLAIM_STATES = {"DRAFT", "VERIFIED", "CERTIFIED", "CONDITIONAL", "PARTIAL",
                "REFUTED", "SUPERSEDED", "STALE", "NEEDS_REVALIDATION"}
OBL_STATES = {"OPEN", "EVIDENCE_ONLY", "CONDITIONAL", "RIGOROUSLY_CLOSED", "REFUTED"}
INDEPENDENCE = {"CROSS_PROVIDER_SEPARATE_CONTEXT", "SAME_PROVIDER_SEPARATE_CONTEXT",
                "SAME_PROVIDER_SEQUENTIAL"}
PUBLISHED = {"PUBLISHED_VERIFIED", "PREPRINT_VERIFIED", "UNVERIFIED", "WITHDRAWN"}


def populated(value: object) -> bool:
    return value is not None and value != "" and value != [] and value != {}


def validate(data: object) -> list[str]:
    errors: list[str] = []
    def err(message: str) -> None:
        errors.append(message)
    if not isinstance(data, dict):
        return ["root must be a JSON object"]
    if data.get("schema_version") not in VERSION:
        err("schema_version must be 3.1.0")
    if not populated(data.get("project_id")):
        err("project_id is required")

    for field in ("literature", "routes", "objects", "nodes", "edges", "theorem_applications"):
        if not isinstance(data.get(field), list):
            err(f"{field} must be a list")
    if any(not isinstance(data.get(k), list) for k in
           ("literature", "routes", "objects", "nodes", "edges", "theorem_applications")):
        return errors

    scope = data.get("scoping", {})
    if not isinstance(scope, dict):
        err("scoping must be an object")
        scope = {}
    state = scope.get("state")
    if state not in STATES:
        err(f"invalid scoping state: {state}")
    history = scope.get("history", [])
    if not isinstance(history, list):
        err("scoping history must be an array")
    else:
        last = None
        for i, event in enumerate(history):
            if not isinstance(event, dict):
                err(f"history[{i}] must be an object")
                continue
            fr, to = event.get("from"), event.get("to")
            if fr not in TRANSITIONS or to not in TRANSITIONS.get(fr, set()):
                err(f"history[{i}]: invalid transition {fr} -> {to}")
            if last is not None and fr != last:
                err(f"history[{i}]: disconnected transition")
            if not populated(event.get("reason")):
                err(f"history[{i}]: missing decision reason")
            last = to
        if last is not None and last != state:
            err("scoping state differs from last history transition")

    ids: set[str] = set()
    def unique(rec: dict, category: str, i: int) -> None:
        ident = rec.get("id")
        if not isinstance(ident, str) or not ident.strip():
            err(f"{category}[{i}] missing id")
        elif ident in ids:
            err(f"duplicate ID {ident}")
        else:
            ids.add(ident)

    literature: dict[str, dict] = {}
    for i, ref in enumerate(data["literature"]):
        if not isinstance(ref, dict):
            err(f"literature[{i}] must be an object")
            continue
        unique(ref, "literature", i)
        status = ref.get("status")
        if status not in PUBLISHED:
            err(f"literature[{i}]: invalid status")
        if status == "PUBLISHED_VERIFIED":
            for key in ("title", "authors", "year", "venue", "publisher_record", "verified_by"):
                if not populated(ref.get(key)):
                    err(f"{ref.get('id')}: published record missing {key}")
            if not (populated(ref.get("doi")) or populated(ref.get("isbn")) or
                    populated(ref.get("publisher_url"))):
                err(f"{ref.get('id')}: published record lacks persistent publisher identifier")
        if isinstance(ref.get("id"), str):
            literature[ref["id"]] = ref

    routes: dict[str, dict] = {}
    if len(data["routes"]) > 4:
        err("at most four ACTIVE route candidates per scoping cycle; archive earlier versions separately")
    for i, route in enumerate(data["routes"]):
        if not isinstance(route, dict):
            err(f"routes[{i}] must be an object")
            continue
        unique(route, "routes", i)
        for ref_id in route.get("prior_art_refs", []):
            if ref_id not in literature:
                err(f"{route.get('id')}: missing prior-art record {ref_id}")
        if route.get("approval") == "APPROVED":
            for key in ("scientific_question", "gap_evidence", "risks", "falsification_criterion"):
                if not populated(route.get(key)):
                    err(f"{route.get('id')}: approved route missing {key}")
            if not route.get("prior_art_refs"):
                err(f"{route.get('id')}: approved route lacks prior-art comparison")
        if isinstance(route.get("id"), str):
            routes[route["id"]] = route

    if state == "OBJECTIVE_APPROVED":
        obj = scope.get("objective", {})
        if not isinstance(obj, dict):
            err("approved objective must be an object")
            obj = {}
        for key in ("claim", "domain", "quantifiers", "hypotheses", "success_criterion",
                    "refutation_criterion", "delimitations"):
            if not populated(obj.get(key)):
                err(f"approved objective missing {key}")
        rid = scope.get("selected_route_id")
        if rid not in routes or routes[rid].get("approval") != "APPROVED":
            err("approved objective requires one selected APPROVED route")

    objects: list[dict] = []
    for i, obj in enumerate(data["objects"]):
        if not isinstance(obj, dict):
            err(f"objects[{i}] must be an object")
            continue
        unique(obj, "objects", i)
        for key in ("symbol", "type", "meaning", "scope"):
            if not populated(obj.get(key)):
                err(f"objects[{i}] missing {key}")
        objects.append(obj)
    for i, a in enumerate(objects):
        for b in objects[i+1:]:
            if (a.get("symbol") and a.get("symbol") == b.get("symbol")
                and a.get("scope") == b.get("scope")
                and a.get("id") != b.get("alias_of")
                and b.get("id") != a.get("alias_of")):
                err(f"notation collision {a.get('symbol')}: {a.get('id')} vs {b.get('id')} in {a.get('scope')}")
    for obj in objects:
        if populated(obj.get("alias_of")) and obj["alias_of"] not in {x.get("id") for x in objects}:
            err(f"{obj.get('id')}: alias_of target missing")

    nodes: dict[str, dict] = {}
    for i, node in enumerate(data["nodes"]):
        if not isinstance(node, dict):
            err(f"nodes[{i}] must be an object")
            continue
        unique(node, "nodes", i)
        nid = node.get("id")
        if node.get("type") not in NODE_TYPES:
            err(f"node {nid}: unknown type")
        if node.get("type") == "CLAIM" and node.get("status") not in CLAIM_STATES:
            err(f"claim {nid}: unknown status")
        if node.get("type") == "OBLIGATION" and node.get("status") not in OBL_STATES:
            err(f"obligation {nid}: unknown status")
        if not populated(node.get("provenance")):
            err(f"node {nid}: provenance required")
        if isinstance(nid, str):
            nodes[nid] = node

    for i, edge in enumerate(data["edges"]):
        if not isinstance(edge, dict):
            err(f"edges[{i}] must be an object")
            continue
        if edge.get("source") not in nodes or edge.get("target") not in nodes:
            err(f"edges[{i}]: dangling node")
        if not populated(edge.get("relation")):
            err(f"edges[{i}]: missing relation")
    adj: dict[str, list[str]] = {n: [] for n in nodes}
    for edge in data["edges"]:
        if isinstance(edge, dict) and edge.get("relation") == "requires" and edge.get("source") in nodes and edge.get("target") in nodes:
            adj[edge["source"]].append(edge["target"])
    visited: set[str] = set()
    active: set[str] = set()
    def walk(node_id: str) -> None:
        if node_id in active:
            err(f"dependency cycle at {node_id}")
            return
        if node_id in visited:
            return
        visited.add(node_id)
        active.add(node_id)
        for child in adj[node_id]:
            walk(child)
        active.remove(node_id)
    for nid in nodes:
        walk(nid)

    for nid, claim in nodes.items():
        if claim.get("type") != "CLAIM" or claim.get("status") != "CERTIFIED":
            continue
        for key in ("statement", "hypotheses", "scope", "proof_artifact"):
            if not populated(claim.get(key)):
                err(f"{nid}: CERTIFIED claim missing {key}")
        rev = claim.get("second_review", {})
        if not isinstance(rev, dict) or rev.get("verdict") != "CONFIRMS" or not populated(rev.get("artifact")) or rev.get("independence") not in INDEPENDENCE:
            err(f"{nid}: missing adequate second-review record")
        for edge in data["edges"]:
            if not isinstance(edge, dict) or edge.get("source") != nid or edge.get("relation") != "requires" or not edge.get("essential"):
                continue
            dep = nodes.get(edge.get("target"), {})
            if dep.get("type") == "OBLIGATION" and (dep.get("status") != "RIGOROUSLY_CLOSED" or not populated(dep.get("certificate"))):
                err(f"{nid}: essential obligation {dep.get('id')} not rigorously satisfied")
            elif dep.get("type") == "CLAIM" and dep.get("status") != "CERTIFIED":
                err(f"{nid}: essential claim dependency {dep.get('id')} not certified")

    for i, app in enumerate(data["theorem_applications"]):
        if not isinstance(app, dict):
            err(f"theorem_applications[{i}] must be an object")
            continue
        unique(app, "theorem_applications", i)
        ref = app.get("source_ref_id")
        if ref not in literature:
            err(f"theorem application {app.get('id')}: missing source {ref}")
        status = app.get("status")
        if status not in APP_STATUSES:
            err(f"theorem application {app.get('id')}: invalid status")
        conditions = app.get("conditions", [])
        if not isinstance(conditions, list):
            err(f"theorem application {app.get('id')}: conditions must be a list")
            continue
        if status == "APPLICABLE":
            if not conditions or any(not isinstance(c, dict) or c.get("status") != "VERIFIED" or not populated(c.get("evidence")) for c in conditions):
                err(f"theorem application {app.get('id')}: unmet/missing theorem hypotheses")
            if not populated(app.get("theorem_statement")) or not populated(app.get("source_location")):
                err(f"theorem application {app.get('id')}: theorem statement/location missing")
            if app.get("conclusion_bridge_verified") is not True:
                err(f"theorem application {app.get('id')}: conclusion-to-target bridge unverified")
            if literature.get(ref, {}).get("full_text_verified") is not True:
                err(f"theorem application {app.get('id')}: source theorem text not verified")

    manuscript = data.get("manuscript", {})
    if not isinstance(manuscript, dict):
        err("manuscript must be an object")
        manuscript = {}
    if manuscript.get("status") == "MANUSCRIPT_READY":
        if state != "OBJECTIVE_APPROVED":
            err("MANUSCRIPT_READY requires approved objective")
        for flag in ("semantic_diff_pass", "notation_pass", "latex_compile_pass", "bibliography_verified"):
            if manuscript.get(flag) is not True:
                err(f"MANUSCRIPT_READY requires {flag}")
        for cid in manuscript.get("claim_ids", []):
            if cid not in nodes or nodes[cid].get("type") != "CLAIM" or nodes[cid].get("status") != "CERTIFIED":
                err(f"MANUSCRIPT_READY contains uncertified central claim {cid}")
        for rid in manuscript.get("bibliography_ids", []):
            if literature.get(rid, {}).get("status") != "PUBLISHED_VERIFIED":
                err(f"MANUSCRIPT_READY bibliography not published/verified {rid}")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_research_lifecycle.py RESEARCH_GRAPH.json")
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        print(f"RESEARCH LIFECYCLE: FAIL - {exc}")
        return 1
    errors = validate(data)
    if errors:
        print("RESEARCH LIFECYCLE: FAIL")
        for item in errors:
            print(f"- {item}")
        return 1
    print("RESEARCH LIFECYCLE: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
