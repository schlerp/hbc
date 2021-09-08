import pydantic


class UserProfile(pydantic.BaseModel):
    username: str
    first_name: str
    last_name: str
    bio: str
    avatar: bytes
