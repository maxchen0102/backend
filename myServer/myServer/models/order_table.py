
from cgitb import text
import enum
from sqlalchemy import SmallInteger, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, TEXT,sql,ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import ARRAY

from sqlalchemy.orm import relationship

Base = declarative_base()

class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, autoincrement=True)
    buyer = Column(String)
    product_id = Column(Integer, ForeignKey("product.id"))  # Corrected ForeignKey definition

class Product(Base):
    __tablename__ = "product"  # Corrected table name
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)
    price = Column(Integer)  # Changed field type to Integer for price
  