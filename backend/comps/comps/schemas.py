from typing import List
from datetime import datetime
import pydantic


class BJCPStyle(pydantic.BaseModel):
    name: str
    category: str
    subcategory: str


class Competition(pydantic.BaseModel):
    competition_id: int
    allowed_styles: List[BJCPStyle]
    entries_close_date: datetime
    awards_date: datetime
    description: str
