from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
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

    def get_all_users(self):
        # Supposons que vous ayez une liste ou un dépôt d'utilisateurs
        return self.user_repo.get_all_users()

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
            return amenity.to_dict()  # Convertir l'objet en dict avant de le renvoyer
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
            place = Place(
                title=place_data['title'],
                description=place_data.get('description', ''),
                price=place_data['price'],
                latitude=place_data['latitude'],
                longitude=place_data['longitude'],
                owner_id=place_data['owner_id']
            )
            self.place_repo.add(place)
            return place.to_dict()

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise Exception("Place not found.")
        return place.to_dict()

    def get_all_places(self):
        places = self.place_repo.get_all()
        print(f"Retrieved places: {places}")
        return [place.to_dict() for place in self.place_repo.get_all()]

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            raise Exception("Place not found.")

        try:
            if 'title' in place_data:
                place.title = place_data['title']
            if 'description' in place_data:
                place.description = place_data.get('description', place.description)
            if 'price' in place_data:
                place.price = place_data['price']
            if 'latitude' in place_data:
                place.latitude = place_data['latitude']
            if 'longitude' in place_data:
                place.longitude = place_data['longitude']
            return place.to_dict()
        except ValueError as e:
            raise Exception(f"Invalid input data: {str(e)}")
