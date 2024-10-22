from flask import Blueprint
from flask_restx import Api
from app.api.v1.amenities import api as amenities_api
from app.api.v1.users import api as users_api

blueprint = Blueprint('api', __name__)

# Créez l'instance de l'API
api = Api(
    blueprint,
    title='API HBnB',
    version='1.0',
    description='Une API pour gérer les utilisateurs et les données associées.'
)

# Enregistrement de l'espace de noms d'utilisateurs
api.add_namespace(users_api)
api.add_namespace(amenities_api, path='/api/v1/amenities')
# Ajoutez d'autres espaces de noms si nécessaire
# api.add_namespace(another_api)
