from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<User {}>'.format(self._name)