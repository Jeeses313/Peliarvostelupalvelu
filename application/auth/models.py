from application import db

class User(db.Model):

    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    reviews = db.relationship("Review", backref='user', lazy=True)
    likes = db.relationship("Like", backref='user', lazy=True)

    def __init__(self, username, password, admin):
        self.username = username
        self.password = password
        self.admin = admin
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True