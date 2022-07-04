import requests

res = requests.get("http://localhost:5000/data/1")
if res.ok:
    print(res.json())