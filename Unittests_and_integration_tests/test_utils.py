import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
import requests

# Assuming utils.get_json is implemented as follows


def get_json(url):
    # fetch JSON data from a URL
    response = requests.get(url)
    return response.json()


class TestGetJson(unittest.TestCase):
    # class inherits from unittest.TestCase
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        # method that returns test_payload
        with patch('requests.get') as mocked_get:
            # Create a mock response object with a json method
            mocked_response = Mock()
            mocked_response.json.return_value = test_payload
            mocked_get.return_value = mocked_response

            # Call the function being tested
            result = get_json(test_url)

            # Assert requests.get was called exactly once with test_url
            mocked_get.assert_called_once_with(test_url)
            # Assert the result is equal to test_payload
            self.assertEqual(result, test_payload)

if __name__ == '__main__':
    unittest.main()
