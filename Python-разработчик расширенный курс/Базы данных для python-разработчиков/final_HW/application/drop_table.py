import sqlalchemy
from sqlalchemy.orm import sessionmaker

from config import DSN
from models import  drop_table


engine  = sqlalchemy.create_engine(DSN)


Session = sessionmaker(bind=engine)
session = Session()

drop_table(engine)



