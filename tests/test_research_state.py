"""Legacy and v3.1 state validation regression tests."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_research_state.py"

def run(payload):
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "state.json"
        path.write_text(json.dumps(payload))
        return subprocess.run([sys.executable, str(SCRIPT), str(path)],
                              capture_output=True, text=True)

def state(version="3.1.0", status="RIGOROUSLY_CLOSED"):
    return {"framework_version":version,"execution_mode":"AUTO",
            "independence_level":"NONE","nodes":[
                {"id":"C1","type":"CLAIM","status":"CERTIFIED","provenance":"CERT1"},
                {"id":"O1","type":"OBLIGATION","status":status,"provenance":"PO1"}],
            "edges":[{"source":"C1","target":"O1","relation":"requires","essential":True}],
            "disputes":[]}

class BlackboardTests(unittest.TestCase):
    def test_rigorously_closed(self):
        self.assertEqual(run(state()).returncode,0)
    def test_refuted_is_not_satisfied(self):
        r=run(state(status="REFUTED"))
        self.assertNotEqual(r.returncode,0)
        self.assertIn("essential obligation",r.stdout)
    def test_open_is_not_satisfied(self):
        self.assertNotEqual(run(state(status="OPEN")).returncode,0)
    def test_legacy_version_still_readable(self):
        self.assertEqual(run(state(version="3.0.0")).returncode,0)
    def test_non_object_node_is_clean_failure(self):
        p=state();p["nodes"].append(None)
        r=run(p)
        self.assertEqual(r.returncode,1)
        self.assertNotIn("Traceback",r.stderr)

if __name__=="__main__":
    unittest.main()
