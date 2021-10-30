import pytest
import jwt

from ..provider import AuthProvider


def test_add_user():
    auth_local = AuthProvider()
    username = "test_add_user"
    auth_local.add_user(
        username=username, password="testing123", email="test@test.com", scopes=[]
    )
    assert auth_local.users.get_user(username).username == username


def test_add_remove_user():
    auth = AuthProvider()
    username = "test_add_remove_user"
    auth.add_user(
        username=username, password="testing123", email="test@test.com", scopes=[]
    )
    auth.users.remove_user(username=username)
    assert not auth.users.get_user(username)


def test_successful_password():
    auth = AuthProvider()
    username = "test_user"
    password = "bleep"
    auth.add_user(
        username=username, password=password, email="test@test.com", scopes=["admin"]
    )
    assert auth.check_password(username, password)


def test_unsuccessful_password():
    auth = AuthProvider()
    username = "test_user"
    password = "bleep"
    auth.add_user(
        username=username, password=password, email="test@test.com", scopes=["admin"]
    )
    assert not auth.check_password(username, "WRONG")


def test_unsuccessful_invalid_user():
    auth = AuthProvider()
    username = "test_user"
    password = "bleep"
    auth.add_user(
        username=username, password=password, email="test@test.com", scopes=["admin"]
    )
    assert not auth.check_password("IDONTEXIST", password)


def test_token():
    auth = AuthProvider()
    username = "test_user"
    password = "bleep"
    secret_key = "super_secret"
    auth.add_user(
        username=username, password=password, email="test@test.com", scopes=["admin"]
    )
    assert auth.login(username, password, secret_key)


def test_token_scope_empty():
    auth = AuthProvider()
    username = "test_user"
    password = "bleep"
    secret_key = "super_secret"
    scopes = []
    auth.add_user(
        username=username, password=password, email="test@test.com", scopes=scopes
    )
    user = auth.login(username, password, secret_key)
    assert (
        jwt.decode(user["token"], key=secret_key, algorithms=["HS256"]).get("scopes")
        == scopes
    )


def test_user_scope_single():
    auth = AuthProvider()
    username = "test_user"
    password = "bleep"
    secret_key = "super_secret"
    scopes = ["1"]
    auth.add_user(
        username=username, password=password, email="test@test.com", scopes=scopes
    )
    user = auth.login(username, password, secret_key)
    assert (
        jwt.decode(user["token"], key=secret_key, algorithms=["HS256"]).get("scopes")
        == scopes
    )


def test_user_scope_multiple():
    auth = AuthProvider()
    username = "test_user"
    password = "bleep"
    secret_key = "super_secret"
    scopes = ["1", "2", "3"]
    auth.add_user(
        username=username, password=password, email="test@test.com", scopes=scopes
    )
    user = auth.login(username, password, secret_key)
    assert (
        jwt.decode(user["token"], key=secret_key, algorithms=["HS256"]).get("scopes")
        == scopes
    )
