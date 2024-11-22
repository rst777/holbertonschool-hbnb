from sqlalchemy.orm import Session
from models.place import Place

class PlaceRepository:
    """Repository pour gérer les entités Place."""

    def __init__(self, session: Session):
        self.session = session

    def create_place(self, place_data):
        """Crée un lieu et le sauvegarde dans la base."""
        place = Place(**place_data)
        self.session.add(place)
        self.session.commit()
        return place

    def get_place_by_id(self, place_id):
        """Récupère un lieu par ID."""
        return self.session.query(Place).get(place_id)

    def update_place(self, place):
        """Met à jour un lieu existant."""
        self.session.merge(place)
        self.session.commit()
        return place

    def delete_place(self, place):
        """Supprime un lieu."""
        self.session.delete(place)
        self.session.commit()
