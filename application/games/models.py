from application import db
from sqlalchemy.orm import relationship


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    tag = db.Column(db.String(150), nullable=False)
    publication = db.Column(db.DateTime, nullable=False)
    flag = db.Column(db.Boolean, nullable=False)
    reviews = db.relationship("Review", backref='game', lazy=True)
    
    def __init__(self, name, tag, publication):
        self.name = name
        self.tag = tag
        self.publication = publication
        self.flag= False