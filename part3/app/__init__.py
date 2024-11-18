from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask import Flask, jsonify

bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_name='default'):
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Load configuration
    from part3.config import config  # Import the config dictionary
    app.config.from_object(config[config_name])
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Create API
    api = Api(app, version='1.0', title='HBnB API',
              description='HolbertonBnB API')

    # Import namespaces
    from app.api.v1.users import api as users_ns
    from app.api.v1.places import api as places_ns
    from app.api.v1.amenities import api as amenities_ns
    from app.api.v1.reviews import api as reviews_ns

    # Register namespaces
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    return app

@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify({"error": "Missing or invalid token."}), 401

@jwt.invalid_token_loader
def invalid_token_callback(callback):
    return jsonify({"error": "Invalid token provided."})
