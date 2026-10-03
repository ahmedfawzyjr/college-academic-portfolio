import unittest

class TestMA101(unittest.TestCase):
    def test_course_integrity(self):
        code = "MA101"
        name = "Mathematics I (Calculus)"
        self.assertEqual(code, "MA101")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
