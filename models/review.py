#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Review Module - inherits from BaseModel class.
It holds attributes assigned to the reviews created by the users.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class

    Attributes:
        place_id (str): UUID of the Place the Review belongs to
        user_id (str): UUID of the User that made the review
        text (str): message the User wrote about the Place
    """

    place_id = ""
    user_id = ""
    text = "" 
