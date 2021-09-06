from typing import List

from .schemas import CompetitionEntry
from .exceptions import EntryExistsException, NoMatchingEntryException


class EntryStore(object):
    def __init__(self):
        self._store: List[CompetitionEntry] = []

    def add_entry(self, entry: CompetitionEntry) -> bool:
        if self.get_entry(entry.entry_id):
            raise EntryExistsException
        self._store.append(entry)
        return True

    def remove_entry(self, entry_id: int) -> bool:
        entry = self.get_entry(entry_id)
        if entry:
            self._store.remove(entry)
            return True
        return False

    def get_entry(self, entry_id: int) -> CompetitionEntry:
        matching_entrys = [x for x in self._store if x.entry_id == entry_id]
        return matching_entrys[0] if matching_entrys else None

    def update_entry(self, entry: CompetitionEntry) -> bool:
        stored_entry = self.get_entry(entry.entry_id)
        if not stored_entry:
            raise NoMatchingEntryException
        self._store.remove(stored_entry)
        self._store.append(entry)
        return True
