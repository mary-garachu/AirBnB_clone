#!/usr/bin/python3
"""This is a module to perform tests on FileStorage class"""
import unittest
from unittest.mock import patch, mock_open
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """This class tests methods in FileStorage"""

    def setUp(self):
        """This is a setup for tests in the class
        It creates an instance of FileStorage
        """
        self.storage = FileStorage()

    def test_initial_state(self):
        """Tests the initial state of the class"""
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_new_method(self):
        """Tests the new method from FileStorage class"""
        model = BaseModel()
        self.storage.new(model)
        stored_objects = self.storage.all()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, stored_objects)
        self.assertEqual(stored_objects[key], model)

    def test_all_method(self):
        """Tests the all-method from FileStorage class"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.storage.new(model1)
        self.storage.new(model2)
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        key1 = "{}.{}".format(model1.__class__.__name__, model1.id)
        key2 = "{}.{}".format(model2.__class__.__name__, model2.id)
        self.assertIn(key1, all_objects)
        self.assertIn(key2, all_objects)

    def test_save_method(self):
        """This tests the save() method in FileStorage class"""
        model1 = BaseModel()
        model2 = BaseModel()
        model1.name = "Test1"
        model2.name = "Test2"
        self.storage.new(model1)
        self.storage.new(model2)

        with patch('builtins.open', mock_open()) as mock_file:
            self.storage.save()
            mock_file.assert_called_once_with(
                    FileStorage._FileStorage__file_path, 'w')

    def test_reload_method(self):
        """This method tests the reload() method in FileStorage class"""
        mock_data = {
                'BaseModel.1234': {
                    'id': '1234',
                    'name': 'MockModel'
                    }
                }

        with patch('json.load', return_value=mock_data):
            self.storage.reload()

        self.assertIn('BaseModel.1234', self.storage.all())

    def test_reload_nonexistent_file(self):
        """Testing a non-existent file in FileStorage class"""
        with patch('os.path.exists', return_value=False):
            self.storage.reload()
        self.assertIsInstance(self.storage.all(), dict)

    def test_reload_invalid_json(self):
        """Testing a reload with an invalid FileStorage class"""
        pass
