from application import db
from sqlalchemy.orm import relationship
from application.auth.models import User
from application.games.models import Game

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(300), nullable=False)
    flag = db.Column(db.Boolean, nullable=False)

    
    def __init__(self, game_id, grade, text):
        self.grade = grade
        self.text = text
        self.flag= False