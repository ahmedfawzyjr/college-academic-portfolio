import unittest

class TestCS221(unittest.TestCase):
    def test_course_integrity(self):
        code = "CS221"
        name = "Digital Logic Design"
        self.assertEqual(code, "CS221")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
