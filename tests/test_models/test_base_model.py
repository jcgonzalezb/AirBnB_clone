#!/usr/bin/python3
"""
Unittest for base_model.py
"""
import unittest
import json
from os import chdir, getcwd, path
from datetime import datetime
from time import sleep
from models import base_model
from models.engine.file_storage import FileStorage
BaseModel = base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """This class contains several methods to test the
    base_model.py file.
    """

    @classmethod
    def setUpClass(cls):
        cls.base1 = BaseModel()
        cls.base1.name = "Betty"
        cls.base1.my_number = 89

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

    def test_str(self):
        """
        Test __str__ method
        """
        my_model = BaseModel()
        string = '[{}] ({}) {}'.format(
            my_model.__class__.__name__,
            my_model.id,
            my_model.__dict__,
        )
        self.assertEqual(string, str(my_model))

    def test_save(self):
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)

    def test_to_dict(self):
        """
        Test to_dict method
        """
        my_model = BaseModel()
        self.assertEqual(my_model.to_dict()['__class__'],
                         my_model.__class__.__name__)
        self.assertEqual(my_model.to_dict()["updated_at"],
                         my_model.updated_at.isoformat())
        self.assertEqual(my_model.to_dict()["created_at"],
                         my_model.created_at.isoformat())

    def test_init_basemodel_from_dictionary(self):
        """
        Checks when it is passed a dictionary to the init method.
        """
        model = BaseModel()
        model.name = "Holberton"
        model.my_number = 89
        model_json = model.to_dict()
        my_new_model = BaseModel(**model_json)
        # Checks that the object has the same attributes that the model
        dict_attr = {'name': 'Holberton', 'my_number': 89, 'id': model.id,
                     'created_at': model.created_at,
                     'updated_at': model.updated_at}
        for key, value in dict_attr.items():
            self.assertTrue(hasattr(my_new_model, key))
            self.assertEqual(getattr(my_new_model, key), value)
        # Checks if __class__ attribute was not added
        self.assertTrue(hasattr(my_new_model, key))
        cls_name = getattr(my_new_model, key)
        self.assertNotEqual(cls_name, model_json["__class__"])

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)
