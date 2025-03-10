from logging import getLogger

from db.database import Base

logger = getLogger("uvicorn")

def create_tables(engine, checkfirst: bool = True):
  logger.info("Initialize tables if not exist.")
  Base.metadata.create_all(engine, checkfirst=checkfirst)

def initialize_table(engine, checkfirst: bool = True):
  logger.info("Initialize tables")
  create_tables(engine=engine, checkfirst=checkfirst)