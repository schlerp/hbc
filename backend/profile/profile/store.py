from typing import List

from .schemas import UserProfile
from .exceptions import ProfileExistsException, NoMatchingProfileException


class ProfileStore(object):
    def __init__(self):
        self._store: List[UserProfile] = []

    def add_profile(self, profile: UserProfile) -> bool:
        if self.get_profile(profile.username):
            raise ProfileExistsException
        self._store.append(profile)
        return True

    def remove_profile(self, username: str) -> bool:
        profile = self.get_profile(username)
        if profile:
            self._store.remove(profile)
            return True
        return False

    def get_profile(self, username: str) -> UserProfile:
        matching_profiles = [x for x in self._store if x.username == username]
        return matching_profiles[0] if matching_profiles else None

    def get_profiles(self) -> List[UserProfile]:
        return [profile for profile in self._store if profile.active]

    def update_profile(self, profile: UserProfile) -> bool:
        stored_profile = self.get_profile(profile.username)
        if not stored_profile:
            raise NoMatchingProfileException
        self._store.remove(stored_profile)
        self._store.append(profile)
        return True
