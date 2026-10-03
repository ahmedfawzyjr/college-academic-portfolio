import unittest

class TestMA301(unittest.TestCase):
    def test_course_integrity(self):
        code = "MA301"
        name = "Operations Research"
        self.assertEqual(code, "MA301")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
