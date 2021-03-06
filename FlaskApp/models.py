from datetime import datetime
from extensions import db


class memory(db.Model):
    __tablename__ = 'memory'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Integer)
    used = db.Column(db.Integer)
    free = db.Column(db.Integer)


class InRun_memory(db.Model):
    timestamp = db.Column(db.Integer, primary_key=True)


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))

    def __init__(self, id, name):
        self.id = id
        self.name = name


class ceshi(db.Model):
    __tablename__ = 'ceshi'
    aaaa = db.Column(db.String(32))
    bbbb = db.Column(db.String(32))
    ID = db.Column(db.Integer, primary_key=True)

    def __init__(self, aaaa, bbbb, ID):
        self.aaaa = aaaa
        self.bbbb = bbbb
        self.ID = ID

class PCmemory(db.Model):
    __tablename__ = 'aaaaa'
    index = db.Column(db.Integer, primary_key=True)
    timeStamp = db.Column(db.DateTime,primary_key=True)
    total = db.Column(db.Integer)
    avai = db.Column(db.String(32))
    percent = db.Column(db.String(32))
    used = db.Column(db.Integer)
    free = db.Column(db.Integer)

    def __init__(self, index, timeStamp, total, avai, percent, used, free):
        self.index = index
        self.timeStamp = timeStamp
        self.total = total
        self.avai = avai
        self.percent = percent
        self.used = used
        self.free = free

