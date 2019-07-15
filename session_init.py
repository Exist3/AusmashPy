import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get("API_KEY")


class APIKeyMissingError(Exception):
    pass


if API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. See "
        "https://ausmash.com.au/api "
        "for how to retrieve an authentication token from "
        "Ausmash"
    )

session = requests.Session()
session.headers = {}
session.headers['X-ApiKey'] = API_KEY
