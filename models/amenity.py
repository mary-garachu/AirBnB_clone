#!/usr/bin/python3
"""
Amenity class inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Public class attributes:
    name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Calls the init method of the BaseModel"""
        super().__init__(*args, **kwargs)
