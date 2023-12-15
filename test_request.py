import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)

print(response.json())
