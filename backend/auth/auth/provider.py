import os
from datetime import datetime
from typing import List
import hashlib
import jwt

from .store import UserStore
from .schemas import AuthUserBase, AuthUserStored


class AuthProvider(object):
    """provides auth for the application"""

    def __init__(self):
        self.users: UserStore = UserStore()

    @staticmethod
    def _gen_salt(salt_length: int = 32):
        return os.urandom(salt_length)

    def add_user(self, username: str, password: str, scopes: List[str]) -> bool:
        salt = self._gen_salt()
        hashed_password = self._hash_password(password, salt)
        self.users.add_user(
            AuthUserStored(
                username=username,
                hashed_password=hashed_password,
                salt=salt,
                scopes=scopes,
            )
        )
        return True

    def update_user(self, user: AuthUserBase) -> bool:
        stored_user = self.users.get_user(user.username)
        if not stored_user:
            return False
        stored_user.password = self._hash_password(user.password, stored_user.salt)
        self.users.update_user(stored_user)
        return True

    def delete_user(self, username: str):
        return self.users.remove_user(username)

    @staticmethod
    def _hash_password(password: str, salt: bytes):
        return hashlib.pbkdf2_hmac(
            hash_name="sha256",
            password=password.encode("utf8"),
            salt=salt,
            iterations=100_000,
            dklen=256,
        )

    def check_password(self, username: str, password: str) -> bool:
        user = self.users.get_user(username)
        if not user:
            return False

        test_hash = self._hash_password(password, user.salt)
        return bool(test_hash == user.hashed_password)

    def _gen_token(
        self,
        user: AuthUserStored,
        secret_key: str,
        expire_delta: int = 1,
    ) -> bytes:
        return jwt.encode(
            {
                "name": user.username,
                "scopes": user.scopes,
                "iat": datetime.utcnow(),
            },
            secret_key,
            algorithm="HS256",
        )

    def login(self, username: str, password: str, secret_key: str) -> bytes:
        if self.check_password(username, password):
            user = self.users.get_user(username)
            return self._gen_token(user, secret_key)
