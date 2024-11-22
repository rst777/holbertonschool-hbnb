from flask import Flask
from models.db import get_db_session
from models.sqlalchemy_repository import SQLAlchemyRepository
from facade.hbnb_facade import HBnBFacade

app = Flask(__name__)

# Initialiser la façade avec une session SQLAlchemy
with get_db_session() as session:
    repository = SQLAlchemyRepository(session)
    facade = HBnBFacade(repository)
