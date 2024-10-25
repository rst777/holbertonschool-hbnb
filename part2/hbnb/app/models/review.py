#!/usr/bin/python3

from app.models import BaseModel
from app.models import Place
from app.models import User

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
