from application import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    tag = db.Column(db.String(150), nullable=False)
    publication = db.Column(db.DateTime, nullable=False)
    flag = db.Column(db.Boolean, nullable=False)
    
    def __init__(self, name, tag, publication):
        self.name = name
        self.tag = tag
        self.publication = publication
        self.flag= False