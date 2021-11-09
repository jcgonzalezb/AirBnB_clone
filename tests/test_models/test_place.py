#!/bin/usr/python3
"""Unittest for place.py"""

import unittest
from models import base_model
from models import place
Place = place.Place
BaseModel = base_model.BaseModel


class TestPlace(unittest.TestCase):
    """Test Place"""

    def test_class(self):
        """Test class"""
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])
        self.assertTrue(issubclass(Place, BaseModel))

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(Place.__doc__)

    def test_instance_BaseModel(self):
        """ Tests inheritance """
        amenity = Place()
        self.assertTrue(isinstance(amenity, BaseModel))

    def test_instaciacion(self):
        """ Tests correct instatiation of the class """
        amme = Place()
        amme.name = "Betty"
        self.assertIn("name", amme.to_dict())

if _name_ == "_main_":
    unittest.main()
