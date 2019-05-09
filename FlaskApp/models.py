from datetime import datetime
from FlaskApp.extensions import db


class PC_memory(db.Model):
    timestamp = db.Column(db.Integer, primary_key=True)
    available = db.Column(db.Integer)
    used = db.Column(db.Integer)
    free = db.Column(db.Integer)
    percent = db.Column(db.Integer)


class InRun_memory(db.Model):
    timestamp = db.Column(db.Integer, primary_key=True)
