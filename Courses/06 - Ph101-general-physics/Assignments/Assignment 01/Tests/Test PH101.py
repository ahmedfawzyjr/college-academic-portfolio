import unittest

class TestPH101(unittest.TestCase):
    def test_course_integrity(self):
        code = "PH101"
        name = "General Physics"
        self.assertEqual(code, "PH101")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
