import requests
import json

headers = {
    'action': 'test',
    'path': 'Shivani_Jhinkwan__99999'
}

h = {
    'action': 'download',
    'path': 'test'
}


rep = requests.get("http://127.0.0.1:8000", params=headers)

print(rep.json())
