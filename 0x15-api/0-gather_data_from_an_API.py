#!/usr/bin/python3
"""
module that get info about todos of some user
by its id , using an jsonplace hosler api
"""

import requests
import sys
if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user_id)
    url2 = 'https://jsonplaceholder.typicode.com/users?id={}'.format(user_id)
    response = requests.get(url)
    response2 = requests.get(url2)
    todo_data = response.json()
    user_data = response2.json()
    name = user_data[0].get('name')
    comp = 0
    tot = len(todo_data)
    for td in todo_data:
        if td.get('completed'):
            comp += 1
    print('Employee {} is done with tasks({}/{}):'.format(
        name, comp, tot
    ))
    for td in todo_data:
        if td.get('completed'):
            print('\t {}'.format(td.get('title')))
    # print(todo_data)
