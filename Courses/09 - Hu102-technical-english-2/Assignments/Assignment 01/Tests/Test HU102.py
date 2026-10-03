import unittest

class TestHU102(unittest.TestCase):
    def test_course_integrity(self):
        code = "HU102"
        name = "Technical English II"
        self.assertEqual(code, "HU102")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
