import unittest

class TestCS214(unittest.TestCase):
    def test_course_integrity(self):
        code = "CS214"
        name = "Visual Programming (C#)"
        self.assertEqual(code, "CS214")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
