from fastapi_quickstart import init_auth
from ..db import get_db
from ..crud import usercrud

logindep, get_user = init_auth('secret', get_db, usercrud)
