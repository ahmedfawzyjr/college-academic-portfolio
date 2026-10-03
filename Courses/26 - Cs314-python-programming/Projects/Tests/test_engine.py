"""
Unit Tests for Automated Data Processing & Web Scraping Pipeline (CS314)
"""

import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from engine import CS314Engine

class TestCS314Engine(unittest.TestCase):
    def setUp(self):
        self.engine = CS314Engine()

    def test_initialization(self):
        self.assertEqual(self.engine.course_code, "CS314")
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
