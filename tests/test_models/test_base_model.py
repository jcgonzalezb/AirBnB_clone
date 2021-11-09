#!/usr/bin/python3
"""
Unittest for base_model.py
"""
import unittest
import json
import os
from datetime import datetime
from models import base_model
BaseModel = base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """This class contains several methods to test the
    base_model.py file.
    """

    def test_class(self):
        """Test instance of the class"""
        base = BaseModel()
        self.assertTrue(isinstance(base, BaseModel))

    def test_id(self):
        """Test for unic id"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertTrue(base1.id != base2.id)

    def test_kwargs(self):
        """Test instance for kwargs"""
        base3 = BaseModel()
        base3.name = "Betty"
        dictionary = base3.to_dict()
        self.assertTrue("name" in dictionary)

    def test_dict(self):
        """Test that fuction returns a dictionary."""
        base4 = BaseModel()
        ret_dic = base4.to_dict()
        self.assertTrue(isinstance(ret_dic, dict))

    def test__str__(self):
        """Check the string of an created instance"""
        bm1 = BaseModel()
        printed = "[{}] ({}) {}".format(
            bm1.__class__.__name__, bm1.id, bm1.__dict__)
        self.assertEqual(str(bm1), printed)

    def test_save(self):
        """Test it saves an instance"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        hour = my_model.updated_at
        my_model.save()
        hour2 = my_model.updated_at
        self.assertNotEqual(hour, hour2)
        self.assertTrue(os.path.exists('file.json'))

    def test_save(self):
        """Test for correct update of attribute updated_at"""
        old_updated_at = self.base_1.updated_at
        time.sleep(0.5)
        self.base_1.save()
        base_1_key = type(self.base_1).__name__ + "." + self.base_1.id
        with open("file.json", "r") as f:
            json_text = f.read()

        self.assertTrue(base_1_key in json_text)
        self.assertNotEqual(self.base_1.created_at, self.base_1.updated_at)
        self.assertNotEqual(self.base_1.updated_at, old_updated_at)

    def test_str_magic_method(self):
        """Test for correct __str__ output"""
        correct_output = "[BaseModel] ({}) {}".format(
            self.base_1.id, self.base_1.__dict__)
