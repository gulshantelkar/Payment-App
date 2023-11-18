from peewee import Model, ForeignKeyField
from playhouse.postgres_ext import UUIDField, JSONField,ArrayField
from database import database
from peewee import *
from models.user import User
class BaseModel(Model):
    class Meta:
        database = database
        only_save_dirty = True

class UserRole(BaseModel):
    id = UUIDField(constraints=[SQL("DEFAULT gen_random_uuid()")], primary_key=True,index=True)
    user_id = ForeignKeyField(User, to_field='id')
    role = CharField(index=True)
    
    class Meta:
        table_name='user_role'