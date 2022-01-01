class NoMatchingUserException(Exception):
    pass


class UserExistsException(Exception):
    pass


class IncorrectLoginException(Exception):
    status_code: int = 401
    detail: str = "Incorrect username/password!"


class NoSecretKeyException(Exception):
    pass
