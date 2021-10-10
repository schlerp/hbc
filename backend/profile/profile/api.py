from typing import List
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .provider import ProfileProvider
from .schemas import UserProfile

app = FastAPI(
    title="HBC: Profile uService",
    description="Provides functions and storage of user profiles/bio's",
    version="0.0.1",
)
provider = ProfileProvider()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://0.0.0.0:3000",
    "http://localhost:5000",
    "http://0.0.0.0:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def get_prov():
    return provider


@app.get("/profile", response_model=List[UserProfile])
async def get_all_profiles(_prov: ProfileProvider = Depends(get_prov)):
    return _prov.get_profiles()


@app.get("/{username}")
async def get_profile(username: str, _prov: ProfileProvider = Depends(get_prov)):
    return _prov.get_profile(username)


@app.post("/profile")
async def create_profile(
    profile: UserProfile, _prov: ProfileProvider = Depends(get_prov)
):
    return _prov.create_profile(profile)


@app.put("/{username}")
async def update_profile(
    username: str, profile: UserProfile, _prov: ProfileProvider = Depends(get_prov)
):
    if profile.username == username:
        return _prov.update_profile(profile)
    raise HTTPException(500, "profile username in url/body do not match!")


@app.delete("/{username}")
async def remove_profile(username: str, _prov: ProfileProvider = Depends(get_prov)):
    return _prov.remove_profile(username)
