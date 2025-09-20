from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime, timezone

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    staffnumber = db.Column(db.String(10), nullable=False)
    firstaider = db.Column(db.Boolean, nullable=False)
    certificate_number = db.Column(db.String(6), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self): 
        return str(self.id)


class Accident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    date_of_accident = db.Column(db.Date, nullable=False)
    time_of_accident = db.Column(db.Time, nullable=False)
    first_aid_administered = db.Column(db.Boolean, nullable=False)
    first_aider_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True) 
    first_aid_details = db.Column(db.Text, nullable=False)

    date_reported = db.Column(db.DateTime, default=lambda: datetime.noe(timezone.utc))

    reporter_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reporter = db.relationship('User', foreign_keys=[reporter_id], backref='reported_accidents')

    first_aider = db.relationship('User', foreign_keys=[first_aider_id])