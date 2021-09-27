from typing import Literal, Optional
import pydantic


class UserAPIDetails(pydantic.BaseModel):
    user_id: str
    api_key: str
    api_type: Optional[Literal["brewfather"]]
    enabled: bool = True
    shared_recipe: bool = True
    shared_invetory: bool = False

    class Config:
        orm_mode = True
