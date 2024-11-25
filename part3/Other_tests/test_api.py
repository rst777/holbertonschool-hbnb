#!/usr/bin/python3
"""Test API endpoints"""
import unittest
import requests
import json
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class TestAPI(unittest.TestCase):
    """Test API class"""
    
    @classmethod
    def setUpClass(cls):
        """Setup test class"""
        cls.base_url = "http://localhost:5000/api/v1"
        cls.headers = {'Content-Type': 'application/json'}

    def test_status(self):
        """Test status endpoint"""
        r = requests.get(f"{self.base_url}/status")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), {"status": "OK"})

    def test_stats(self):
        """Test stats endpoint"""
        r = requests.get(f"{self.base_url}/stats")
        self.assertEqual(r.status_code, 200)
        stats = r.json()
        self.assertIn('users', stats)
        self.assertIn('states', stats)
        self.assertIn('cities', stats)
        self.assertIn('amenities', stats)
        self.assertIn('places', stats)
        self.assertIn('reviews', stats)

    def test_users(self):
        """Test users endpoints"""
        # Create user
        user_data = {
            "email": "test@test.com",
            "password": "test123",
            "first_name": "Test",
            "last_name": "User"
        }
        r = requests.post(
            f"{self.base_url}/users",
            headers=self.headers,
            data=json.dumps(user_data)
        )
        self.assertEqual(r.status_code, 201)
        user_id = r.json()['id']

        # Get user
        r = requests.get(f"{self.base_url}/users/{user_id}")
        self.assertEqual(r.status_code, 200)
        user = r.json()
        self.assertEqual(user['email'], user_data['email'])

        # Update user
        update_data = {"first_name": "Updated"}
        r = requests.put(
            f"{self.base_url}/users/{user_id}",
            headers=self.headers,
            data=json.dumps(update_data)
        )
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['first_name'], "Updated")

        # Delete user
        r = requests.delete(f"{self.base_url}/users/{user_id}")
        self.assertEqual(r.status_code, 200)

    def test_states(self):
        """Test states endpoints"""
        # Create state
        state_data = {"name": "California"}
        r = requests.post(
            f"{self.base_url}/states",
            headers=self.headers,
            data=json.dumps(state_data)
        )
        self.assertEqual(r.status_code, 201)
        state_id = r.json()['id']

        # Get state
        r = requests.get(f"{self.base_url}/states/{state_id}")
        self.assertEqual(r.status_code, 200)
        state = r.json()
        self.assertEqual(state['name'], state_data['name'])

        # Create city in state
        city_data = {"name": "San Francisco"}
        r = requests.post(
            f"{self.base_url}/states/{state_id}/cities",
            headers=self.headers,
            data=json.dumps(city_data)
        )
        self.assertEqual(r.status_code, 201)
        city_id = r.json()['id']

        # Get cities of state
        r = requests.get(f"{self.base_url}/states/{state_id}/cities")
        self.assertEqual(r.status_code, 200)
        cities = r.json()
        self.assertEqual(len(cities), 1)
        self.assertEqual(cities[0]['name'], city_data['name'])

    def test_places(self):
        """Test places endpoints"""
        # Setup: Create state, city and user first
        state = State(name="California")
        state.save()
        city = City(name="San Francisco", state_id=state.id)
        city.save()
        user = User(email="test@test.com", password="test123")
        user.save()

        # Create place
        place_data = {
            "name": "Test Place",
            "description": "Test Description",
            "number_rooms": 3,
            "number_bathrooms": 2,
            "max_guest": 6,
            "price_by_night": 100,
            "latitude": 37.774929,
            "longitude": -122.419416,
            "user_id": user.id
        }
        r = requests.post(
            f"{self.base_url}/cities/{city.id}/places",
            headers=self.headers,
            data=json.dumps(place_data)
        )
        self.assertEqual(r.status_code, 201)
        place_id = r.json()['id']

        # Get place
        r = requests.get(f"{self.base_url}/places/{place_id}")
        self.assertEqual(r.status_code, 200)
        place = r.json()
        self.assertEqual(place['name'], place_data['name'])

        # Search places
        search_data = {
            "states": [state.id],
            "cities": [city.id],
            "amenities": []
        }
        r = requests.post(
            f"{self.base_url}/places_search",
            headers=self.headers,
            data=json.dumps(search_data)
        )
        self.assertEqual(r.status_code, 200)
        places = r.json()
        self.assertEqual(len(places), 1)
        self.assertEqual(places[0]['name'], place_data['name'])

if __name__ == '__main__':
    unittest.main()