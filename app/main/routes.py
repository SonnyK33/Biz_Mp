from app import db
from flask.templating import render_template
from flask_login.utils import login_required
from app.main import bp
from app.auth.forms import LoginForm
from config import Config
from flask import flash, redirect, url_for, jsonify
from flask_login import current_user, login_user, logout_user
from app.models import Listings, Users
import time

#template to be changed - should be first page post-logging in

@bp.route('/')
@bp.route('/index')
@login_required
def index():    
    return render_template('index.html',title="Home",Users=Users)

@bp.route('/user/<username>')
@login_required
def user(username):
    if current_user.is_authenticated:
      
        user = Users.query.filter_by(username=username).first_or_404()
        return render_template('user.html',user=user)


@bp.route('/listings')
def listings():    
    # listings = Listings.query.order_by(Listings.bizname.desc())
    listings = Listings.query.join(Users).order_by(Listings.bizname.desc())

    

    # user_email=db.session.query(Listings).join(Users)
    # email = Users.query.join(Listings).order_by(Listings.bizname.desc())
    email = Users.query.join(Listings)
    e = {i: email.filter(Users.id==i.user_id).first().email for i in listings}
    # email = Users.query.join(Listings).filter(Users.id==Listings.user_id)   
    return render_template('listings.html',listings=listings,e=e)
    


# this isn't working in api directory; not sure why
@bp.route('/users/<int:id>', methods=['GET'])
def get_user_api(id):  
    return jsonify(Users.query.get_or_404(id).to_dict())

@bp.route('/listings-api/<int:id>', methods=['GET']) 
def get_listings(id):   
    return jsonify(Listings.query.get_or_404(id).to_dict())

@bp.route('/time')
def get_current_time():
    return {'time': time.time()}

