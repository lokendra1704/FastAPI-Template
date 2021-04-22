from fastapi_quickstart import init_db
import os

dbhost = os.environ["POSTGRE_HOSTNAME"]
dbport = os.environ["POSTGRE_PORT_NO"]
dbuser = os.environ["POSTGRE_USERNAME"]
dbpass = os.environ["POSTGRE_PWD"]
dbname = os.environ["POSTGRE_DBNAME"]

engine, Base, get_db = init_db(dbhost, dbuser, dbpass, dbname)
