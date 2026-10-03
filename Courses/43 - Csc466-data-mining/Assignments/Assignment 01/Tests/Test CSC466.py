import unittest

class TestCSC466(unittest.TestCase):
    def test_course_integrity(self):
        code = "CSC466"
        name = "Data Mining & Analytics"
        self.assertEqual(code, "CSC466")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
