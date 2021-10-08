import re
from app.auth import bp
from app.auth.forms import LoginForm, UserRegistration
from flask.templating import render_template
from flask_login import current_user, login_user, logout_user
from app.models import Users
from flask import redirect, url_for, flash
from app import db




@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()    

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid credentials')            
            return redirect ('login')
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))

    return render_template('auth/login.html',title='login',form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))



# need to modify database to get first and last name
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = UserRegistration()

    if form.validate_on_submit():        
        user = Users(username=form.username.data,email=form.email.data)                
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='register', form=form)


        