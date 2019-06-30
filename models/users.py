from peewee import Model, CharField
from . import db  

class Users(Model):
    username = CharField()
    password = CharField()
    mail = CharField()
    role = CharField(default="public")

    class Meta:
        database = db