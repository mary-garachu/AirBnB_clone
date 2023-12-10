#!/usr/bin/python3
"""
This class inherits from the BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Public class attributes:
    name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """class the Baseclass init method"""
        super().__init__(*args, **kwargs)
