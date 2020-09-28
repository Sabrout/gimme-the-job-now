import requests

""" This script is for testing requests sent to the server. """

url = 'http://localhost:5000/api/predict'

# Request for MyModel by Inarix
r = requests.post(url,json={'x':1.8,})
print(str(r.json()))

# # Request for ModelExample by Me 
r = requests.post(url,json={'x':4,})
print(str(r.json()))