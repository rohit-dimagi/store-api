from loguru import logger

from database import Base, engine
from models import Item
try:
    logger.info("Running DB Migration..")
    Base.metadata.create_all(engine)
except Exception as e:
    logger.opt(exception=True).error(f"Error During DB Migration: {e}")
    raise
