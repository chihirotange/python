import unittest

class TestFirst(unittest.TestCase):
    def setUp(self):
        print("Hello world")

    def test_hello(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()