
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from table1 import Person,Thing

# Establish connection
connection_string = "postgresql://postgres:postgres@127.0.0.1:5432/test"
engine = create_engine(connection_string, echo=True)

Session = sessionmaker(bind=engine)
session = Session()


# row=session.query(Person,Thing).filter(Thing.owner==Person.ssn).filter(Person.firstname=="chris").first()
# if row:
#     print("data=",row[0])  # Accessing column 'ssn'
  

x= session.query(Person).get(3) 
print(type(x))
print(x)

x =session.get(Person,2)
print(x)
print(x.ssn)