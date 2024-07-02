import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
import requests

# Assuming utils.get_json is implemented as follows


def access_nested_map(nested_map, path):
    current = nested_map
    for key in path:
        current = current[key]
    return current


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises((KeyError, TypeError)) as cm:
            access_nested_map(nested_map, path)
        if isinstance(cm.exception, KeyError):
            self.assertEqual(str(cm.exception), f"'{path[-1]}'")
        else:
            self.assertEqual(str(cm.exception),
                             "'int' object is not subscriptable")


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
