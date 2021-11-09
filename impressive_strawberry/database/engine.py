import sqlalchemy.orm
from os import environ


engine = sqlalchemy.create_engine(environ["IS_DB_URI"])
Session = sqlalchemy.orm.sessionmaker(bind=engine)
