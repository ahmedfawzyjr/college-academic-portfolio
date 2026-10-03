"""
Unit Tests for Cross-Platform Smart Student Course & Schedule App (CS415)
"""

import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from engine import CS415Engine

class TestCS415Engine(unittest.TestCase):
    def setUp(self):
        self.engine = CS415Engine()

    def test_initialization(self):
        self.assertEqual(self.engine.course_code, "CS415")
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
