from typing import Optional, Union, Dict, Sequence
import os
from datetime import datetime, timezone
import jwt
import uuid

from exceptions import NoSecretKeyException


def _create_token(
    self,
    subject: Union[str, int],
    type_token: str,
    exp_time: Optional[int],
    fresh: Optional[bool] = False,
    algorithm: Optional[str] = "HS256",
    headers: Optional[Dict] = None,
    issuer: Optional[str] = None,
    audience: Optional[Union[str, Sequence[str]]] = None,
    user_claims: Optional[Dict] = {},
) -> str:
    """
    Create token for access_token and refresh_token (utf-8)
    :param subject: Identifier for who this token is for example id or username from database.
    :param type_token: indicate token is access_token or refresh_token
    :param exp_time: Set the duration of the JWT
    :param fresh: Optional when token is access_token this param required
    :param algorithm: algorithm allowed to encode the token
    :param headers: valid dict for specifying additional headers in JWT header section
    :param issuer: expected issuer in the JWT
    :param audience: expected audience in the JWT
    :param user_claims: Custom claims to include in this token. This data must be dictionary
    :return: Encoded token
    """
    # Validation type data
    if not isinstance(subject, (str, int)):
        raise TypeError("subject must be a string or integer")
    if not isinstance(fresh, bool):
        raise TypeError("fresh must be a boolean")
    if audience and not isinstance(audience, (str, list, tuple, set, frozenset)):
        raise TypeError("audience must be a string or sequence")
    if algorithm and not isinstance(algorithm, str):
        raise TypeError("algorithm must be a string")
    if user_claims and not isinstance(user_claims, dict):
        raise TypeError("user_claims must be a dictionary")

    # Data section
    current_time = int(datetime.now(timezone.utc))
    reserved_claims = {
        "sub": subject,
        "iat": current_time,
        "nbf": current_time,
        "jti": str(uuid.uuid4()),
    }

    custom_claims = {"type": type_token}

    # for access_token only fresh needed
    if type_token == "access":
        custom_claims["fresh"] = fresh

    if exp_time:
        reserved_claims["exp"] = exp_time
    if issuer:
        reserved_claims["iss"] = issuer
    if audience:
        reserved_claims["aud"] = audience

    secret_key = os.environ.get("SECRET_KEY", None)
    if secret_key is None:
        raise NoSecretKeyException

    return jwt.encode(
        {**reserved_claims, **custom_claims, **user_claims},
        secret_key,
        algorithm=algorithm,
        headers=headers,
    ).decode("utf-8")
