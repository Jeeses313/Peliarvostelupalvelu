from application import db
from sqlalchemy.orm import relationship
from application.auth.models import User
from application.reviews.models import Review

class Like(db.Model):
    __tablename__ = "liking"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    review_id = db.Column(db.Integer, db.ForeignKey('review.id'), nullable=False)
    
    def __init__(self, user_id, review_id):
        self.user_id = user_id
        self.review_id = review_id