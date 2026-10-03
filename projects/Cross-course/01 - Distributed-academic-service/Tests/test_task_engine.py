"""
Unit Tests for Distributed Academic Task Engine
"""

import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from task_engine import AcademicTaskEngine

class TestTaskEngine(unittest.TestCase):
    def test_priority_order(self):
        engine = AcademicTaskEngine()
        engine.submit_task("t_low", priority=1, payload={"action": "routine_audit"})
        engine.submit_task("t_urgent", priority=10, payload={"action": "grade_release"})
        engine.submit_task("t_medium", priority=5, payload={"action": "attendance_sync"})

        self.assertEqual(engine.get_queue_size(), 3)

        # Urgent (10) must be popped first
        first = engine.process_next()
        self.assertEqual(first["task_id"], "t_urgent")

        # Medium (5) second
        second = engine.process_next()
        self.assertEqual(second["task_id"], "t_medium")

        # Low (1) third
        third = engine.process_next()
        self.assertEqual(third["task_id"], "t_low")

        self.assertIsNone(engine.process_next())

if __name__ == '__main__':
    unittest.main()
