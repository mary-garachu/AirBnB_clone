#!/usr/bin/python3
"""
Review Class inherits from BaseModel
"""
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """
    Public class attributes:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes init method with Base class"""
        super().__init__(*args, **kwargs)
        if 'Place' in kwargs and isinstance(kwargs['Place'], Place):
            self.place_id = kwargs['Place'].id
        if 'User' in kwargs and isinstance(kwargs['User'], User):
            self.user_id = kwargs['User'].id
