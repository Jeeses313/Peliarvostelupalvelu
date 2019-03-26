from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import ValidationError, InputRequired 
from application.games.models import Game
from application import db
import datetime
class GameForm(FlaskForm):
    name = StringField("Pelin nimi: ", [InputRequired()])
    tag = StringField("Pelin tunnus: ", [InputRequired()])
    publication = StringField("Pelin julkaisupäivä (YYYY-MM-DD): ", [InputRequired()])
    def validate_name(form, field):
        name = form.name.data
        exists = Game.query.filter_by(name=name).first()
        if(not (exists is None)):
            raise ValidationError("Peli on jo tietokannassa")
        if(len(name) >= 150):
            raise ValidationError("Nimen pituus saa olla enintään 150 merkkiä")
    
    def validate_tag(form, field):
        tag = form.tag.data
        if(len(tag) >= 150):
            raise ValidationError("Tunnisteen pituus saa olla enintään 150 merkkiä")
        
    def validate_publication(form, field):
        try:
            datetime.datetime.strptime(form.publication.data, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Päivämäärän muoto on väärä")
    
    class Meta:
        csrf = False
        
class GameEditForm(FlaskForm):
    oldName = HiddenField()
    name = StringField("Uusi nimi: ", [InputRequired()])
    tag = StringField("Uusi tunnus: ", [InputRequired()])
    publication = StringField("Uusi julkaisupäivä (YYYY-MM-DD): ", [InputRequired()])
    
    def validate_name(form, field):
        name = form.name.data
        oldName = form.oldName.data
        exists = Game.query.filter_by(name=name).first()
        if(not (exists is None)):
            if(not (name == oldName)):
                raise ValidationError("Peli on jo tietokannassa")
        if(len(name) >= 150):
            raise ValidationError("Nimen pituus saa olla enintään 150 merkkiä")
            
    def validate_tag(form, field):
        tag = form.tag.data
        if(len(tag) >= 150):
            raise ValidationError("Tunnisteen pituus saa olla enintään 150 merkkiä")

    
    def validate_publication(form, field):
        try:
            datetime.datetime.strptime(form.publication.data, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Päivämäärän muoto on väärä")
    
    class Meta:
        csrf = False
  