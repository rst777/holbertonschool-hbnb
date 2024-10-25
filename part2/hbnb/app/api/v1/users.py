#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from app.services import facade  # Assure-toi que le facade est bien configuré

api = Namespace('users', description='User operations')

# Modèle pour valider les données de l'utilisateur
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='Prénom de l\'utilisateur'),
    'last_name': fields.String(required=True, description='Nom de l\'utilisateur'),
    'email': fields.String(required=True, description='Email de l\'utilisateur')
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'Utilisateur créé avec succès')
    @api.response(400, 'Email déjà enregistré')
    def post(self):
        """Enregistre un nouvel utilisateur"""
        user_data = api.payload

        # Vérification d'unicité de l'email
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email déjà enregistré'}, 400

        new_user = facade.create_user(user_data)
        return {
            'id': new_user.id,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email
        }, 201
    
    def get(self):
        """Récupère la liste de tous les utilisateurs"""
        users = facade.get_all_users()  # Ajouter cette méthode dans la facade
        return [{
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        } for user in users], 200

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'Détails de l\'utilisateur récupérés avec succès')
    @api.response(404, 'Utilisateur non trouvé')
    def get(self, user_id):
        """Récupère les détails d'un utilisateur par ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'Utilisateur non trouvé'}, 404
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200
    
    def put(self, user_id):
        """Met à jour les informations de l'utilisateur"""
        user_data = api.payload
        updated_user = facade.update_user(user_id, user_data)  # Ajoute cette méthode dans la facade
        if not updated_user:
            return {'error': 'Utilisateur non trouvé'}, 404
        return {
            'id': updated_user.id,
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'email': updated_user.email
        }, 200
