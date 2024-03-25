#!/usr/bin/env python3
"apis"
import requests
import json
import csv

import pandas as pd

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

    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(data[0].keys())
        for user in data:
            writer.writerow(user.values())
    
    # data = pd.read_csv('data.csv')
    # print(data)

    # with open('data.csv', 'r') as f:
    #     reader = csv.reader(f)
    #     for r in reader:
    #         print(r)
