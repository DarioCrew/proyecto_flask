from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.fields.html5 import EmailField

from .models import User

def codi_validator(form,field):
    if field.data.lower() == 'codi':
        raise validators.ValidationError('El username no es permitido')


class LoginForm(Form):
    username = StringField('Usuario',[
        validators.length(min=4, max=50,message="EL nombre se ecuentra fuera de rango")
    ])
    password = PasswordField('Password',[
        validators.Required(message='el passqword es requerido')
    ])

class RegisterForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50),
        codi_validator
    ])
    email = EmailField('Correo electronico', [
        validators.length(min=6, max=100),
        validators.Required(message='El email es requerido'),
        validators.Email(message='Ingrese un email valido')
    ])
    password = PasswordField('Password', [
        validators.Required('El password es requerido'),
        validators.EqualTo('confirm_password',message='La constrasenia no coincide')
    ])
    confirm_password = PasswordField('Confirm password')
    accept= BooleanField('',[
        validators.DataRequired()
    ])

    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError('El username ya se encuentra en uso')

    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError('El email ya se encuentra en uso') 

class TaskForm(Form):
    title = StringField('Titulo',[
        validators.length(min=4, max=50, message='Titulo fuera de rango'),
        validators.DataRequired(message='El titulo es requerido'),

    ])
    description = TextAreaField('Descripcion',[
        validators.DataRequired(message='La descripcion es requerida')
    ], render_kw={'rows':5})