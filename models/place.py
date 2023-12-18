#!/usr/bin/python3
"""
Inherits from the BaseModel class
"""
from models.base_model import BaseModel
from models.user import User
from models.city import City


class Place(BaseModel):
    """
    Public class attributes:
    city_id: string - empty string: it will be the City.id
    user_id: string - empty string: it will be the User.id
    name: string - empty string
    description: string - empty string
    number_rooms: integer - 0
    number_bathrooms: integer - 0
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    amenity_ids: list of string - empty list:
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Calls the init method from the BaseModel"""
        super().__init__(*args, **kwargs)
        if 'City' in kwargs and isinstance(kwargs['City'], City):
            self.city_id = kwargs['City'].id
        if 'User' in kwargs and isinstance(kwargs['User'], User):
            self.user_id = kwargs['User'].id

        if 'amenities' in kwargs and isinstance(kwargs['amenities'], list):
            self.amenity_ids = kwargs['amenities']
