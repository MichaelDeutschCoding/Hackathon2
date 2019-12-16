from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, Form
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(max=15)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(max=80)])
    first_name = StringField('first name', validators=[InputRequired(), Length(max=15)])
    last_name = StringField('last name', validators=[InputRequired(), Length(max=15)])
