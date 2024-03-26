from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired('Введите имя')])
    title = StringField('Тема', validators=[DataRequired('Заполните тему')])
    question = TextAreaField('Коммент', validators=[DataRequired('Заполните коммент')])
    button = SubmitField('Отправить')
