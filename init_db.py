from sqlalchemy import create_engine
from models import Base

DATABASE_URL = "postgresql+psycopg2://postgres:VS010203@localhost:5432/goit_hw_06"
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

print("Database create successfully!")
