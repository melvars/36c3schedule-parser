import requests
import config

r = requests.get(config.URL)

days = r.json()[""]
print(r.json())