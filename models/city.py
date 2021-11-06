#!/usr/bin/python3
"""
Class City that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Class to create cities. This class inherits from BaseModel.
        Public class attributes:
            state.id: string
            name: string
    """

    name = ''
    state_id = ''
