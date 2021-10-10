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
                description="The start of the year competition!",
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
