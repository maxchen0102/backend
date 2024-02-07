from sqlalchemy import create_engine,ForeignKey ,Column,String,Integer,CHAR 
#from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker,declarative_base


Base= declarative_base()

class Person(Base):
    __tablename__ ="people"
    
    ssn =Column("ssn",Integer,primary_key=True ) # ssn 是python 裡面的使用名稱 
    firstname=Column("firstname",String)  # "firstname",是db 裡面的欄位名稱 
    gender=Column("gender",CHAR)
    age=Column("age",Integer)
    
# 建立物件的時候，可以產生instance 
    def __init__(self,ssn,first,gender,age):
        self.ssn=ssn 
        self.firstname=first
        self.gender=gender
        self.age=age
    
#這樣才可以回傳string 給我們做debug 
    def __repr__(self):
        
        return f"({self.ssn}){self.firstname}({self.gender}{self.age})"
    

class Thing(Base): 
    __tablename__= "things"

    tid=Column("tid",Integer,primary_key=True) 
    description=Column('description',String)
    owner =Column(Integer,ForeignKey("people.ssn"))

    def __init__(self,tid,description,owner):
        self.tid=tid 
        self.description=description
        self.owner=owner

    def __repr__(self):
        
        return f"({self.tid}){self.description} ownerd by {self.owner}"
    
# 建立連線    
connection_string = "postgresql://postgres:postgres@127.0.0.1:5432/test"
engine=create_engine(connection_string, echo=False)
# 建立table 
Base.metadata.create_all(bind=engine) 



