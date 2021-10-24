from typing import Dict, List
from datetime import datetime
from .store import CompStore
from .schemas import Competition


class CompProvider(object):
    def __init__(self):
        self._store = CompStore()
        self.create_comp(
            Competition(
                competitionId=1,
                allowedStyles=[
                    {"name": "Black IPA", "category": "11", "subcategory": "c"},
                    {"name": "Saison", "category": "12", "subcategory": "b"},
                ],
                entriesCloseDate=datetime.fromisoformat("2021-01-01"),
                awardsDate=datetime.fromisoformat("2021-02-01"),
                description="The start of the year competition! Some really long text about what we expect htis comp to be like. Why not add in another sentence just to see? is thi long enough yet, what do you think?",
            )
        )
        self.create_comp(
            Competition(
                competitionId=2,
                allowedStyles=[
                    {"name": "Pale Ale", "category": "6", "subcategory": "b"},
                    {
                        "name": "Russian Imperial Stout",
                        "category": "12",
                        "subcategory": "b",
                    },
                    {"name": "Saison", "category": "12", "subcategory": "b"},
                    {"name": "Black IPA", "category": "11", "subcategory": "c"},
                    {"name": "Saison", "category": "12", "subcategory": "b"},
                ],
                entriesCloseDate=datetime.fromisoformat("2021-10-04"),
                awardsDate=datetime.fromisoformat("2021-10-16"),
                description="The End of the year competition! This is the first AABC certified competition for NT Homebrewers!",
            )
        )

    def get_all_comps(
        self,
    ) -> List[Competition]:
        return self._store.get_all_comps()

    def get_comp(self, competition_id: int) -> Competition:
        return self._store.get_comp(competition_id)

    def create_comp(self, comp: Competition) -> bool:
        return self._store.add_comp(comp)

    def update_comp(self, comp: Competition) -> bool:
        return self._store.update_comp(comp)

    def remove_comp(self, competition_id: int) -> bool:
        return self._store.remove_comp(competition_id)
