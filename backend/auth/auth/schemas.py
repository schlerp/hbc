from typing import List
import pydantic


class AuthUserBase(pydantic.BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class LoginRequest(AuthUserBase):
    pass

    class Config:
        orm_mode = True


class LoginResponse(pydantic.BaseModel):
    username: str
    scopes: List[str]
    email: str
    token: str

    class Config:
        orm_mode = True


class AuthUserRegister(AuthUserBase):
    email: str

    class Config:
        orm_mode = True


class AuthUserStored(pydantic.BaseModel):
    username: str
    email: str
    hashed_password: bytes
    salt: bytes
    scopes: List[str]

    class Config:
        orm_mode = True
