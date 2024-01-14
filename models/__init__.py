#!/usr/bin/python3
"""
Initializes the module variables
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
