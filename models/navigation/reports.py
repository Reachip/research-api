import datetime
from peewee import Model, CharField, IntegerField, PrimaryKeyField
from .. import db 

class NavigationReports(Model):
    id = PrimaryKeyField()
    timestamp = CharField(default=datetime.datetime.now())
    ph = IntegerField()
    temperature = IntegerField()
    longitude = CharField()
    latitude = CharField()
    
    class Meta:
        database = db 
        