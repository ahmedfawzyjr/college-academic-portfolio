"""
Unit Tests for Computer Vision Image Enhancement & Edge Detection Suite (CS444)
"""

import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from engine import CS444Engine

class TestCS444Engine(unittest.TestCase):
    def setUp(self):
        self.engine = CS444Engine()

    def test_initialization(self):
        self.assertEqual(self.engine.course_code, "CS444")
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
