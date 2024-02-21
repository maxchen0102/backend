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

class Post(Base) :
    __tablename__="post" 

    post_id=Column(Integer,primary_key=True,autoincrement=True)
    post_title=Column(String)
    post_context=Column(String)
    Owner_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"))
    user=relationship("User")

class User(Base):
    __tablename__="users" 
    
    id=Column(Integer,autoincrement=True ,primary_key=True) 
    author=Column(String)  
    author_email=Column(String)
    author_password=Column(String)
    # post=relationship('Post',back_populates='user')


class Parent(Base):
    __tablename__ = "parent_table"
    id = Column(Integer, primary_key=True,autoincrement=True)
    
    ill_child=relationship(
        "Child",
        primaryjoin="and_(Parent.id==Child.parent_id,Child.illness==1)",
    )

class Child(Base):
    __tablename__ = "child_table"
    id = Column(Integer, primary_key=True,autoincrement=True)
    child_name=Column(String)
    illness=Column(Integer)
    parent_id = Column(Integer, ForeignKey("parent_table.id"))

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