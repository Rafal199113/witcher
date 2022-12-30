from tabnanny import check
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, PasswordField ,EmailField, DecimalField,SubmitField,  validators

class registerBeast(FlaskForm):
    id=DecimalField("Id",[validators.DataRequired()])
    name = StringField('Nazwa',[validators.Length(min=4, max=25)])
    weeknes=StringField("Słabości")
    drop=StringField("Łupy")
    info=TextAreaField("Opis",[validators.DataRequired()])
    image=StringField("Image src",[validators.DataRequired()])
    submit= SubmitField('Prześlij')
    