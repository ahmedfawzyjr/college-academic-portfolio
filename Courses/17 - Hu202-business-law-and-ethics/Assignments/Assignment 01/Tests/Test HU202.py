import unittest

class TestHU202(unittest.TestCase):
    def test_course_integrity(self):
        code = "HU202"
        name = "Business Law & Human Rights"
        self.assertEqual(code, "HU202")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
