import unittest

class TestIS101(unittest.TestCase):
    def test_course_integrity(self):
        code = "IS101"
        name = "Information Systems Fundamentals"
        self.assertEqual(code, "IS101")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
