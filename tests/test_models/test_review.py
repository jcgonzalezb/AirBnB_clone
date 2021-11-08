#!/bin/usr/pyhton3
"""Test Review"""

import unittest
from models import TestReview
from models import review
Review = review.Review


class TestReview(unittest.TestCase):
    """Test review"""

    def test_class(self):
        """Test class"""
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
        self.assertTrue(issubclass(Review, BaseModel))
