import unittest

class TestCS313(unittest.TestCase):
    def test_course_integrity(self):
        code = "CS313"
        name = "Web Programming"
        self.assertEqual(code, "CS313")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
