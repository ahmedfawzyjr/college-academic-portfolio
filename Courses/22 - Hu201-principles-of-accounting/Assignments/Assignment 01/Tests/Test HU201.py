import unittest

class TestHU201(unittest.TestCase):
    def test_course_integrity(self):
        code = "HU201"
        name = "Principles of Accounting"
        self.assertEqual(code, "HU201")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
