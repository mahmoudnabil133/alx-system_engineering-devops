#!/usr/bin/env python3
"apis"
import requests
import json
if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    res = requests.get(url)
    data = res.json()
    # name = data.get('name')
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
    
