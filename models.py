from datetime import datetime

from sqlalchemy_utils import PhoneNumberType

from app import db


# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(PhoneNumberType())
    genres = db.Column(db.String, nullable=False)
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.String(120))
    seeking_description = db.Column(db.String(500))



    artists = db.relationship('Artist', secondary='shows')
    shows = db.relationship('Show', backref='venues', lazy=True, cascade="all, delete-orphan")


class Artist(db.Model):
    __tablename__ = 'artist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(PhoneNumberType())
    genres = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website_link = db.Column(db.String(length=120))
    seeking_venue = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(500))




    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    shows = db.relationship('Show', backref='artists', lazy=True)


class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    show_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    venue = db.relationship('Venue')
    artist = db.relationship('Artist')


