"""Scientific real-world seed article smoke test."""
import json
import unittest
from fractions import Fraction
from pathlib import Path
from scripts.validate_research_lifecycle import validate

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "examples" / "case-studies" / "jerk-sinh-2022" / "research_graph.json"

class JerkResearchCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p = json.loads(GRAPH.read_text(encoding="utf-8"))

    def test_scoping_structure_without_fake_approval(self):
        self.assertEqual(validate(self.p), [])
        self.assertEqual(self.p["scoping"]["state"],"ROUTES_PENDING")
        self.assertEqual(self.p["scoping"]["selected_route_id"],"")
        self.assertFalse(self.p["audit"]["user_objective_approved"])

    def test_published_records_vs_primary_inspection(self):
        sources = self.p["literature"]
        self.assertGreaterEqual(len(sources), 3)
        self.assertEqual(sum(x["full_text_verified"] for x in sources), 1)
        self.assertTrue(all(x["status"]=="PUBLISHED_VERIFIED" for x in sources))

    def test_routh_exact_applicability(self):
        d,b,c = Fraction(1),Fraction(1),Fraction(1,5)
        a_valid, a_invalid = Fraction(11,10),Fraction(167,100)
        upper = d+c*b*b
        self.assertTrue(d < a_valid < upper)
        self.assertFalse(d < a_invalid < upper)
        statuses={x["id"]:x["status"] for x in self.p["theorem_applications"]}
        self.assertEqual(statuses["APP-HURWITZ-VALID"],"APPLICABLE")
        self.assertEqual(statuses["APP-HURWITZ-INVALID"],"NOT_APPLICABLE")

    def test_negative_divergence_counterexample_exact(self):
        c=Fraction(1,5)
        x=Fraction(3,2)
        divergence=(2*x)+(-2*x-c)
        self.assertEqual(divergence,-c)
        x0=Fraction(2)
        t=Fraction(1,4)
        solution=x0/(1-x0*t)
        self.assertEqual(solution, Fraction(4))
        self.assertEqual(Fraction(1,x0),Fraction(1,2))

    def test_no_fake_certification_or_manuscript(self):
        self.assertEqual(self.p["manuscript"]["status"],"NOT_STARTED")
        self.assertFalse(any(n["type"]=="CLAIM" and n["status"]=="CERTIFIED"
                             for n in self.p["nodes"]))

if __name__=="__main__":
    unittest.main()
