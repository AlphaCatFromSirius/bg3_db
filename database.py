from config import DB_USER, DB_PASSWORD, DB_NAME, DB_HOST
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
