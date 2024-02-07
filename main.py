
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from table1 import Person

# Establish connection
connection_string = "postgresql://postgres:postgres@127.0.0.1:5432/test"
engine = create_engine(connection_string, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

result = session.query(Person).all()
for i in result:
    print(i)
