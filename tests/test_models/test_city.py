#!/usr/bin/python3
"""Test City"""

import unittest
from models import city
from models import base_model
City = city.City
BaseModel = base_model.BaseModel


class TestCity(unittest.TestCase):
    """Test City"""

    def test_class(self):
        """Test class"""
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")
        self.assertTrue(issubclass(City, BaseModel))
