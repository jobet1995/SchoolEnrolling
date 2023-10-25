import unittest
from soap import SoapService

class TestSoapService(unittest.TestCase):
    def setUp(self):
        self.service = SoapService()

    def test_get(self):
        self.assertEqual(self.service.get("data"), "GET Response")

    def test_put(self):
        self.assertEqual(self.service.put("data"), "PUT Response")

    def test_delete(self):
        self.assertEqual(self.service.delete("data"), "DELETE Response")

    def test_post(self):
        self.assertEqual(self.service.post("data"), "POST Response")

if __name__ == "__main__":
    unittest.main()