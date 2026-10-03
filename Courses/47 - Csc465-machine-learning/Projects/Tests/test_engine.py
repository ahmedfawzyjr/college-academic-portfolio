"""
Unit Tests for End-to-End Machine Learning Model Training & Evaluation Pipeline (CSC465-ML)
"""

import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from engine import CSC465-MLEngine

class TestCSC465-MLEngine(unittest.TestCase):
    def setUp(self):
        self.engine = CSC465-MLEngine()

    def test_initialization(self):
        self.assertEqual(self.engine.course_code, "CSC465-ML")
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
