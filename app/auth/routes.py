from app.auth import bp
from app.auth.forms import LoginForm
from flask.templating import render_template
from flask_login import current_user, login_user, logout_user
from models import Users
from flask import redirect, url_for, flash


# @bp.route('/login')
# def login():
#     form = LoginForm()
#     # Users = {'user':'Sonny'}
#     return render_template('login.html',title='login',form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()    

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid credentials')            
            return redirect ('auth.login')
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))

    return render_template('auth/login.html',title='login',form=form)