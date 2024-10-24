#!/user/bin/python3

import unittest
from app.models.place import Place
from app.models.user import User
from app.models.review import Review

class TestPlaceModel(unittest.TestCase):
    
    def test_place_creation(self):
        """Test la création d'un objet Place"""
        owner = User(first_name="Alice", last_name="Smith", email="alice@example.com")
        place = Place(title="Chalet", description="Un bel endroit", price=150.0, latitude=48.8566, longitude=2.3522, owner=owner)
        
        # Vérifier que les attributs sont correctement assignés
        self.assertEqual(place.title, "Chalet")
        self.assertEqual(place.description, "Un bel endroit")
        self.assertEqual(place.price, 150.0)
        self.assertEqual(place.latitude, 48.8566)
        self.assertEqual(place.longitude, 2.3522)
        self.assertEqual(place.owner, owner)

    def test_add_review(self):
        """Test l'ajout d'une review à un Place"""
        owner = User(first_name="Alice", last_name="Smith", email="alice@example.com")
        place = Place(title="Chalet", description="Un bel endroit", price=150.0, latitude=48.8566, longitude=2.3522, owner=owner)
        review = Review(text="Excellent endroit!", rating=5, place=place, user=owner)

        # Ajouter la review au Place
        place.add_review(review)

        # Vérifier que la review est bien ajoutée
        self.assertEqual(len(place.reviews), 1)
        self.assertEqual(place.reviews[0].text, "Excellent endroit!")

    def test_add_amenity(self):
        """Test l'ajout d'une amenity à un Place"""
        owner = User(first_name="Alice", last_name="Smith", email="alice@example.com")
        place = Place(title="Chalet", description="Un bel endroit", price=150.0, latitude=48.8566, longitude=2.3522, owner=owner)
        amenity = "Wi-Fi"

        # Ajouter une amenity au Place
        place.add_amenity(amenity)

        # Vérifier que l'amenity est bien ajoutée
        self.assertEqual(len(place.amenities), 1)
        self.assertEqual(place.amenities[0], "Wi-Fi")

class TestUserModel(unittest.TestCase):
    
    def test_user_creation(self):
        """Test la création d'un objet User"""
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com")

        # Vérifier les valeurs des attributs
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "john.doe@example.com")
        self.assertFalse(user.is_admin)

if __name__ == '__main__':
    unittest.main()

