from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import TextAreaField, BooleanField, TelField, EmailField
from wtforms.validators import DataRequired


class VacanciesAddForm(FlaskForm):
    title = StringField('Название вакансии', validators=[DataRequired()])
    company = StringField('Название компании', validators=[DataRequired()])
    price = StringField('Зарплата', validators=[DataRequired()])
    experience = StringField('Требуемый опыт работы', validators=[DataRequired()])
    address = StringField('Адрес работы', validators=[DataRequired()])
    schedule = StringField('График работы', validators=[DataRequired()])
    hours = SelectField('Занятость', choices=['Другое', 'Полная занятость', 'Частичная занятость', 'Проектная работа', 'Подработка',
                                 'Стажировка'], validators=[DataRequired()])
    phone = TelField('Номер телефона для связи', validators=[DataRequired()])
    email = EmailField('Почта для связи', validators=[DataRequired()])
    description = TextAreaField('Подробное описание вакансии', validators=[DataRequired()])
    submit = SubmitField('Сохранить')
