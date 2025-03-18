# app/items.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import Item
from app import db

items_bp = Blueprint('items', __name__)

@items_bp.route('/public/items', methods=['GET'])
def public_items():
    items = Item.query.all()
    items_list = [{"id": item.id, "name": item.name, "description": item.description} for item in items]
    return jsonify(items_list), 200

@items_bp.route('/items', methods=['GET'])
@jwt_required()
def get_items():
    items = Item.query.all()
    items_list = [{"id": item.id, "name": item.name, "description": item.description} for item in items]
    return jsonify(items_list), 200

@items_bp.route('/items', methods=['POST'])
@jwt_required()
def create_item():
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({"msg": "Missing item name"}), 400
    
    item = Item(name=data['name'], description=data.get('description', ''))
    db.session.add(item)
    db.session.commit()
    return jsonify({
        "msg": "Item created",
        "item": {"id": item.id, "name": item.name, "description": item.description}
    }), 201

@items_bp.route('/items/<int:item_id>', methods=['GET'])
@jwt_required()
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify({"id": item.id, "name": item.name, "description": item.description}), 200

@items_bp.route('/items/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    data = request.get_json()
    if not data:
        return jsonify({"msg": "No data provided"}), 400
    
    item.name = data.get('name', item.name)
    item.description = data.get('description', item.description)
    db.session.commit()
    return jsonify({
        "msg": "Item updated",
        "item": {"id": item.id, "name": item.name, "description": item.description}
    }), 200

@items_bp.route('/items/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"msg": "Item deleted"}), 200