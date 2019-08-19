from app import db


class Weather(db.Model):
    """Simple database model to track event attendees."""

    __tablename__ = 'weather'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    temperature = db.Column(db.Integer)

    def __init__(self, time=None, email=None):
        self.time = time
        self.temperature = temperature
