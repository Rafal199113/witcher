from tabnanny import check
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, PasswordField ,EmailField, DecimalField,SubmitField,  validators

class News(FlaskForm):
    id=DecimalField("Id",[validators.DataRequired()])
    name = StringField('Nazwa',[validators.Length(min=4, max=25)])
    info=TextAreaField("Informacje")
    charakter=StringField("Url")
    image=StringField("Image src",[validators.DataRequired()])
    submit= SubmitField('Prześlij')