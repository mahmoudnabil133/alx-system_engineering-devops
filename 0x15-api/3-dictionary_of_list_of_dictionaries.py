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
    url = 'https://jsonplaceholder.typicode.com/todos'
    url2 = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    response2 = requests.get(url2)
    todo_data = response.json()
    user_data = response2.json()

    all_user_todos = {}
    for user in user_data:
        id = user.get('id')
        username = user.get('username')
        todos_for_user = []
        for td in todo_data:
            if td.get('userId') == id:
                todo_info = {}
                todo_info['task'] = td.get('title')
                todo_info['completed'] = td.get('completed')
                todo_info['username'] = username
                todos_for_user.append(todo_info)
        all_user_todos[id] = todos_for_user



    json_file = 'todo_all_employees.json'
    with open(json_file, 'w') as f:
        json.dump(all_user_todos, f)
