#!/usr/bin/env python3
""" tests for the basemodel """


import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import json
"""from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""
from uuid import uuid4


class TestBaseModel(unittest.TestCase):
    """ define unittests for base model """

    def startup(self):
        """ startup for the proceeding tests """
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89

    def testting_id_type(self):
        """ testting for id type """
        self.assertEqual(type(self.model.id), str)

    def testting_created_at_type(self):
        """ testting for created at type """
        self.assertEqual(type(self.model.created_at), datetime)

    def testting_updated_at_type(self):
        """ testting for updated at type """
        self.assertEqual(type(self.model.updated_at), datetime)

    def testting_name_type(self):
        """ test for name type """
        self.assertEqual(type(self.model.name), str)

    def testting_my_number_type(self):
        """ test for my number type """
        self.assertEqual(type(self.model.my_number), int)

    def testting_save_updates_updated_at(self):
        """ test for save updated at """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def testting_to_dict_returns_dict(self):
        """ testting for to dict return type """
        self.assertEqual(type(self.model.to_dict()), dict)

    def testting_to_dict_contains_correct_keys(self):
        """ testting for dict containing correct keys """
        model_dict = self.model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('name', model_dict)
        self.assertIn('my_number', model_dict)
        self.assertIn('__class__', model_dict)

    def testting_to_dict_created_at_format(self):
        """ testting for created at format """
        model_dict = self.model.to_dict()
        created_at = model_dict['created_at']
        self.assertEqual(created_at, self.model.created_at.isoformat())

    def testting_to_dict_updated_at_format(self):
        """ testting for updated at format """
        model_dict = self.model.to_dict()
        updated_at = model_dict['updated_at']
        self.assertEqual(updated_at, self.model.updated_at.isoformat())


class TestBaseModel_2(unittest.TestCase):
    """ define unittests for base model two """

    def startup(self):
        """ startup for proceeding tests two """
        self.my_model = BaseModel()

    def testting_id_generation(self):
        """ testting for id gen type """
        self.assertIsInstance(self.my_model.id, str)

    def testting_str_representation(self):
        """ testting for str rep """
        expected = "[BaseModel] ({}) {}".format(
            self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected)

    def testting_to_dict_method(self):
        """ testting for to dict method """
        my_model_dict = self.my_model.to_dict()
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')

    def testting_from_dict_method(self):
        """ testting for from dict method """
        my_model_dict = self.my_model.to_dict()
        my_new_model = BaseModel(**my_model_dict)
        self.assertIsInstance(my_new_model, BaseModel)
        self.assertEqual(my_new_model.id, self.my_model.id)
        self.assertEqual(my_new_model.created_at, self.my_model.created_at)
        self.assertEqual(my_new_model.updated_at, self.my_model.updated_at)

    def testting_created_at_and_updated_at_types(self):
        """ testting for created at and updated at types """
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)


class TestBaseMode_3(unittest.TestCase):
    """ define unittests for base model three """

    def testting_state(self):
        """ testting for state """
        state = State()
        state.name = "Kenya"
        self.assertEqual(state.name, "Kenya")

    def testting_city(self):
        """ testting for city """
        state_id = uuid4()
        city = City()
        city.name = "Nairobi"
        city.state_id = state_id
        self.assertEqual(city.name, "Nairobi")
        self.assertEqual(city.state_id, state_id)

    def testting_amenity(self):
        """ testing amenity """
        amenity = Amenity()
        amenity.name = "Free Wifi"
        self.assertEqual(amenity.name, "Free Wifi")

    def testing_review(self):
        """testing reviwe  """
        place_id = uuid4()
        user_id = uuid4()
        review = Review()
        review.place_id = place_id
        review.user_id = user_id
        review.text = "Good"
        self.assertEqual(review.place_id, place_id)
        self.assertEqual(review.user_id, user_id)
        self.assertEqual(review.text, "Good")


if __name__ == "__main__":
    unittest.main()
