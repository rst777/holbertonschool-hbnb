from sqlalchemy.orm import Session
from models.amenity import Amenity

class AmenityRepository:
    """Repository pour gérer les entités Amenity."""

    def __init__(self, session: Session):
        self.session = session

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.session.add(amenity)
        self.session.commit()
        return amenity

    def get_amenity_by_id(self, amenity_id):
        return self.session.query(Amenity).get(amenity_id)

    def update_amenity(self, amenity):
        self.session.merge(amenity)
        self.session.commit()
        return amenity

    def delete_amenity(self, amenity):
        self.session.delete(amenity)
        self.session.commit()
