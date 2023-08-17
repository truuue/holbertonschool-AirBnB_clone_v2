#!/usr/bin/python3
"""This module instantiates a storage object depending on the
current storage type"""
import os

if os.environ.get("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
