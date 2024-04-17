from database import db
from datetime import datetime

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(80))
    date = db.Column(db.String(10))
    hour = db.Column(db.String(10))
    diet = db.Column(db.Boolean, nullable=False)


