#!/bin/usr/python3
"""Unittest for state.py"""

import unittest
from models import base_model
from models import state
State = state.State
BaseModel = base_model.BaseModel


class TestState(unittest.TestCase):
    """Test Amenity"""

    def test_class(self):
        """Test class"""
        self.assertEqual(State.name, "")
        self.assertTrue(issubclass(State, BaseModel))
