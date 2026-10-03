"""
Unit Tests for Interactive Academic Web Portal & Student Dashboard (CS313)
"""

import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from engine import CS313Engine

class TestCS313Engine(unittest.TestCase):
    def setUp(self):
        self.engine = CS313Engine()

    def test_initialization(self):
        self.assertEqual(self.engine.course_code, "CS313")
        self.assertEqual(len(self.engine.get_topics()), 6)

    def test_processing(self):
        res = self.engine.process_data("sample_payload")
        self.assertEqual(res["status"], "PROCESSED")
        self.assertTrue(res["verified"])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.engine.process_data(None)

if __name__ == '__main__':
    unittest.main()
