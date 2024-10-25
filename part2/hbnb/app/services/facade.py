#!/usr/bin/python3
from app.models.user import User
from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        pass

    def get_place(self, place_id):
        pass

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.list_all()

    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if user:
            user.update(user_data)  # Hypothèse: méthode d'update définie dans le modèle User
            self.user_repo.update(user_id, user)
            return user
        return None
