"""Project-local CLI tests, including atomic no-clobber."""
import json
import tempfile
import unittest
from pathlib import Path
from scripts.research_project import initialize, transition, load

class ProjectCLITests(unittest.TestCase):
    def test_initialize_and_advance(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "project.json"
            initialize(p,"PROJECT-1","Jerk sinh system")
            self.assertEqual(load(p)["scoping"]["state"],"TOPIC_UNDELIMITED")
            transition(p,"PROPERTY_SELECTED","Selected UPO study")
            self.assertEqual(load(p)["scoping"]["state"],"PROPERTY_SELECTED")
            self.assertEqual(len(load(p)["scoping"]["history"]),1)
    def test_illegal_jump_is_atomic(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"project.json";initialize(p,"PROJECT-2","")
            old=p.read_text()
            with self.assertRaises(ValueError):
                transition(p,"OBJECTIVE_APPROVED","jumping")
            self.assertEqual(p.read_text(),old)
    def test_do_not_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"project.json";initialize(p,"PROJECT-3","")
            with self.assertRaises(FileExistsError):
                initialize(p,"PROJECT-3","")

if __name__=="__main__":
    unittest.main()
