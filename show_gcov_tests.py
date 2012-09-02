import unittest
import show_gcov

class ShowGcovTests(unittest.TestCase):
    def test_fail(self):
        self.assertTrue(False, "checking the test framework")

if __name__ == "__main__":
    unittest.main()
