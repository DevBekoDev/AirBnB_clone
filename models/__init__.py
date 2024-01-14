#!/usr/bin/python3
"""
Initializes the module variables
"""

import sys
from models.engine.file_storage import FileStorage
sys.path.append('/root/AirBnB_clone/')


storage = FileStorage()
storage.reload()
