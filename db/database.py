from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
SQLALCHEMY_DATABASE_URL = "postgresql://dbsentinel_user:t5QOr20WW0KDdFDgZfXFhc0uVYSNzqV8@dpg-d36uc3re5dus738s319g-a.virginia-postgres.render.com:5432/dbsentinel"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()