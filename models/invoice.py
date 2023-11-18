from peewee import Model, ForeignKeyField
from playhouse.postgres_ext import UUIDField, JSONField,ArrayField
from database import database
from peewee import *
from models.user import User
import datetime

class BaseModel(Model):
    class Meta:
        database = database
        only_save_dirty = True

class Invoice(BaseModel):
    id = UUIDField(constraints=[SQL("DEFAULT gen_random_uuid()")], primary_key=True,index=True)
    amount = DecimalField(index=True)
    description = CharField()
    receiver = ForeignKeyField(User, to_field='id')
    payer = ForeignKeyField(User, to_field='id')
    status = CharField(index=True)
    amount_recovered=DecimalField(index=True,default=0)
    created_at = DateTimeField(default=datetime.datetime.now, index=True)
    updated_at = DateTimeField(default=datetime.datetime.now, index=True)
    
    class Meta:
        table_name='invoice'