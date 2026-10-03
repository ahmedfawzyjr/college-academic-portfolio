import unittest

class TestHU103(unittest.TestCase):
    def test_course_integrity(self):
        code = "HU103"
        name = "Principles of Economics"
        self.assertEqual(code, "HU103")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
