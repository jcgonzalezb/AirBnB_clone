#!/usr/bin/python3
"""
Class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
        """
        Class to create users. This class
	inherits from BaseModel.
	Public class attributes:
		email: string
		password: string
		first_name: string
		last_name: string
        """

