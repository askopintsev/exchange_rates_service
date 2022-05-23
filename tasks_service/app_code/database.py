import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_NAME = os.getenv("DB_NAME", "exchange")
DB_HOST = os.getenv("DB_HOST", "db")

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}",
    convert_unicode=True, pool_recycle=3600, pool_size=10
)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
