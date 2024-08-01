from pydantic import BaseModel, EmailStr
from typing import Annotated
from fastapi import Query


class CreateUser(BaseModel):
    username: Annotated[str, Query(min_length=1, max_length=5)]
    email: EmailStr
