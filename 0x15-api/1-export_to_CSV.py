#!/usr/bin/python3
"""
module that get info about todos of some user
by its id , using an jsonplace hosler api
"""
import csv
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
    user_todos = []
    for td in todo_data:
        td_data = [user_id, name]
        td_data.append(td.get('completed'))
        td_data.append(td.get('title'))
        user_todos.append(td_data)

    csv_file = '{}.csv'.format(user_id)
    with open(csv_file, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(user_todos)
