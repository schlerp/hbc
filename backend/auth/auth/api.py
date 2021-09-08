import os
from fastapi import FastAPI, Depends

from .provider import AuthProvider

app = FastAPI(
    title="HBC: Auth uService",
    description="Provides authentication and authorization for the rest of the microservices using JWT's",
    version="0.0.1",
)
auth_provider = AuthProvider()


async def get_prov():
    return auth_provider


@app.get("/login")
async def read_auth(
    username: str, password: str, auth_prov: AuthProvider = Depends(get_prov)
):
    return auth_prov.login(username, password, os.environ.get("SECRET_KEY", 123))


@app.post("/signup")
async def add_user(
    username: str, password: str, auth_prov: AuthProvider = Depends(get_prov)
):
    return auth_prov.add_user(username, password, [])
