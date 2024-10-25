#!/usr/bin/python3

from app.models import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name  # Nom de l'équipement (ex : Wi-Fi)
