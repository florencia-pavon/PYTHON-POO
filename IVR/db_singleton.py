
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# Crear el engine
engine = create_engine('sqlite:///ivr.db')

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()
