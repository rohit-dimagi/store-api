from database import Base, engine

from loguru import logger

try:
    logger.info("Running DB Migration..")
    Base.metadata.create_all(engine)
except Exception as e:
    logger.opt(exception=True).error(f"Error During DB Migration: {e}")
    raise