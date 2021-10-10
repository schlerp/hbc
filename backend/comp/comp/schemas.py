from typing import List
from datetime import datetime
import pydantic


class BJCPStyle(pydantic.BaseModel):
    name: str
    category: str
    subcategory: str


class Competition(pydantic.BaseModel):
    competitionId: int
    allowedStyles: List[BJCPStyle]
    entriesCloseDate: datetime
    awardsDate: datetime
    description: str
