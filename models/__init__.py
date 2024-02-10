#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage

"""Create a unique FileStorage instance for your application"""
storage = FileStorage()
storage.reload()