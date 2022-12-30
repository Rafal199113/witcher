from tabnanny import check
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField ,EmailField, DecimalField,SubmitField,  validators

class Edit(FlaskForm):
    username = StringField('Login',[validators.Length(min=4, max=25)])
    password1 = PasswordField('Hasło',[ validators.DataRequired()])
    age=DecimalField('wiek',[validators.number_range(10,100,"Ta gra jest zbyt brutalna dla ciebie:)")])
    email = EmailField('Adress email',[validators.DataRequired()])
    submit= SubmitField('Prześlij dane')
    