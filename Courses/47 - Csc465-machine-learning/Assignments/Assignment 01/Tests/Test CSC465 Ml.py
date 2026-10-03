import unittest

class TestCSC465ML(unittest.TestCase):
    def test_course_integrity(self):
        code = "CSC465-ML"
        name = "Machine Learning"
        self.assertEqual(code, "CSC465-ML")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
