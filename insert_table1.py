
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from table1 import Person,Thing

# Establish connection
connection_string = "postgresql://postgres:postgres@127.0.0.1:5432/test"
engine = create_engine(connection_string, echo=True)

Session = sessionmaker(bind=engine)
session = Session()



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

p1=Person(2,"chris","m",35)
p2=Person(3,"max","m",15)

session.add(p1)
session.add(p2)
session.commit()

t1=Thing(1,"cat",p1.ssn)
t2=Thing(2,"lattop",p2.ssn)

session.add(t1)
session.add(t2)
session.commit()
