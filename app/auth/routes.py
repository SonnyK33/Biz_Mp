from app.auth import bp
from flask import render_template

@bp.route('/login')
def login():
    Users = {'user':'Sonny'}
    return render_template('auth/login.html',title='login',users=Users)
