#!/user/bin/python3

from app.models.place import Place
from app.models.user import User

def test_place_creation():
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=100, latitude=37.7749, longitude=-122.4194, owner=owner)
    assert place.title == "Cozy Apartment"
    assert place.price == 100
    assert place.owner == owner

test_place_creation()
