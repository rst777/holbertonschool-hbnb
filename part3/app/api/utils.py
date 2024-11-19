from flask_jwt_extended import get_jwt_identity
from functools import wraps 
from flask import jsonify
from models import storage


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        current_user_id = get_jwt_identity()
        current_user = storage.get("User", current_user_id)
        if not current_user or not current_user.is_admin:
            return jsonify({"error": "Access forbiden: Admins only"}), 403
        return fn (*args, **kwargs)
    return wrapper
