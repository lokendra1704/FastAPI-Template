from fastapi_quickstart import getCrudClass, getUserCrudClass
from ..models.user import User
from ..schemas.user import UserIn, UserUpdate
CRUDUser = getUserCrudClass(User, UserIn, UserUpdate)
usercrud = CRUDUser(User)
