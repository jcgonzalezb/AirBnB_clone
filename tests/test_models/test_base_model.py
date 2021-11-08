#!/usr/bin/python3
"""Unittest for base_model.py
"""
import unittest
import json
import os
from models import TestBaseModel
from models import base_model
BaseModel = base_model.BaseModel

class TestBaseModel(unittest.TestCase):
    """This class contains several methods to test the
    base_model.py file.
    """
