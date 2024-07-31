#!/usr/bin/python3

'''intract with web api and save data to json file'''

import json
import requests


def get_key(data, column):
    '''takes a dict and returns the desired key'''
    return data.get(column, None)


def tasks_to_dict(user, todos):
    '''return strucured array of dict for user tasks '''
    if not user or not todos:
        return

    # Assuming user is a dictionary
    username = get_key(user, "username")
    result = []

    for task in todos:
        '''collect all tasks in one array'''
        result.append(
            {
                "username": username,
                "task": get_key(task, "title"),
                "completed": get_key(task, "completed"),
            }
        )
    return result


def export_to_json(file_content):
    '''export data to json file'''
    file_name = "todo_all_employees.json"
    content = json.dumps(file_content, indent=4)
    with open(file_name, 'w') as file:
        file.write(content)


def main():
    ''' main logic'''
    url_tasks = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(url_users)

    if users.status_code == 200:
        content = {}
        for user in users.json():
            id = user.get('id')
            params = {"userId": id}
            tasks = requests.get(url_tasks, params)
            content.update({
                str(id): tasks_to_dict(user, tasks.json())
                })

        export_to_json(content)


if __name__ == "__main__":
    main()
