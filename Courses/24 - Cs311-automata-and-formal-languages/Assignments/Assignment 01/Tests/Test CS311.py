import unittest

class TestCS311(unittest.TestCase):
    def test_course_integrity(self):
        code = "CS311"
        name = "Automata & Formal Languages"
        self.assertEqual(code, "CS311")
        self.assertTrue(len(name) > 0)

    def test_sample_computation(self):
        result = 10 + 20
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
