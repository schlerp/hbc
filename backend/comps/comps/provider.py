from typing import Dict, List
from .store import CompStore
from .schemas import Competition


class CompProvider(object):
    def __init__(self):
        self._store = CompStore()

    def get_comp(self, competition_id: int) -> Competition:
        return self._store.get_comp(competition_id)

    def create_comp(self, comp: Competition) -> bool:
        return self._store.add_comp(comp)

    def update_comp(self, comp: Competition) -> bool:
        return self._store.update_comp(comp)

    def remove_comp(self, competition_id: int) -> bool:
        return self._store.remove_comp(competition_id)
