from typing import List

from .schemas import Competition
from .exceptions import CompExistsException, NoMatchingCompException


class CompStore(object):
    def __init__(self):
        self._store: List[Competition] = []

    def add_comp(self, comp: Competition) -> bool:
        if self.get_comp(comp.competition_id):
            raise CompExistsException
        self._store.append(comp)
        return True

    def remove_comp(self, competition_id: int) -> bool:
        comp = self.get_comp(competition_id)
        if comp:
            self._store.remove(comp)
            return True
        return False

    def get_comp(self, competition_id: int) -> Competition:
        matching_comps = [x for x in self._store if x.competition_id == competition_id]
        return matching_comps[0] if matching_comps else None

    def update_comp(self, comp: Competition) -> bool:
        stored_comp = self.get_comp(comp.competition_id)
        if not stored_comp:
            raise NoMatchingCompException
        self._store.remove(stored_comp)
        self._store.append(comp)
        return True
