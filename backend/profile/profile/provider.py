from typing import Dict, List
from .store import ProfileStore
from .schemas import UserProfile


class ProfileProvider(object):
    def __init__(self):
        self._store = ProfileStore()
        self.create_profile(
            UserProfile(
                username="admin",
                firstName="Johnny",
                lastName="Admin",
                bio="I am the admin user, look at me!",
                avatar="https://randomuser.me/api/portraits/men/3.jpg",
            )
        )
        self.create_profile(
            UserProfile(
                username="derp",
                firstName="Derping",
                lastName="Derpson",
                bio="I am a derp head, bleep blerp heep schlerp.",
                avatar="https://randomuser.me/api/portraits/women/3.jpg",
            )
        )

    def get_profile(self, username: str) -> UserProfile:
        return self._store.get_profile(username)

    def create_profile(self, profile: UserProfile) -> bool:
        return self._store.add_profile(profile)

    def update_profile(self, profile: UserProfile) -> bool:
        return self._store.update_profile(profile)

    def remove_profile(self, username: str) -> bool:
        return self._store.remove_profile(username)
