# crud - create read update and delete (HTTP common requests)
import json
import requests
# res = requests.get('https://google.com')
# if res.ok:
#     print(res.content)
#

# #converting string to dictrionary using loads
# x = '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)     ### will convert string to dictionary
# print(y["age"])

API_KEY = "jMh9t9Regon6NpGiSRSGDFNQCIkt1My1"

url = "https://api.apilayer.com/exchangerates_data/convert?to=ILS&from=USD&amount=1"

payload = {}
headers= {
  "apikey": API_KEY
}

response = requests.request("GET", url, headers=headers, data = payload)
data = response.json()
results = data['result']
print(results)
print(data)



