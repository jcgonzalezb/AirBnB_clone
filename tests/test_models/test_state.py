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

        self.assertEqual(State.name, "")
        self.assertTrue(issubclass(State, BaseModel))

    def test_instance_BaseModel(self):
        amenity = State()
        self.assertTrue(isinstance(amenity, BaseModel))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_instaciacion(self):
        am = State()
        am.name = "Betty"
        self.assertIn("name", am.to_dict())

    def test_to_dict(self):
        base = State()
        ret_dict = base.to_dict()
        self.assertTrue(isinstance(ret_dict, dict))

    def test_two_states_unique_ids(self):
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)

if _name_ == "_main_":
    unittest.main()
