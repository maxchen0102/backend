
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from table1 import Person,Thing

# Establish connection
connection_string = "postgresql://postgres:postgres@127.0.0.1:5432/test"
engine = create_engine(connection_string, echo=True)

Session = sessionmaker(bind=engine)
session = Session()


row=session.query(Person,Thing).filter(Thing.owner==Person.ssn).filter(Person.firstname=="chris").first()
if row:
    print("data=",row[0])  # Accessing column 'ssn'
  


# results=session.query(Person).all()
# for row in results: 
#     print("ssn=", row.ssn ,"|",row.firstname,"|",row.gender,"|",row.age)

# a =session.query(Person).filter(Person.firstname=="chris").all()
# print(type(a))

# for i in a : 
#     print ("name=" ,i.firstname)
#     print(i)