import unittest
from SDTLpy.src import SDTLResult

class MyTestCase(unittest.TestCase):
    def test_ctor(self):
        filename = "testFile.Rmd"
        sdtl = {}
        res = SDTLResult(sdtl, filename)
        self.assertEqual(res.sdtl, sdtl)
        self.assertEqual(res.filename, filename)


if __name__ == '__main__':
    unittest.main()
