#!/usr/bin/python3
"""
module that get info about todos of some user
by its id , using an jsonplace hosler api
"""
import csv
import json
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
    name = user_data[0].get('username')

    tasks_dec = {}
    todos_list = []
    for td in todo_data:
        todo_info = {}
        todo_info['task'] = td.get('title')
        todo_info['completed'] = td.get('completed')
        todo_info['username'] = name
        todos_list.append(todo_info)
    tasks_dec[user_id] = todos_list

    json_file = '{}.json'.format(user_id)
    with open(json_file, 'w') as f:
        json.dump(tasks_dec, f)
