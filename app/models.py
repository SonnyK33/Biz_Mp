from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Users(UserMixin, db.Model):
    __tablename__ ="users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    listings = db.relationship('Listings', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<user {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)

    def to_dict(self):
        data = {
            'id': self.id,
            'username': self.username
        }
        return data

    

class Listings(db.Model):
    __tablename__ ="listings"
    id = db.Column(db.Integer, primary_key=True)
    bizname = db.Column(db.String(64), index=True)
    city = db.Column(db.String(64))
    country = db.Column(db.String(64))
    description = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __repr__(self):
        return '<listing {}>'.format(self.bizname)

    def to_dict(self):
        data = {
            'bizname': self.bizname,
            'description': self.description
        }
        return data


@login.user_loader
def load_user(id):
    return Users.query.get(int(id))



