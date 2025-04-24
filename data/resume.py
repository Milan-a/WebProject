import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Resume(SqlAlchemyBase):
    __tablename__ = 'resume'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # должность
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)  # возраст
    gender = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # пол
    price = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # желаемая зарплата (от - до)
    experience = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # опыт работы
    place_of_residence = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # место проживания
    last_place_of_work = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # последнее место работы
    education = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # образование
    specializations = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # список специализаций
    about_me = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # "обо мне"
    portfolio = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # портфолио (файл)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_private = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship('User')
