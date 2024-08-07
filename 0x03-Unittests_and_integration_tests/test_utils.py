#!/usr/bin/env python3
" doc doc"
import unittest
from parameterized import parameterized  # type:ignore
from utils import access_nested_map, get_json, memoize
from typing import Any, Tuple, Dict
from unittest.mock import patch, Mock


class TestAccessNestedMap (unittest.TestCase):

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict[str, Any], path: Tuple[str], expected: Any
    ) -> None:
        """doc doc doc"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
