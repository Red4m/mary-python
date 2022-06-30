from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine
from classes import Base

engine = create_engine('postgresql://postgres:postgres@localhost/test', echo=False)
if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
