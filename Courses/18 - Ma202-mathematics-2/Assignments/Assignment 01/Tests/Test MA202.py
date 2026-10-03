import unittest

class TestMA202(unittest.TestCase):
    def test_course_integrity(self):
        code = "MA202"
        name = "Mathematics II (Linear Algebra)"
        self.assertEqual(code, "MA202")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
