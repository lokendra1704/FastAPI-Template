
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

print('Running DB')


def init_db(dbhost, dbuser, dbpass, dbname, dbport):
    """Parameters:
    db_host: Hostname of PostgreSQL DB,
    db_user: Username of PostgreSQL DB,
    dbpass: Password of PostgreSQL DB,
    dbname: Database Name of PostgreSQL DB

    Returns: engine, Base, get_db
    Please Note: JWT tokens are made from email attribute in User.
    """

    SQLALCHEMY_DATABASE_URL = f"postgresql://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}"
    print(SQLALCHEMY_DATABASE_URL)
    engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

    def get_db():
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()
    return engine, Base, get_db


#dotenv.load_dotenv("./api/.env", verbose=True)
dbhost = os.environ["POSTGRE_HOSTNAME"]
dbport = os.environ["POSTGRE_PORT_NO"]
dbuser = os.environ["POSTGRE_USERNAME"]
dbpass = os.environ["POSTGRE_PWD"]
dbname = os.environ["POSTGRE_DBNAME"]

engine, Base, get_db = init_db(dbhost, dbuser, dbpass, dbname, dbport)
