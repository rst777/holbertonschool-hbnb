"""User model module for the HBnB application."""
from datetime import datetime
from app.models.base_model import BaseModel
import uuid
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token


bcrypt = Bcrypt


class User(BaseModel):
    """User Model"""
    def __init__(self, id, email, password, **kwargs):
        """Initialize user"""
        self.id = id
        self.set_password(password)
        self.email = email
        self.other_attributes = kwargs
    
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self , password):
        return bcrypt.check_password_hash(self._password, password)
    
    def generate_jwt(self):
        return create_access_token(identity={'id': self.id, 'email': self.email})
    
    @property
    def password(self):
        raise AttributeError("Password is write-only!")
    
    def to_dict(self):
        user_dict = self._dict_.copy()
        user_dict.pop('_password', None)
        return user_dict 

    def validate(self):
        """Validate user data"""
        if not self.first_name or not self.first_name.strip():
            raise ValueError("first_name cannot be empty")
        if not self.last_name or not self.last_name.strip():
            raise ValueError("last_name cannot be empty")
        if not self.email or not self.email.strip():
            raise ValueError("email cannot be empty")
        if '@' not in self.email:
            raise ValueError("Invalid email format")
