#!/user/bin/python3

from .basemodel import Basemodel
from .user import User

class Place(Basemodel):
    def _init_(self, title, description, price, latitude, longitude, owner)
        super()._init_()
        self.title =title 
        self.description = description
        self.price = price 
        self.latitude = latitude 
        self.longitude = longitude 
        self.owner = owner
        self.review = []
        self.ameneties = []

        def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)
