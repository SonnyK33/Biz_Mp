from app import create_app, db
from app.models import Users, Listings

app = create_app()

#decorator registers function as a shell context function and function is invoked when the flask shell command runs
@app.shell_context_processor
def make_shell_context():
    return {'db':db,'Users': Users, 'Listings': Listings}