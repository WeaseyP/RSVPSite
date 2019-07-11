from rsvp import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    party_of = db.Column(db.String(2), nullable = False)
    user = db.relationship('RSVP', backref='data', lazy =True)

    def get_party():
        return int(User.party_of) 

    def __repr__(self):
        return f"User('{self.username}','{self.id}','{self.party_of}'')"

class RSVP(db.Model):
    rsvp_id = db.Column(db.Integer, primary_key=True)
    party_attending = db.Column(db.Integer, nullable = False)
    attending = db.Column(db.Text)
    food = db.Column(db.Text)
    music = db.Column(db.Text)
    note = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship(User)


    def __repr__(self):
        return f"User('{self.rsvp_id}', '{self.party_attending}','{self.attending}',  '{self.food}', '{self.music}', '{self.note}','{self.note}','{self.user_id}')"

