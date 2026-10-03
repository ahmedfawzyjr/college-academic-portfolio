import unittest

class TestCS499(unittest.TestCase):
    def test_course_integrity(self):
        code = "CS499"
        name = "Graduation Project"
        self.assertEqual(code, "CS499")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
