from typing import List
import pydantic


class AuthUserBase(pydantic.BaseModel):
    username: str
    password: str


class AuthUserStored(pydantic.BaseModel):
    username: str
    hashed_password: bytes
    salt: bytes
    scopes: List[str]
