#!/usr/bin/python3
"""Amenity module - a module for Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class
    
    Attributes:
        name(str): amenity name
    """
    name = ""
