#!/usr/bin/python3
"""
Unittest for user.py
"""
import unittest
import json
import os
from models import base_model
import models
from models import user
from datetime import datetime
User = user.User
BaseModel = base_model.BaseModel


class TestUser(unittest.TestCase):
    """This class contains several methods to test the
    user.py file.
    """

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_to_dict(self):
        base = User()
        ret_dict = base.to_dict()
        self.assertTrue(isinstance(ret_dict, dict))

    def test__str__(self):
        base = User()
        base_str = base.__str__()
        self.assertTrue(isinstance(base_str, str))

    def test_class(self):
        """Test class"""
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
        self.assertTrue(issubclass(User, BaseModel))

    def test_instance(self):
        """Test instance"""
        my_user = User()
        self.assertEqual(my_user.email, "")
        self.assertEqual(my_user.password, "")
        self.assertEqual(my_user.first_name, "")
        self.assertEqual(my_user.last_name, "")
        self.assertTrue(isinstance(my_user, BaseModel))
