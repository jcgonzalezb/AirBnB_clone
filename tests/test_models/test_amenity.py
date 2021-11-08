#!/bin/usr/python3
""" Unittest for amenity.py """

import unittest
from models import amenity
from models import TestAmenity
Amenity = amenity.Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity"""

    def test_class(self):
        """Test class"""
        self.assertEqual(Amenity.name, "")
        self.assertTrue(issubclass(Amenity, BaseModel))
