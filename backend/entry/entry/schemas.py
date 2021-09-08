import pydantic


class CompetitionEntry(pydantic.BaseModel):
    username: str
    competition_id: int
    entry_id: int
    name: str
    category: str
    subcategory: str
    notes: str

    class Config:
        orm_mode = True
