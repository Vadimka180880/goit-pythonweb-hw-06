from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
 
load_dotenv()  

db_user = os.getenv("DB_USER") 
db_password = os.getenv("DB_PASSWORD")    
db_host = os.getenv("DB_HOST") 
db_name = os.getenv("DB_NAME") 

DATABASE_URL = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}/{db_name}"  

engine = create_engine(DATABASE_URL) 
Session = sessionmaker(bind=engine) 
