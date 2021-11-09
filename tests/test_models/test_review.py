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
