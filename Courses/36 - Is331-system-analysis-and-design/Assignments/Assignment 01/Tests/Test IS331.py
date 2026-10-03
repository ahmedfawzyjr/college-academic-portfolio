import unittest

class TestIS331(unittest.TestCase):
    def test_course_integrity(self):
        code = "IS331"
        name = "System Analysis & Design"
        self.assertEqual(code, "IS331")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
