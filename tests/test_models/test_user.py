#!/bin/usr/python3
"""Test User"""

import unittest
from models.base_model import BaseModel
from models.user import User
from pep8 import StyleGuide


class TestUser(unittest.TestCase):
    """Test User"""

    def test_class(self):
        """Test class"""
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
        self.assertTrue(issubclass(User, BaseModel))
