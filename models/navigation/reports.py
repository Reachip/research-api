import datetime
from peewee import Model, CharField, IntegerField, DecimalField
from .. import db 

class NavigationReports(Model):
    timestamp = CharField(default=str(datetime.datetime.now))
    PH = IntegerField()
    temperature = IntegerField()
    longitude = DecimalField()
    latitude = DecimalField()
    
    class Meta:
        database = db 
        