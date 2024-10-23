from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from app.models.user import User

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})

facade = HBnBFacade()

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')

    def get(self):
        """Retrieve a list of all users"""
        users = facade.get_all_users()  # Assurez-vous que cette méthode existe
        return users, 200
    
    def post(self):
        """Register a new user"""
        print("Received POST request")
        user_data = api.payload

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')

    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200


    @api.response(200, 'User updated successfully')
    @api.response(404, 'User not found')
    @api.response(400, 'Email already registered')
    def put(self, user_id):
            """Update a user by ID"""
            print(f"Received PUT request for user_id: {user_id}")
            user_data = api.payload
            print(f"Request payload: {user_data}")

            # Check if the user exists
            existing_user = facade.get_user(user_id)
            if not existing_user:
                return {'error': 'User not found'}, 404

            # Check for email uniqueness if the email is being changed
            if user_data['email'] != existing_user.email:
                duplicate_user = facade.get_user_by_email(user_data['email'])
                if duplicate_user:
                    return {'error': 'Email already registered'}, 400

            # Update the user's information
            existing_user.first_name = user_data['first_name']
            existing_user.last_name = user_data['last_name']
            existing_user.email = user_data['email']

            # Optionally, update the repository if using one
            facade.user_repo.update(existing_user.id, {
                'first_name': existing_user.first_name,
                'last_name': existing_user.last_name,
                'email': existing_user.email
            })
            return {
                'id': existing_user.id,
                'first_name': existing_user.first_name,
                'last_name': existing_user.last_name,
                'email': existing_user.email
            }, 200
