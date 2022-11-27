"""City Module
This Module holds attributes of a Module.
Inherits from BaseModel base class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City Class

    Attributes:
        state_id (str): The UUID of the State the City belongs to
        name (str): City name
    """
    state_id = ''
    name = ''
