import unittest

class TestCS212(unittest.TestCase):
    def test_course_integrity(self):
        code = "CS212"
        name = "Programming Language II (OOP)"
        self.assertEqual(code, "CS212")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
