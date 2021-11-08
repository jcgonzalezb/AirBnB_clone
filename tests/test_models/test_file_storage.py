#!/usr/bin/python3
"""
Unittest for file_storage.py
"""
import unittest
import json
import os
from models.engine import TestFileStorage
from models.engine import file_storage
FileStorage = file_storage.FileStorage


class TestFileStorage(unittest.TestCase):
    """This class contains several methods to test the
    file_storage.py file.
    """
