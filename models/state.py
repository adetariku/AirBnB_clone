#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module State 
This Module holds attributes of the class States
It is extended from the base class BaseModel
"""


from models.base_model import BaseModel


class State(BaseModel):
    """State Class
    
    Attributes:
        name (str): The name of a State
    """
    
    name = ""
