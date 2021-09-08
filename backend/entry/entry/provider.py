from typing import Dict, List
from .store import EntryStore
from .schemas import CompetitionEntry


class EntryProvider(object):
    def __init__(self):
        self._store = EntryStore()

    def get_all(self) -> List[CompetitionEntry]:
        return self._store.get_all()

    def get_entry(self, entry_id: int) -> CompetitionEntry:
        return self._store.get_entry(entry_id)

    def create_entry(self, entry: CompetitionEntry) -> bool:
        return self._store.add_entry(entry)

    def update_entry(self, entry: CompetitionEntry) -> bool:
        return self._store.update_entry(entry)

    def remove_entry(self, entry_id: int) -> bool:
        return self._store.remove_entry(entry_id)
