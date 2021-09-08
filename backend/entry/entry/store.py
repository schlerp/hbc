from typing import List

from .schemas import CompetitionEntry
from .exceptions import EntryExistsException, NoMatchingEntryException


class EntryStore(object):
    def __init__(self):
        self._store: List[CompetitionEntry] = []

    def get_all(self) -> List[CompetitionEntry]:
        return self._store

    def add_entry(self, entry: CompetitionEntry) -> bool:
        try:
            self.get_entry(entry.entry_id)
            raise EntryExistsException
        except NoMatchingEntryException:
            pass
        self._store.append(entry)
        return True

    def remove_entry(self, entry_id: int):
        entry = self.get_entry(entry_id)
        if not entry:
            return NoMatchingEntryException
        self._store.remove(entry)

    def get_entry(self, entry_id: int) -> CompetitionEntry:
        matching_entrys = [x for x in self._store if x.entry_id == entry_id]
        if not matching_entrys:
            raise NoMatchingEntryException
        return matching_entrys[0]

    def update_entry(self, entry: CompetitionEntry) -> bool:
        stored_entry = self.get_entry(entry.entry_id)
        if not stored_entry:
            raise NoMatchingEntryException
        self._store.remove(stored_entry)
        self._store.append(entry)
