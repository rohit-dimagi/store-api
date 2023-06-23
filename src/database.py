from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from settings import Settings

try:
    logger.info("Creating DB Connection...")
    db_url = f"postgresql://{Settings().db_user}:{Settings().db_password}@{Settings().db_host}:{Settings().db_port}/{Settings().db_name}"
    engine = create_engine(db_url, echo=Settings().debug)

    Base = declarative_base()

    SessionLocal = sessionmaker(bind=engine)
except Exception as e:
    logger.opt(exception=True).error(f"Error During DB Connection: {e}")
    raise
