from typing import Annotated
from fastapi import Depends
from database import SessionLocal
from .localdb import get_db
from .auth import get_current_user

db_dependency = Annotated[SessionLocal, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]