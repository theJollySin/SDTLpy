import unittest


class MyTestCase(unittest.TestCase):
    def test_ctor(self):
        self.assertEqual(True, False)

    def test_save(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
