import unittest

class TestHU301(unittest.TestCase):
    def test_course_integrity(self):
        code = "HU301"
        name = "Technical Report Writing"
        self.assertEqual(code, "HU301")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
