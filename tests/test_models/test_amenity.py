#!/bin/usr/python3
""" Unittest for amenity.py """


import unittest
from datetime import datetime
import models
from models import amenity
from models import base_model
BaseModel = base_model.BaseModel
Amenity = amenity.Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity"""

    def test_class(self):
        """Test class"""
        self.assertEqual(Amenity.name, "")
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        instance = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", instance.__dict__)

    def test_two_amenities_unique_ids(self):
        instance1 = Amenity()
        instance2 = Amenity()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)
