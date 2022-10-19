from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .cessao_fundo import *
import os
from .base import Base

engine = create_engine(
    os.environ["DB_CONNECTION_STRING"],
)
Base.metadata.create_all(engine)
