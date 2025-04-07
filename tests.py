import requests.exceptions
from requests.exceptions import Timeout

import unittest
from unittest.mock import patch, MagicMock

from main import get_joke, len_joke


class TestJoke(unittest.TestCase):

    @patch('main.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'test joke'
        self.assertEqual(len_joke(), 9)

    @patch('main.requests')
    def test_get_joke(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'value': 'Test joke xaxa'
        }
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'Test joke xaxa')

    @patch('main.requests')
    def test_fail_get_joke_raises_exception(self, mock_requests):
        mock_requests.exceptions = requests.exceptions  # to avoid - TypeError: catching classes that do not inherit from BaseException is not allowed
        mock_requests.get.side_effect = Timeout('Seems the server is down :(')
        self.assertEqual(get_joke(), 'No joke')

    @patch('main.requests')
    def test_fail_get_joke_raise_for_status(self, mock_requests):
        mock_requests.exceptions = requests.exceptions  # to avoid - TypeError: catching classes that do not inherit from BaseException is not allowed

        mock_response = MagicMock(status_code=403)
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()

        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'HTTPError raised')


if __name__ == '__main__':
    unittest.main()
