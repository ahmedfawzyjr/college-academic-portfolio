"""
Unit Tests for Quine-McCluskey Boolean Minimizer & Digital Circuit Synthesizer (EE242)
"""

import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from engine import EE242Engine

class TestEE242Engine(unittest.TestCase):
    def setUp(self):
        self.engine = EE242Engine()

    def test_initialization(self):
        self.assertEqual(self.engine.course_code, "EE242")
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
