from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import ValidationError, InputRequired 
from application.auth.models import User
from application import db

class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi: ")
    password = PasswordField("Salasana: ")
    
    class Meta:
        csrf = False
        
class RegisterForm(FlaskForm):
    username = StringField("Käyttäjänimi: ", [InputRequired()])
    password = PasswordField("Salasana: ")
    passwordSec = PasswordField("Salasana toisen kerran: ", [InputRequired()])
    
    def validate_username(form, field):
        username = form.username.data
        exists = User.query.filter_by(username=username).first()
        if(not (exists is None)):
            raise ValidationError("Käyttäjänimi varattu")
        if(len(username) >= 50):
            raise ValidationError("Käyttäjänimen pituus saa olla enintään 50 merkkiä")
       
    def validate_passwordSec(form, field):
        password = form.password.data
        passwordSec = form.passwordSec.data
        if(not (password == passwordSec)):
            raise ValidationError("Kirjoita sama salasana molempiin kohtiin")
        if(len(password) >= 50):
            raise ValidationError("Salasanan pituus saa olla enintään 50 merkkiä")

    class Meta:
        csrf = False