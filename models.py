from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


db = SQLAlchemy()


class User(db.Model):
    """ User model """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # reviews = db.relationship('Review')

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password


class Review(db.Model):
    """ Review model """
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    customername = db.Column(db.String(50), nullable=False)
    barbershopname = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    cash = db.Column(db.String, nullable=False)
    card = db.Column(db.String, nullable=False)
    vibe = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(1000), nullable=False)
    review_timestamp = db.Column(
        db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(
        self, customername, barbershopname, date, time,
            cash, card, vibe, rating, comments, review_timestamp, user_id):
        self.customername = customername
        self.barbershopname = barbershopname
        self.date = date
        self.time = time
        self.cash = cash
        self.card = card
        self.vibe = vibe
        self.rating = rating
        self.comments = comments
        self.review_timestamp = review_timestamp
        self.user_id = user_id
