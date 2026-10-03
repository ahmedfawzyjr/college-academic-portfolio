import unittest

class TestEL101(unittest.TestCase):
    def test_course_integrity(self):
        code = "EL101"
        name = "Computer Electronics"
        self.assertEqual(code, "EL101")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
