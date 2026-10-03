"""
Unit Tests for Double-Entry Ledger & Financial Statement Generator (HU201)
"""

import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from engine import HU201Engine

class TestHU201Engine(unittest.TestCase):
    def setUp(self):
        self.engine = HU201Engine()

    def test_initialization(self):
        self.assertEqual(self.engine.course_code, "HU201")
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
