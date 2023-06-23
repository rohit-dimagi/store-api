from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import Settings
from loguru import logger


try:
    logger.info("Creating DB Connection...")
    db_url= f"postgresql://{Settings().db_user}:{Settings().db_password}@{Settings().db_host}:{Settings().db_port}/{Settings().db_name}"
    engine = create_engine(db_url, echo=Settings().debug)

    Base = declarative_base()

    SessionLocal = sessionmaker(bind=engine)
except Exception as e:
    logger.opt(exception=True).error(f"Error During DB Connection: {e}")
    raise