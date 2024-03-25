#!/usr/bin/env python3
"apis"
import requests
import json
import csv
if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    res = requests.get(url)
    data = res.json()
    # name = data.get('name')
    # with open('data.json', 'r') as f:
    #     json.dump(data, f, indent=4)

    # with open('data.json', 'r') as f:
    #     data = json.load(f)
    #     print(data)

    with open('data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(data[0].keys())
        for user in data:
            writer.writerow(user.values())
