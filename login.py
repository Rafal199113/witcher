from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField

class Singup(FlaskForm):
    username=StringField("Loign")
    password= PasswordField("Password")

    submit= SubmitField('Sing in')