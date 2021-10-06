from flask.templating import render_template
from app.main import bp
from app.auth.forms import LoginForm
from config import Config
from flask import flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from models import Users

@bp.route('/')
@bp.route('/index')
def index():
    Users = {'username':'SonnyK'}
    return render_template('index.html',title="Home",Users=Users)

# moved this here temporarily for testing, needs to go back to auth/routes.py

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()    

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid credentials')            
            return redirect ('/login')
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html',title='login',form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



    # for database:
    #     seller name, contact info, name of business, description, asking price
    #      
    