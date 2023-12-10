#!/usr/bin/python3
"""
Inherits from BaseModel class
"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """
    Public class attributes:
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initilizes cclass city from BaseModel"""
        super().__init__(*args, **kwargs)
        if 'State' in kwargs and isinstance(kwargs['State'], State):
            self.state_id = kwargs['State'].id
