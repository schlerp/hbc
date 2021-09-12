import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .provider import AuthProvider
from .schemas import LoginRequest, AuthUserRegister, LoginResponse

app = FastAPI(
    title="HBC: Auth uService",
    description="Provides authentication and authorization for the rest of the microservices using JWT's",
    version="0.0.1",
)
auth_provider = AuthProvider()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://0.0.0.0:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def get_prov():
    return auth_provider


@app.post("/login", response_model=LoginResponse)
async def login(
    login_details: LoginRequest, auth_prov: AuthProvider = Depends(get_prov)
):
    return auth_prov.login(
        login_details.username,
        login_details.password,
        os.environ.get("SECRET_KEY", "123"),
    )


@app.post("/signup")
async def signup(
    register_details: AuthUserRegister,
    auth_prov: AuthProvider = Depends(get_prov),
):
    return auth_prov.add_user(
        register_details.username, register_details.password, register_details.email, []
    )
