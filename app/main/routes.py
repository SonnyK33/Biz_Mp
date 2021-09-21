from flask.templating import render_template
from app.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    Users = {'username':'Sonny'}
    return render_template('index.html',title="Home",Users=Users)

    # for database:
    #     seller name, contact info, name of business, description, asking price
    #      
    