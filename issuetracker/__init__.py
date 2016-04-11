# __init__.py

from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from issuetracker.config import DevelopmentConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

engine = create_engine(app.config.get('DATABASE_URI'), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
Base.metadata.reflect(engine)


from issuetracker import views
