
from cgitb import text
import enum
from sqlalchemy import SmallInteger, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, TEXT,sql
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import ARRAY

class BaseField: 
    mother_name=Column(Integer)
    father_name=Column(String)


class BaseField2 : 
    grandfather_name=Column(String)

class AuditMixin(BaseField,BaseField2):
    pass

