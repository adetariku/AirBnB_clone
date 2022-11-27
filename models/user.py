#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""User Module
This Module holds user information.
It is extended from the BaseModel class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User Class: inherited from BaseModel class
    
    Attributes:
        email (str): valid User email
        password (str): User password
        first_name (str): The first name of the User
        last_name (str): last name of the User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
