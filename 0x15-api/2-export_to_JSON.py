#!/usr/bin/env python3


import json
import requests
import sys

def get_key(data, column):
    '''takes a dict and returns the desired key'''
    return data.get(column, None)

def export_to_json(user_id, user, todos):
    if not user or not todos:
        return

    username = get_key(user[0], "username")  # Assuming user is a list with one dictionary
    file_name = f"{user_id}.json"
    file_content = {str(user_id): []}

    for task in todos:
        '''collect all tasks in one array'''
        file_content[str(user_id)].append(
            {"task": get_key(task, "title"), "completed": get_key(task, "completed"), "username": username}
        )

    content = json.dumps(file_content, indent=4)
    with open(file_name, 'w') as file:
        file.write(content)

def main():
    ''' main logic'''
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        url_tasks = 'https://jsonplaceholder.typicode.com/todos'
        url_users = 'https://jsonplaceholder.typicode.com/users'
        params_tasks = {"userId": user_id}
        params_users = {"id": user_id}
        tasks = requests.get(url_tasks, params=params_tasks)
        user = requests.get(url_users, params=params_users)

        if tasks.status_code == 200 and user.status_code == 200:
            name = get_key(user.json()[0], "name")
            total = len(tasks.json())
            done = len([task for task in tasks.json() if task["completed"]])
            # print(f"Employee {name} is done with tasks({done}/{total}):")
            export_to_json(user_id=user_id, user=user.json(), todos=tasks.json())

if __name__ == "__main__":
    main()
