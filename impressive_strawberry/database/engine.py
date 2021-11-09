import sqlalchemy.orm
from os import environ


engine = sqlalchemy.create_engine(environ["sqlalchemy.uri"])
Session = sqlalchemy.orm.sessionmaker(bind=engine)
