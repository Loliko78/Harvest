from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    nickname = StringField('Ник', validators=[DataRequired(), Length(min=3, max=32)])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=8, max=128)])
    submit = SubmitField('Зарегистрироваться')

class LoginForm(FlaskForm):
    nickname = StringField('Ник', validators=[DataRequired(), Length(min=3, max=32)])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=8, max=128)])
    submit = SubmitField('Войти') 