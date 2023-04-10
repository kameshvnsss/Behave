# import requests module
import requests
import json

# Making a get request
data = {"name": "kamesh", "job": "test"}
response = requests.post('https://reqres.in/api/users/', json=data)

# print response
print(response)
print(response.content)
user_details = json.loads(response.content)
print(user_details['name'])

# print request status_code
print(response.status_code)
