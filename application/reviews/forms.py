from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField
from wtforms.validators import ValidationError, InputRequired 
from application.reviews.models import Review
from application import db
from flask_login import current_user

class ReviewForm(FlaskForm):
    game_id = HiddenField()
    grade = StringField("Arvosana: ", [InputRequired()])
    text = TextAreaField("Arvostelu: ", render_kw={"rows": 10, "cols": 30})
    
    def validate_game_id(form, field):
        game_id = form.game_id.data
        exists = Review.query.filter_by(user_id=current_user.id).filter_by(game_id=game_id).first()
        if(not (exists is None)):
            raise ValidationError("Olet jo tehnyt arvostelun tälle pelille")
    
    def validate_grade(form, field):
        grade = 0
        stringgrade = form.grade.data
        try:
            grade = int(stringgrade)
        except:
            raise ValidationError("Arvosanan täytyy olla kokonaisluku")
        if((grade < 0) or (grade > 5)):
                raise ValidationError("Arvosanan täytyy olla väliltä 0-5")
    
    def validate_text(form, field):
        text = form.text.data
        if(len(text) >= 300):
            raise ValidationError("Arvostelun pituus saa olla enintään 300 merkkiä")
        if(len(text) < 1):
            raise ValidationError("Arvostelu ei saa olla tyhjä")
    class Meta:
        csrf = False
        
class ReviewEditForm(FlaskForm):
    review_id = HiddenField()
    game_id = HiddenField()
    grade = StringField("Arvosana: ", [InputRequired()])
    text = TextAreaField("Arvostelu: ", render_kw={"rows": 10, "cols": 30})
    
    def validate_grade(form, field):
        grade = 0
        stringgrade = form.grade.data
        try:
            grade = int(stringgrade)
        except:
            raise ValidationError("Arvosanan täytyy olla kokonaisluku")
        if((grade < 0) or (grade > 5)):
                raise ValidationError("Arvosanan täytyy olla väliltä 0-5")
    
    def validate_text(form, field):
        text = form.text.data
        if(len(text) >= 300):
            raise ValidationError("Arvostelun pituus saa olla enintään 300 merkkiä")
        if(len(text) < 1):
            raise ValidationError("Arvostelu ei saa olla tyhjä")
    
    class Meta:
        csrf = False
  