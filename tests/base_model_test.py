#!/usr/bin/python3
"""
Test suits base model
"""

import os
import re
import json
import uuid
import unittest
from time import sleep
from datetime import datetime
import sys

sys.path.append('/root/AirBnB_clone/')
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Base model testing
    """

    def setUp(self):
        """
        startup
        """
        pass

    def testting_basic(self):
        """
    bsic tests
        """
        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.number = 89
        self.assertEqual([my_model.name, my_model.number],
                         ["ALX", 89])

    def testting_datetime(self):
        """
        check datetime format
        """
        pass
    
    def testting_datetime(self):
        """
        check datetime format
        """
        pass


if __name__ == '__main__':
    unittest.main()
