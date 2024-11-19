from flask import request, jsonify
from flask_restx import Namespace, Resource
from flask_jwt_extended import create_access_token

from app.models.user import User

user_data=[]

api = Namespace('auth', description="Authentication operations")

@api.route('/login')
class LoginResource(Resource):
    def post(self):
        """Authenticate user and return a JWT."""
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return {"error": "Email and password are required."}, 400

        # Simule une recherche utilisateur dans une base de données
        user = next((u for u in user_data if u.email == email), None)
        if not user or not user.check_password(password):
            return {"error": "Invalid credentials."}, 401

        # Génère le token JWT
        token = user.generate_jwt()
        return {"access_token": token}, 200
