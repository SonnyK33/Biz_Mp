from app.api import bp
from flask import jsonify, flash
from models import Users, Listings

@bp.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    flash('test')
    return jsonify(Users.query.get_or_404(id).to_dict())

@bp.route('/listings/<int:id>', methods=['GET'])    
def get_listings(id):
    return jsonify(Listings.query.get_or_404(id).to_dict())
    # return jsonify(Listings.query.get(id).to_dict())
