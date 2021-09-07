import os
from fastapi import FastAPI, Depends

from .provider import ProfileProvider
from .schemas import UserProfile

app = FastAPI()
provider = ProfileProvider()


async def get_prov():
    return provider


@app.get("/profile")
async def get_profile(
    username: str, auth_prov: ProfileProvider = Depends(get_prov)
):
    return auth_prov.get_profile(username)

@app.post("/profile")
async def create_profile(
    profile: UserProfile, auth_prov: ProfileProvider = Depends(get_prov)
):
    return auth_prov.create_profile(profile)

@app.put("/profile")
async def update_profile(
    profile: UserProfile, auth_prov: ProfileProvider = Depends(get_prov)
):
    return auth_prov.update_profile(profile)

@app.delete("/profile")
async def remove_profile(
    username: str, auth_prov: ProfileProvider = Depends(get_prov)
):
    return auth_prov.remove_profile(username)
