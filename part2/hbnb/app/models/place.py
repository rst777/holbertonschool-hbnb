#!/user/bin/python3

from .basemodel import Basemodel
from .user import User

class Place(BaseModel):
    def _init_(self, title, description, price, latitude, longitude, owner)
