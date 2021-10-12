from flask.templating import render_template
from flask_login.utils import login_required
from app.main import bp
from app.auth.forms import LoginForm
from config import Config
from flask import flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.models import Users

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

