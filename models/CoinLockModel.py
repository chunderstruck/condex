from peewee import *

from models.BaseModel import BaseModel

class CoinLockModel(BaseModel):

    Ticker = CharField(unique=True, max_length=64)