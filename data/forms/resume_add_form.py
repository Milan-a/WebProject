from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, IntegerField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ResumeAddForm(FlaskForm):
    title = StringField('Должность', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    gender = SelectField('Пол', choices=[('Мужской', 'Мужской'), ('Женской', 'Женской')])
    price = StringField('Желаемая зарплата')
    experience = StringField('Опыт работы')
    place_of_residence = StringField('Место проживания')
    last_place_of_work = StringField('Последнее место работы')
    education = StringField('Образование')
    specializations = TextAreaField('Специализации')
    about_me = TextAreaField('Обо мне')
    portfolio = FileField('Портфолио')
    image = FileField('Загрузить изображение')  # Поле для загрузки изображения
    submit = SubmitField('Создать резюме')