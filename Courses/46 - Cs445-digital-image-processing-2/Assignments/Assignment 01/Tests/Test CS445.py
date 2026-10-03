import unittest

class TestCS445(unittest.TestCase):
    def test_course_integrity(self):
        code = "CS445"
        name = "Digital Image Processing II"
        self.assertEqual(code, "CS445")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
