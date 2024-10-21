from app.models.base_model import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # Liste pour stocker les reviews
        self.amenities = []  # Liste pour stocker les amenities

    def add_review(self, review):
        """Ajoute une review au lieu."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Ajoute une amenity au lieu."""
        self.amenities.append(amenity)
