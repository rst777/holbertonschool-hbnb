from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuration de la base de données SQLite
DATABASE_URL = "sqlite:///hbnb_dev.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
