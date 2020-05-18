import requests
import json
headers={
    'action':'test',
    'path': 'duo'
}

rep=requests.get("http://127.0.0.1:8000",params=headers)

print(rep.json())