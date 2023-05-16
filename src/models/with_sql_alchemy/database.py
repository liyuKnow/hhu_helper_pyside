# necessary modules
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .user import Base

# Define the path to the app data folder and create it if it doesn't exist
appdata_path = os.path.join(os.environ['APPDATA'], 'hhu_helper')
os.makedirs(appdata_path, exist_ok=True)

# Define the path to the database file within the app data folder
db_path = os.path.join(appdata_path, 'hhu_helper.db')

# Create a SQLAlchemy engine object that connects to the SQLite database at the specified path
engine = create_engine(f'sqlite:///{db_path}')

# Create the necessary tables in the database using the metadata defined in the user module
Base.metadata.create_all(engine)

# Create a session factory that will produce sessions bound to the engine
Session = sessionmaker(bind=engine)

# Create a session object that can be used to interact with the database
session = Session()