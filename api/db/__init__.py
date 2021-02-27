from fastapi_quickstart import init_db
engine, Base, get_db = init_db('localhost', 'postgres', '1704', 'dummy')
