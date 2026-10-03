import unittest

class TestEE242(unittest.TestCase):
    def test_course_integrity(self):
        code = "EE242"
        name = "Logic Design (Self Study)"
        self.assertEqual(code, "EE242")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
