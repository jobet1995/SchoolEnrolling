import unittest
from unittest.mock import MagicMock
import main

class TestResponse(unittest.TestCase):

  def setUp(self):
    self.request_mock = MagicMock()
    self.request_mock.path = '/'
    self.request_mock.headers = {}

  def test_do_GET(self):
    response_mock = MagicMock()
    response_mock.write = MagicMock()

    handler = main.MyHandler(self.request_mock, ('', 0), None)
    handler.send_json_response = MagicMock(return_value=None)
    handler.wfile = response_mock

    handler.do_GET()

    response_mock.write.assert_called_with(b"Response GET Request")

if __name__ == '__main__':
  unittest.main()