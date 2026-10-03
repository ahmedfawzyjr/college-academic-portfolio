import unittest

class TestCS341(unittest.TestCase):
    def test_course_integrity(self):
        code = "CS341"
        name = "Computer Graphics"
        self.assertEqual(code, "CS341")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
