import logging
from datetime import datetime

from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField, DateTimeField

logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

db = SqliteDatabase('sqlite3.db')

class BaseModel(Model):
    class Meta:
        database = db


class Student(BaseModel):
    name = CharField()
    age = IntegerField()


class Mark(BaseModel):
    student = ForeignKeyField(Student, backref='marks')
    value = IntegerField()
    timestamp = DateTimeField(default=datetime.now)


if __name__ == "__main__":
    db.connect()
    db.create_tables([Student, Mark])
    db.close()