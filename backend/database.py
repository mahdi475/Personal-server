from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import settings

# The engine keeps a pool of open connections to PostgreSQL.
# pool_pre_ping checks that a connection still works before using it.
engine = create_engine(settings.database_url, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    """Parent class for all database tables."""


def get_db():
    """Give each request its own database session and close it afterwards."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
