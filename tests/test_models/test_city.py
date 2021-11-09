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

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_two_cities_unique_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_str(self):
        base = City()
        base_str = base._str_()
        self.assertTrue(isinstance(base_str, str))


if _name_ == "_main_":
    unittest.main()
