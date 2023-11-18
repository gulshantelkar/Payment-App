from peewee import Model, ForeignKeyField
from playhouse.postgres_ext import UUIDField, JSONField,ArrayField
from database import database
from peewee import *
import datetime
class BaseModel(Model):
    class Meta:
        database = database
        only_save_dirty = True

class User(BaseModel):
    id = UUIDField(constraints=[SQL("DEFAULT gen_random_uuid()")], primary_key=True,index=True)
    username = CharField(unique=True)
    email = CharField(unique=True)
    password_hash = CharField()
    created_at = DateTimeField(default=datetime.datetime.now, index=True)
    updated_at = DateTimeField(default=datetime.datetime.now, index=True)
    
    class Meta:
        table_name='user'