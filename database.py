from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from settings import DATABASE

DB_URL = f'postgresql+psycopg2://{DATABASE["DB_USER"]}:{DATABASE["DB_PASSWORD"]}@{DATABASE["DB_HOST"]}:{DATABASE["DB_PORT"]}/{DATABASE["DB_NAME"]}'

engine = create_engine(DB_URL)

Base = declarative_base(engine)
