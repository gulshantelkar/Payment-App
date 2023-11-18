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

class InvoiceTransaction(BaseModel):
    id = UUIDField(constraints=[SQL("DEFAULT gen_random_uuid()")], primary_key=True,index=True)
    invoice = ForeignKeyField(Invoice, to_field='id')
    amount = DecimalField()
    payment_date = DateTimeField(default=datetime.datetime.now,index=True)
    payment_mode = CharField(index=True)
    
    class Meta:
        table_name='invoice_transaction'