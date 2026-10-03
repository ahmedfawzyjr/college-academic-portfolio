import unittest

class TestCS222(unittest.TestCase):
    def test_course_integrity(self):
        code = "CS222"
        name = "Computer Architecture & Organization"
        self.assertEqual(code, "CS222")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
