from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://plivo:plivo@192.168.0.113:5432/plivo", echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)