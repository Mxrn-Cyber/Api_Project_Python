from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from core.setting import setting


engine = create_engine(
    setting.DATABASE_URL, connect_args={'sslmode': 'require'},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
