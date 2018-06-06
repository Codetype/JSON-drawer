import unittest

class MyTestCase(unittest.TestCase):
    def test_circle(self):
        self.assertEqual("test", "test")

if __name__ == '__main__':
    unittest.main()