#!/usr/bin/python3
"""Test City"""

import unittest
from models import TestCity
from models import city
City = city.City


class TestCity(unittest.TestCase):
    """Test City"""

    def test_class(self):
        """Test class"""
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")
        self.assertTrue(issubclass(City, BaseModel))
