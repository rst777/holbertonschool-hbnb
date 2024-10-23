from flask import Blueprint
from flask_restx import Api
from app.api.v1.amenities import api as amenities_api
from app.api.v1.users import api as users_api
from app.api.v1.places import api as places_api


# Créez et configurez le blueprint
blueprint = Blueprint('api_v1', __name__)

# Créez l'instance de l'API avec la documentation
api = Api(
    blueprint,
    title='API HBnB',
    version='1.0',
    description='Une API pour gérer les utilisateurs et les données associées.'
)

# Enregistrement des espaces de noms
api.add_namespace(users_api, path='/users')
api.add_namespace(amenities_api, path='/amenities')
api.add_namespace(places_api, path='/places')
