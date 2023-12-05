#!/usr/bin/python3
"""This is a unittest module to test the  base class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This class tests the methods in the BaseModel"""

    def setUp(self):
        """Initializes an instance of BaseModel"""
        self.base_model = BaseModel()

    def test_init(self):
        """Test the __init__ method in BaseModel"""
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        """Tests the return of __str__ method"""
        expected_str = "[BaseModel] ({}) {}".format(
                self.base_model.id,
                self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save(self):
        """Tests the save method of BaseModel"""
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, prev_updated_at)

    def test_to_dict(self):
        """Tests the to_dict method of BaseModel"""
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(datetime.fromisoformat(
            obj_dict['created_at']),
            datetime)
        self.assertIsInstance(datetime.fromisoformat(
            obj_dict['updated_at']),
            datetime)
