import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Vacancies(SqlAlchemyBase):
    __tablename__ = 'vacancies'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # название вакансии
    company = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # название компании
    price = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # зарплата (от - до)
    experience = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # требуемый опыт работы (от - до)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # адрес работы
    schedule = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # график работы
    hours = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)  # рабочие часы
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # полное описание
    phone = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)  # номер телефона для связи
    emile = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)  # почта для связи
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)  # дата создания
    is_private = sqlalchemy.Column(sqlalchemy.Boolean, default=True)  # приватность
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship('User')
