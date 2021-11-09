#!/usr/bin/python3
"""
Unittest for base_model.py
"""
import unittest
import json
import os
from datetime import datetime
from models import storage
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
        """ Tests the save method """
        object = BaseModel()
        t1 = object.updated_at
        object.name = "Betty"
        object.age = 89
        object.save()
        t2 = object.updated_at
        obj_ref = storage.all().get("BaseModel.{}".format(object.id))
        self.assertNotEqual(t1, t2)
        self.assertEqual(object.id, obj_ref.id)
        self.assertEqual(object.name, obj_ref.name)
        self.assertEqual(object.age, obj_ref.age)
        self.assertTrue(os.path.exists('file.json'))

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

    def test_updated_at(self):
        """Check if the instance has created_at Atttibute"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertTrue(bm1, "updated_at")
        self.assertTrue(bm2, "updated_at")

    def test_base_init(self):
        """
        Testing a class BaseModel
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(issubclass(type(instance), BaseModel))
        self.assertIs(type(instance), BaseModel)

        instance.name = "Holberton"
        instance.my_number = 89
        self.assertEqual(instance.name, "Holberton")
        self.assertEqual(instance.my_number, 89)

    def test_to_dict(self):
        """Test the to_dict method from BaseModel"""
        bm1 = BaseModel()
        bm1_dict = bm1.to_dict()
        self.assertIsInstance(bm1_dict, dict)
        self.assertEqual(bm1_dict["__class__"], "BaseModel")
        self.assertEqual(str(bm1.id), bm1_dict["id"])
        self.assertIsInstance(bm1_dict["created_at"], str)
        self.assertIsInstance(bm1_dict["updated_at"], str)

    def test_save(self):
        """Test to check each update in the storage"""
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, "updated_at"))
        bm1.save()
        self.assertTrue(hasattr(bm1, "updated_at"))
        t_arg = {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                 'create_at': datetime(2017, 9, 28, 21, 5, 54, 119427),
                 'updated_at': datetime(2017, 9, 28, 21, 5, 54, 119572),
                 'name': 'bm1'}
        bm2 = BaseModel(t_arg)
        bm2.save()
        last_time = bm2.updated_at
        bm2.save()
        self.assertNotEqual(last_time, bm2.updated_at)

    def test_init_from_dict(self):
        """test to check a new instance witk Kwargs"""
        my_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                   'created_at': '2017-09-28T21:03:54.052298',
                   '__class__': 'BaseModel', 'my_number': 89,
                   'updated_at': '2017-09-28T21:03:54.052302',
                   'name': 'Holberton'}
        bm1 = BaseModel(**my_dict)
        self.assertIsInstance(bm1, BaseModel)
        self.assertIsInstance(bm1.id, str)
        self.assertEqual(bm1.id, '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.updated_at, datetime)
        self.assertIsInstance(bm1.name, str)
        self.assertEqual(bm1.name, 'Holberton')
        self.assertEqual(
            bm1.created_at.isoformat(), '2017-09-28T21:03:54.052298')
        self.assertEqual(
            bm1.updated_at.isoformat(), '2017-09-28T21:03:54.052302')
