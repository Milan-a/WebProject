from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, SubmitField
from wtforms.fields.choices import RadioField
from wtforms.validators import DataRequired

class ResumeAddForm(FlaskForm):
    title = StringField('Должность', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    gender = RadioField('Пол', choices=['Женский', 'Мужской'], validators=[DataRequired()])
    price = StringField('Желаемая зарплата', validators=[DataRequired()])
    experience = StringField('Опыт работы', validators=[DataRequired()])
    place_of_residence = StringField('Город/Место проживания', validators=[DataRequired()])
    last_place_of_work = StringField('Последнее место работы', validators=[DataRequired()])
    education = SelectField('Образование', choices=['Нету', 'Общее', 'Среднее', 'Высшее'], validators=[DataRequired()])
    specializations = TextAreaField('Специализации', validators=[DataRequired()])
    about_me = TextAreaField('"Обо мне"', validators=[DataRequired()])
    contacts = TextAreaField('Ваши контакты', validators=[DataRequired()])
    submit = SubmitField('Сохранить')