from peewee import Model, CharField, IntegerField, PrimaryKeyField
from .. import db 

class Robot(Model):
    latitude = CharField()
    longitude = CharField()