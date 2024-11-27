import pytest
from api.v1.app import app
from models import storage

@pytest.fixture
def client():
    """Provide a Flask test client."""
    with app.test_client() as client:
        yield client

@pytest.fixture
def test_data():
    """Fixture for setting up test data."""
    # Exemple de setup
    storage.reload()  # Assurez-vous que cette méthode existe dans `models.storage`
    yield
    storage.close()  # Assurez-vous que cette méthode existe aussi

@pytest.fixture
def headers():
    """Headers fixture for JSON requests."""
    return {'Content-Type': 'application/json'}
