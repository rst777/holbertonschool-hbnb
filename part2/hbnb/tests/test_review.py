from app.models.review import Review
from app.models.user import User
from app.models.place import Place

def test_review_creation():
    # Créer un utilisateur et un lieu
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=100, latitude=37.7749, longitude=-122.4194, owner=user)

    # Créer un avis
    review = Review(text="Great stay!", rating=5, place=place, user=user)

    # Vérifier que l'avis a été créé avec les bonnes valeurs
    assert review.text == "Great stay!"
    assert review.rating == 5
    assert review.place == place
    assert review.user == user
    print("Review creation test passed!")

# Appeler la fonction de test
test_review_creation()
