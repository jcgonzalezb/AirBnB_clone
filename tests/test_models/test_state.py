#!/bin/usr/python3
"""Unittest for state.py"""

import unittest
from models import TestState
from models import State
State = state.State


class TestState(unittest.TestCase):
    """Test Amenity"""

    def test_class(self):
        """Test class"""
        self.assertEqual(Amenity.name, "")
        self.assertTrue(issubclass(Amenity, BaseModel))
