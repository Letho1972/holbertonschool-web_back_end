import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Dict, Tuple, Union
import requests

# Assuming utils.get_json is implemented as follows


def access_nested_map(nested_map, path):
    current = nested_map
    for key in path:
        current = current[key]
    return current


class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function."""
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
    # Tests the `get_json` function.
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
    ) -> None:
        #Tests `get_json`'s output.
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


if __name__ == '__main__':
    unittest.main()
