from tabnanny import check
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, PasswordField ,EmailField, DecimalField,SubmitField,  validators

class registerGlo(FlaskForm):
    id=DecimalField("Id",[validators.DataRequired()])
    name = StringField('Imie',[validators.Length(min=4, max=25)])
    info=TextAreaField("Informacje")
    charakter=TextAreaField("Charakter")
    look=TextAreaField("Opis",[validators.DataRequired()])
    image=StringField("Image src",[validators.DataRequired()])
    submit= SubmitField('Prześlij')
    