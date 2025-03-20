'''
auth.py
This module handles user authentication using JWT (JSON Web Tokens). 
It includes routes for user login, token generation, and protected access control.
Users must provide valid credentials to receive a token, which is required for admin routes.
'''
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"msg": "Missing username or password"}), 400
    
    user = User.query.filter_by(username=data.get('username')).first()
    if not user or not user.check_password(data.get('password')):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=str(user.id))
    return jsonify(access_token=access_token), 200

@auth_bp.route('/protected', methods=['GET', 'POST'])
@jwt_required()
def protected():
    current_user_id_str = get_jwt_identity()
    user = User.query.get(int(current_user_id_str))
    
    if not user:
        return jsonify({"msg": "User not found"}), 404

    response_data = {
        "msg": "Token accepted",
        "logged_in_as": user.username,
        "method": request.method
    }
    return jsonify(response_data), 200