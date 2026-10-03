import unittest

class TestHU104(unittest.TestCase):
    def test_course_integrity(self):
        code = "HU104"
        name = "Principles of Management"
        self.assertEqual(code, "HU104")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
