#!/usr/bin/python3
"""Test de hashage du mot de passe"""
from models import storage
from models.user import User

# Créer un utilisateur
user = User(
    email="test@test.com",
    password="test123",
    first_name="Test",
    last_name="User"
)
user.save()

# Vérifier le hash
print(f"Mot de passe hashé: {user.password}")