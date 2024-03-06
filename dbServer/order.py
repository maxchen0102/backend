from cgitb import text
import enum
from sqlalchemy import SmallInteger, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, TEXT,sql,ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import ARRAY
import mixins
from sqlalchemy.orm import relationship

Base = declarative_base()
engine_url = "postgresql://postgres:postgres@127.0.0.1:5432/test"
engine = create_engine(engine_url, echo=True)


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
  

     

def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)


def create_session():
    Session = sessionmaker(bind=engine)
    session = Session()

    return session

class Status(enum.Enum):
    """商城狀態"""

    LOWER = 2  # 已下架
    SHELVES = 3  # 上架中
    VIOLATION = 4  # 違規
    PERIOD = 5  # 指定時間


if __name__ == '__main__':
    drop_table()
    create_table()
    print("create table")