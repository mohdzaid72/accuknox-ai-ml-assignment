import requests

url = "https://openlibrary.org/search.json?q=the+lord+of+the+rings&limit=5"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(data)