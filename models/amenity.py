#!/usr/bin/python3
"""
Class Amenity that inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class to create amenities. This class inherits from BaseModel.
        Public class attribute:
            name: string
    """

    name = ''
