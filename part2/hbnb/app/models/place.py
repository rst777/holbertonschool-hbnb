#!/user/bin/python3

from .app.models. import Basemodel
from .app.models.user import User
from .app.models.review import Review

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
