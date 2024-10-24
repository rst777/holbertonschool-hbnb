#!/usr/bin/python3

from app.models.basemodel import BaseModel
from app.models.user import User
from app.models.review import Review

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # Liste pour les reviews
        self.amenities = []  # Liste pour les amenities

    def add_review(self, review):
        """Ajoute un avis à la place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Ajoute un équipement à la place."""
        self.amenities.append(amenity)
