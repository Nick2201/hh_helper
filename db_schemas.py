
# Replace with your actual database configuration

from sqlalchemy import ( create_engine,
    MetaData, Table,Column,
    String, DateTime,Integer,Boolean,Text)
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

from sqlalchemy_utils import database_exists, create_database
# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение значений переменных окружения
host = os.getenv("HOST")
database = os.getenv("DATABASE")
user = os.getenv("USER")
port = os.getenv("PORT")
password = os.getenv("PASSWORD")

# Construct the database connection URL
connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(connection_string,echo=True)

if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))


metadata = MetaData()
table_vacancy = Table(
    'vacancy', metadata,
    Column('id', Integer(), primary_key=True),


    Column('experience_name', String(255)),
    Column('employment_id', String(20)),
    Column('employment_name', String(255)),
    Column('employer_id', String(20)),
    Column('employer_name', String(255)),
    Column('employer_url', String(255)),

    Column('working_days', String(255)),
    Column('working_time_intervals', String(255)),
    Column('working_time_modes', String(255)),
    Column('description', Text()),

    Column('type_id', String(50)),
    Column('type_name', String(255)),
    Column('key_skills', String(255)),
    Column('date',DateTime()),
    Column('date_pub',String(50)),
    Column('date_create',String(50)),

)


table_vac_page = Table(
    'vac_page', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(255)),
    Column('area_name', String(255)),
    Column('salary_from', Integer()),
    Column('salary_to', Integer()),
    Column('salary_currency', String(50)),
    Column('salary_gross', Boolean()),
    Column('requirement', Text()),
    Column('responsibility', Text()),
    Column('employer_name', String(255)),
    Column('experience_id', String(255)),
    Column('experience_name', String(255)),
    Column('date',DateTime())
)


# Create the table in the database
metadata.create_all(engine)

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# Session = sessionmaker(bind=engine)
# session = Session()

# Base = declarative_base()
# Base.metadata.drop_all(engine)

# # Close the session
# session.close()