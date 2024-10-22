from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
import uuid


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        from app.api.v1.users import User
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def create_amenity(self, data):
        if 'name' not in data:
            raise ValueError("Le champ 'name' est requis")

        amenity_id = str(uuid.uuid4())  # Génère un nouvel ID
        amenity_data = {
            'id': amenity_id,
            'name': data.get('name')
        }

        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        # Convertir l'objet en dictionnaire
        return amenity.to_dict()

    def get_amenity(self, amenity_id):
        # Récupérer une commodité par son ID
        amenity = self.amenity_repo.get(amenity_id)
        if amenity:
            return amenity.to_dict()
        return None  # Si l'amenity n'existe pas

    def get_all_amenities(self):
        # Récupérer toutes les commodités
        amenities = self.amenity_repo.get_all()
        return [amenity.to_dict() for amenity in amenities]

    def update_amenity(self, amenity_id, amenity_data):
        # Mettre à jour une commodité existante
        amenity = self.get_amenity(amenity_id)
        if amenity:
            amenity.update(amenity_data)
            return amenity
        return None


def create_place(self, place_data):
    """create a place, including validation for price, latitude, and longitude"""
    pass


def get_place(self, place_id):
    """retrieve a place by ID, including associated owner and amenities"""
    pass


def get_all_places(self):
    """Placeholder for logic to retrieve all places"""
    pass


def update_place(self, place_id, place_data):
    # Placeholder for logic to update a place
    pass
