#!/usr/bin/python3
"""
Unittest for file_storage.py
"""
import unittest
import json
import os
import models
from models.user import User
from models.engine.file_storage import FileStorage



class TestFileStorage(unittest.TestCase):
    """This class contains several methods to test the
    file_storage.py file.
    """

    def setUp(self):
        """Setup for FileStorage tests."""
        self.engine = FileStorage()
        FileStorage._FileStorage__objects.clear()

    def test_executable_file(self):
        is_read_true = os.access("models/engine/file_storage.py", os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access("models/engine/file_storage.py", os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access("models/engine/file_storage.py", os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        my_model = FileStorage()
        self.assertIsInstance(my_model, FileStorage)

    def test_new(self):
        """
        Tests method: new (saves new object into dictionary)
        """
        m_storage = FileStorage()
        instances_dic = m_storage.all()
        betty = User()
        betty.id = 999999
        betty.name = "Betty"
        m_storage.new(betty)
        key = betty.__class__.__name__ + "." + str(betty.id)
        self.assertIsNotNone(instances_dic[key])

    def test_reload(self):

        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)
