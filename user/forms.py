from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired


# форма для регистрации
class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired('Заполните имя!')])
    email = EmailField('Email', validators=[DataRequired('Введите email')])
    password = PasswordField('Пароль', validators=[DataRequired('Заполните пароль')])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired('Заполните пароль ещё раз!')])
    button = SubmitField('Зарегестрироваться')

# форма для логина
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired('Введите email')])
    password = PasswordField('Пароль', validators=[DataRequired('Заполните пароль')])
    button = SubmitField('Войти')
