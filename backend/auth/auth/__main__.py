import uvicorn

from .api import app

uvicorn.run(app, host="0.0.0.0")

# from .provider import AuthProvider

# auth = AuthProvider()

# username = "derp"
# password = "bleep"

# auth.add_user(username=username, password=password, scopes=["admin"])
# print("added user/password: {}/{}".format(username, password))

# print(
#     "testing username/password for match: {}/{} {}".format(
#         username, password, auth.check_password(username, password)
#     )
# )

# print(
#     "testing username/password for match: {}/{} {}".format(
#         "I DONT EXIST", password, auth.check_password("I DONT EXIST", password)
#     )
# )

# print(
#     "testing username/password for match: {}/{} {}".format(
#         username, "WRONG PASSWORD", auth.check_password(username, "WRONG PASSWORD")
#     )
# )

# secret_key = "super_secret"
# token = auth.login(username, password, secret_key)
# print("jwt: {}".format(token))

# import jwt

# decoded_token = jwt.decode(token, key=secret_key, algorithms=["HS256"])

# print("jwt decoded: {}".format(decoded_token))
