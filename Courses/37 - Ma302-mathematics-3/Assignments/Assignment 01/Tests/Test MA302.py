import unittest

class TestMA302(unittest.TestCase):
    def test_course_integrity(self):
        code = "MA302"
        name = "Mathematics III (Differential Equations)"
        self.assertEqual(code, "MA302")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
