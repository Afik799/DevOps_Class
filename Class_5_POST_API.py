import requests

res = requests.post("http://localhost:5000/data/1", json={"user_name": "Afik"})
if res.ok:
    print(res.json)