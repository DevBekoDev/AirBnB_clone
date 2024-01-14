#!/usr/bin/python3
"""
Initializes the module variables
"""

import sys

sys.path.append('/root/AirBnB_clone/')
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
