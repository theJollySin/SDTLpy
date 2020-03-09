import unittest
from SDTLpy.src.SDTLClient import SDTLClient

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.client_url = "test_url"
        self.client = SDTLClient(self.client_url)

    def test_ctor(self):
        self.assertEqual(len(self.client.input_files), 0)
        self.assertEqual(len(self.client.input_directories), 0)
        self.assertEqual(len(self.client.results), 0)

    def test_add_result(self):
        filename = 'test'
        sdtl = {}
        self.client.add_result(sdtl, filename)
        self.assertEqual(len(self.client.results), 1)
        res = self.client.results[0]
        self.assertEqual(res.filename, filename)
        self.assertEqual(res.sdtl, sdtl)


if __name__ == '__main__':
    unittest.main()
