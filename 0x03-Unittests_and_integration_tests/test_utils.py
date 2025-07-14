#!/usr/bin/env python3

from utils import access_nested_map
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):

    # Previous success test stays here
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    # New exception test
    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected_key}'")

class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        # Patch 'requests.get' where it's used (in utils)
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            # Ensure requests.get was called once with the right URL
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            obj = TestClass()

            # Call the memoized property twice
            result1 = obj.a_property()
            result2 = obj.a_property()

            # Check that both calls returned the correct value
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Ensure a_method was called only once due to memoization
            mock_method.assert_called_once()
