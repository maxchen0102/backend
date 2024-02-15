import requests
response = requests.get("http://localhost:3001/api/get_test")
list=response.json()
#print(response.json())
print(list[0])
print(type(list[0]))
print(list[0]["name"])