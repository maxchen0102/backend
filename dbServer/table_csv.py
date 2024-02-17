from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, TEXT
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine_url = "postgresql://postgres:postgres@127.0.0.1:5432/test"
engine = create_engine(engine_url, echo=True)


class DataCsv(Base):
    __tablename__ = "datacsv"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Seq = Column(String)
    DateListed = Column(String(100))
    year = Column(String(8182))  # Chrome 網址長度上限
    level = Column(String(100))
    identity = Column(String(8182))  # Chrome 網址長度上限
    gentle = Column(String(8182))  # Chrome 網址長度上限
    gentle_code = Column(String)
    register_number = Column(String)
    test_number = Column(String)
    pass_number = Column(String)

def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)


def create_session():
    Session = sessionmaker(bind=engine)
    session = Session()

    return session


if __name__ == '__main__':
    drop_table()
    create_table()
    print("create table")