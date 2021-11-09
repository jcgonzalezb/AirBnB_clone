#!/bin/usr/pyhton3
"""Test Review"""

import unittest
from models import base_model
from models import review
Review = review.Review
BaseModel = base_model.BaseModel


class TestReview(unittest.TestCase):
    """Test review"""

    def test_class(self):
        """Test class"""
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instaciacion(self):
        am = Review()
        am.name = "Betty"
        self.assertIn("name", am.to_dict())

    def test_to_dict(self):
        base = Review()
        ret_dict = base.to_dict()
        self.assertTrue(isinstance(ret_dict, dict))

    def test_str(self):
        base = Review()
        base_str = base.__str__()
        self.assertTrue(isinstance(base_str, str))

    def test_instance_BaseModel(self):
        amenity = Review()
        self.assertTrue(isinstance(amenity, BaseModel))

if _name_ == "_main_":
    unittest.main()
