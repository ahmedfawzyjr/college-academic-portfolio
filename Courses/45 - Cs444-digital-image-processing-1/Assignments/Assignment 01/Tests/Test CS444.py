import unittest

class TestCS444(unittest.TestCase):
    def test_course_integrity(self):
        code = "CS444"
        name = "Digital Image Processing I"
        self.assertEqual(code, "CS444")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
