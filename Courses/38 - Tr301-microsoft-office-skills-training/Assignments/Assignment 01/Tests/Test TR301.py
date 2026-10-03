import unittest

class TestTR301(unittest.TestCase):
    def test_course_integrity(self):
        code = "TR301"
        name = "Microsoft Office Skills Training"
        self.assertEqual(code, "TR301")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
