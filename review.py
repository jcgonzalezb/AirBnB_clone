#!/usr/bin/python3
"""
Class Review that inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class to create review. This class inherits from BaseModel.
        Public class attributes:
            place_id: string
            user_id: string
            text: string
    """

    place_id = ''
    user_id = ''
    text = ''
