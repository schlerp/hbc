# import base64
import json
import requests
from requests.auth import HTTPBasicAuth


BASE_URL = "https://api.brewfather.app/v1"
RECIPE_ENDPOINT = "recipes"
FERM_ENDPOINT = "inventory/fermentables"
HOP_ENDPOINT = "inventory/hops"
MISC_ENDPOINT = "inventory/miscs"
YEAST_ENDPOINT = "inventory/yeasts"

USER_ID = "wMBEMzm6biOMqU8A9cWUtXUbLtb2"
API_KEY = "bfUecM7VFTPpMCb59AXF8N1uj6BANJmOTJEpVtq4KtGpd1J36ZoM4FUmpJlRdMUe"

# AUTH_BASIC = base64.b64encode("{}:{}".format(USER_ID, API_KEY).encode("utf8"))

resp = requests.get(
    "{}/{}".format(BASE_URL, RECIPE_ENDPOINT), auth=HTTPBasicAuth(USER_ID, API_KEY)
)

print(resp)

if resp.status_code == 200:
    print(resp.json())


resp = requests.get(
    "{}/{}/{}".format(BASE_URL, RECIPE_ENDPOINT, "e3U6EIvKRnP5pHZG7NaR0UZ739FFrT"),
    auth=HTTPBasicAuth(USER_ID, API_KEY),
)

if resp.status_code == 200:
    print(json.dumps(resp.json(), indent=2))
