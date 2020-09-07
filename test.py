import requests

BASE = 'http://127.0.0.1:5000/'
response = requests.get(BASE + "hello-world/ajas/21")
print(response.json())
