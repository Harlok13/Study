from pprint import pprint

import requests
from librarys_modules.pytest_.configuration import SERVICE_URL

def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    print()
    print(response.json( ))

