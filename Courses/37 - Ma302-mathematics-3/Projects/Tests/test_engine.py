"""
Unit Tests for Differential Equation Numerical Solver (Runge-Kutta & Euler) (MA302)
"""

import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from engine import MA302Engine

class TestMA302Engine(unittest.TestCase):
    def setUp(self):
        self.engine = MA302Engine()

    def test_initialization(self):
        self.assertEqual(self.engine.course_code, "MA302")
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
