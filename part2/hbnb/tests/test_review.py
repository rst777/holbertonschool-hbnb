#!/user/bin/python3

from app.models.review import Review
from app.models.user import User
from app.models.place import Place

def test_review_creation():
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=100, latitude=37.7749, longitude=-122.4194, owner=owner)
    review = Review(text="Great stay!", rating=5, place=place, user=owner)
    assert review.text == "Great stay!"
    assert review.rating == 5
    assert review.place == place
    assert review.user == owner

test_review_creation()
