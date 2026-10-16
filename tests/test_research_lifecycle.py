"""Regression checks for v3.1 lifecycle gates (stdlib only)."""
import copy
import json
import unittest
from pathlib import Path
from scripts.validate_research_lifecycle import validate

BASE = json.loads((Path(__file__).resolve().parents[1] / "templates/RESEARCH_GRAPH.json").read_text())

def project():
    return copy.deepcopy(BASE)

def published():
    return {"id":"REF-1","status":"PUBLISHED_VERIFIED","title":"Example",
            "authors":["Researcher"],"year":2022,"venue":"Journal",
            "publisher_record":"publisher metadata verified","verified_by":"Crossref DOI",
            "doi":"10.1000/example","full_text_verified":True}

def approved():
    p=project()
    p["literature"]=[published()]
    p["routes"]=[{"id":"ROUTE-1","approval":"APPROVED","scientific_question":"P?",
        "gap_evidence":"Compared with REF-1","prior_art_refs":["REF-1"],
        "risks":"Hypothesis may fail","falsification_criterion":"counterexample"}]
    p["scoping"].update({"state":"OBJECTIVE_APPROVED","selected_route_id":"ROUTE-1",
        "objective":{"claim":"P","domain":"R","quantifiers":"forall x","hypotheses":["H"],
                     "success_criterion":"proof","refutation_criterion":"counterexample",
                     "delimitations":"local"}})
    return p

def certified(p):
    p["nodes"]=[
        {"id":"C-1","type":"CLAIM","status":"CERTIFIED","provenance":"PROOF-1",
         "statement":"P","hypotheses":["H"],"scope":"local","proof_artifact":"PROOF-1",
         "second_review":{"verdict":"CONFIRMS","artifact":"SECOND-1",
                          "independence":"SAME_PROVIDER_SEQUENTIAL"}},
        {"id":"O-1","type":"OBLIGATION","status":"RIGOROUSLY_CLOSED",
         "provenance":"PROOF-1","certificate":"CERT-1"}]
    p["edges"]=[{"source":"C-1","target":"O-1","relation":"requires","essential":True}]
    return p

class LifecycleTests(unittest.TestCase):
    def assert_bad(self,p,fragment):
        self.assertTrue(any(fragment in e for e in validate(p)),validate(p))
    def test_empty_template(self):
        self.assertEqual(validate(project()),[])
    def test_valid_approved_objective(self):
        self.assertEqual(validate(approved()),[])
    def test_approved_requires_route(self):
        p=approved();p["scoping"]["selected_route_id"]="missing"
        self.assert_bad(p,"selected APPROVED route")
    def test_published_requires_provenance(self):
        p=approved();del p["literature"][0]["publisher_record"]
        self.assert_bad(p,"publisher_record")
    def test_unverified_is_not_published(self):
        p=approved();p["literature"][0]["status"]="UNVERIFIED"
        p["manuscript"].update({"status":"MANUSCRIPT_READY","semantic_diff_pass":True,
        "notation_pass":True,"latex_compile_pass":True,"bibliography_verified":True,
        "bibliography_ids":["REF-1"]})
        self.assert_bad(p,"not published/verified")
    def test_more_than_four_routes(self):
        p=project();p["routes"]=[{"id":f"R-{i}"} for i in range(5)]
        self.assert_bad(p,"at most four")
    def test_refuted_obligation_blocks_certified(self):
        p=certified(approved());p["nodes"][1]["status"]="REFUTED"
        self.assert_bad(p,"not rigorously satisfied")
    def test_open_obligation_blocks_certified(self):
        p=certified(approved());p["nodes"][1]["status"]="OPEN"
        self.assert_bad(p,"not rigorously satisfied")
    def test_certified_with_satisfied_obligation(self):
        self.assertEqual(validate(certified(approved())),[])
    def test_missing_second_review(self):
        p=certified(approved());p["nodes"][0]["second_review"]={}
        self.assert_bad(p,"second-review")
    def test_notation_collision(self):
        p=project();p["objects"]=[
            {"id":"X","symbol":"theta","meaning":"angle","type":"scalar","scope":"global"},
            {"id":"Y","symbol":"theta","meaning":"function","type":"function","scope":"global"}]
        self.assert_bad(p,"notation collision")
    def test_local_scope_is_distinct(self):
        p=project();p["objects"]=[
            {"id":"X","symbol":"theta","meaning":"angle","type":"scalar","scope":"theorem_A"},
            {"id":"Y","symbol":"theta","meaning":"function","type":"function","scope":"theorem_B"}]
        self.assertEqual(validate(p),[])
    def test_applicability_missing_hypothesis(self):
        p=approved();p["theorem_applications"]=[{"id":"APP-1","source_ref_id":"REF-1",
            "status":"APPLICABLE","theorem_statement":"H implies Q",
            "source_location":"section 2","conditions":[{"status":"UNVERIFIED","evidence":""}],
            "conclusion_bridge_verified":True}]
        self.assert_bad(p,"unmet/missing theorem hypotheses")
    def test_applicability_verified(self):
        p=approved();p["theorem_applications"]=[{"id":"APP-1","source_ref_id":"REF-1",
            "status":"APPLICABLE","theorem_statement":"H implies Q",
            "source_location":"section 2","conditions":[{"status":"VERIFIED","evidence":"LEM-1"}],
            "conclusion_bridge_verified":True}]
        self.assertEqual(validate(p),[])
    def test_refutation_not_theorem_failure(self):
        p=project();p["theorem_applications"]=[{"id":"APP-1","source_ref_id":"missing",
            "status":"NOT_APPLICABLE","conditions":[]}]
        self.assert_bad(p,"missing source")
    def test_invalid_history_transition(self):
        p=project();p["scoping"]["history"]=[{"from":"TOPIC_UNDELIMITED",
                   "to":"OBJECTIVE_APPROVED","reason":"jump"}]
        self.assert_bad(p,"invalid transition")
    def test_cycle_in_proof_graph(self):
        p=certified(approved());p["edges"].append({"source":"O-1","target":"C-1","relation":"requires"})
        self.assert_bad(p,"dependency cycle")
    def test_ready_manuscript_rejects_unverified_claim(self):
        p=approved();p["nodes"]=[{"id":"C-1","type":"CLAIM","status":"DRAFT","provenance":"draft"}]
        p["manuscript"].update({"status":"MANUSCRIPT_READY","semantic_diff_pass":True,
            "notation_pass":True,"latex_compile_pass":True,"bibliography_verified":True,
            "claim_ids":["C-1"]})
        self.assert_bad(p,"uncertified central claim")
    def test_malformed_node_graceful(self):
        p=project();p["nodes"]=[None]
        self.assert_bad(p,"must be an object")

if __name__ == "__main__":
    unittest.main()
