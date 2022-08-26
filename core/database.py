from .config import DATABASE_URL
import databases
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base


# init connection with database
database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)

# init base model
Base = declarative_base()

# init database metadata
meta_data = MetaData()

