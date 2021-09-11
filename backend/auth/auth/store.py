from typing import List

from .schemas import AuthUserStored, AuthUserRegister
from .exceptions import UserExistsException, NoMatchingUserException


class UserStore(object):
    def __init__(self):
        self._store: List[AuthUserStored] = []

    def add_user(self, user: AuthUserRegister) -> bool:
        if self.get_user(user.username):
            raise UserExistsException
        self._store.append(user)
        return True

    def remove_user(self, username: str) -> bool:
        user = self.get_user(username)
        if user:
            self._store.remove(user)
            return True
        return False

    def get_user(self, username: str) -> AuthUserStored:
        matching_users = [x for x in self._store if x.username == username]
        return matching_users[0] if matching_users else None

    def update_user(self, user: AuthUserStored) -> bool:
        stored_user = self.get_user(user.username)
        if not stored_user:
            raise NoMatchingUserException
        self._store.remove(stored_user)
        self._store.append(user)
        return True
