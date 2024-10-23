from app.models.base_model import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner_id):
        super().__init__()

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.reviews = []  # Liste pour stocker les reviews
        self.amenities = []  # Liste pour stocker les amenities

    def to_dict(self):
        """Convertit l'objet Place en dictionnaire."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'amenities': self.amenities,
        }

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be a non-negative float.")
        self._price = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not (-90 <= value <= 90):
            raise ValueError("Latitude must be between -90 and 90.")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not (-180 <= value <= 180):
            raise ValueError("Longitude must be between -180 and 180.")
        self._longitude = value


    def add_review(self, review):
        """Ajoute une review au lieu."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Ajoute une amenity au lieu."""
        self.amenities.append(amenity)
