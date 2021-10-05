from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    listings = db.relationship('Listings', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<user {}>'.format(self.username)

class Listings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bizname = db.Column(db.String(64), index=True)
    city = db.Column(db.String(64))
    country = db.Column(db.String(64))
    description = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __repr__(self):
        return '<listing {}>'.format(self.bizname)



