import pydantic


class UserProfile(pydantic.BaseModel):
    username: str
    firstName: str
    lastName: str
    bio: str
    avatar: str
    favouriteStyle: str = "Water"
    active: bool = True
