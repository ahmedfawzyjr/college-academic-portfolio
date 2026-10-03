import unittest

class TestHU401(unittest.TestCase):
    def test_course_integrity(self):
        code = "HU401"
        name = "Creative Thinking & Innovation"
        self.assertEqual(code, "HU401")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
