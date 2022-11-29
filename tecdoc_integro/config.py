from sqlalchemy import create_engine
import pymysql
from os import environ, path
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

pymysql.install_as_MySQLdb()
#
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))
#
engine = create_engine(environ.get('DATABASE_URL'), echo=True)
Base = declarative_base(engine)
#


TESTING = True
DEBUG = True
FLASK_ENV = 'development'
SECRET_KEY = environ.get('SECRET_KEY')

def load_session():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

