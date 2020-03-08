import unittest
import responses
from SDTLpy.src.SDTLClient import SDTLClient
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.client_url = ""
        self.client = SDTLClient(self.client_url)

    def test_ctor(self):
        self.assertEqual(len(self.client.input_files), 0)
        self.assertEqual(len(self.client.input_directories), 0)
        self.assertEqual(len(self.client.results), 0)

    def test_add_result(self):
        self.assertEqual(True, False)

    def test_add_file(self):
        self.assertEqual(True, False)

    def test_add_dictory(self):
        self.assertEqual(True, False)

    @responses.activate
    def test_transform_files(self):
        responses.add(responses.GET, self.client.endpoint_url,
                      json={})

        assert responses.calls[0].response.text == {}

    def test_transform_directories(self):
        responses.add(responses.GET, self.client.endpoint_url,
                      json={})

        assert responses.calls[0].response.text == {}

    def test_save(self):
        self.assertEqual(True, False)

    def test_reset(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
