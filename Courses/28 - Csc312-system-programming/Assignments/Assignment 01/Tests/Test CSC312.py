import unittest

class TestCSC312(unittest.TestCase):
    def test_course_integrity(self):
        code = "CSC312"
        name = "System Programming"
        self.assertEqual(code, "CSC312")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
