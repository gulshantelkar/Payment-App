from peewee import Model, ForeignKeyField
from playhouse.postgres_ext import UUIDField, JSONField,ArrayField
from database import database
from peewee import *
from models.user import User
from models.invoice import Invoice
import datetime

class BaseModel(Model):
    class Meta:
        database = database
        only_save_dirty = True

class AuthToken(BaseModel):
    id = UUIDField(constraints=[SQL("DEFAULT gen_random_uuid()")], primary_key=True,index=True)
    user = ForeignKeyField(User, to_field='id')
    token = CharField(unique=True)
    expiration_date = DateTimeField()
    
    class Meta:
        table_name='authtoken'