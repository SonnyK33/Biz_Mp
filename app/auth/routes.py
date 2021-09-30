from app.auth import bp
from app.auth.forms import LoginForm
from flask.templating import render_template


@bp.route('/login')
def login():
    form = LoginForm()
    # Users = {'user':'Sonny'}
    return render_template('login.html',title='login',form=form)
