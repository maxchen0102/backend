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
    
# 建立連線    
connection_string = "postgresql://postgres:postgres@127.0.0.1:5432/test"
engine=create_engine(connection_string, echo=False)
# 建立table 
Base.metadata.create_all(bind=engine) 

# (建立資料庫操作橋梁->config要哪個engine )
Session=sessionmaker(bind=engine)

# 實體化
session=Session()

# person=Person(123,"re",'m',12)
# session.add(person)
# session.commit()
# p1=Person(1,"chris",'m',12)
# p2=Person(23,"max",'m',121)
# p3=Person(12,"bob",'m',122)

# session.add(p1)
# session.add(p2)
# session.add(p3)
# session.commit()


result = session.query(Person).all()
for i in result:
    print(i)