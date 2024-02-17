from sqlalchemy import create_engine,ForeignKey ,Column,String,Integer,CHAR ,Date,UnicodeText
#from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker,declarative_base


Base= declarative_base()
# 建立連線    
connection_string = "postgresql://postgres:postgres@127.0.0.1:5432/test"
engine=create_engine(connection_string, echo=False)

class PID(Base):
    __tablename__="pid"

    id=Column(Integer,primary_key=True,autoincrement=True) 
    name=Column(String(55),nullable=False)
    author=Column(String,nullable=False)

def create_table() :
    Base.metadata.create_all(engine)

def drop_table():
    Base.metadata.drop_all(engine)

def creat_sessoin():
    Session=sessionmaker(bind=engine) 
    session=Session()
    return session
    

if __name__=='__main__': 
    print("refresh table done")
    drop_table()
    create_table()

   
print("Executing table1.py")




