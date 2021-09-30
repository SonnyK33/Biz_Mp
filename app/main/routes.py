from flask.templating import render_template
from app.main import bp
from app.auth.forms import LoginForm

@bp.route('/')
@bp.route('/index')
def index():
    Users = {'username':'Sonny'}
    return render_template('index.html',title="Home",Users=Users)

# moved this here temporarily for testing, needs to go back to auth/routes.py
@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # Users = {'user':'Sonny'}
    return render_template('login.html',title='login',form=form)



    # for database:
    #     seller name, contact info, name of business, description, asking price
    #      
    