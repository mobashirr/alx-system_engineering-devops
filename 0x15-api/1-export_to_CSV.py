#!/usr/bin/python3

''' this module intract with a web api to fetch a user TODO list data'''

import requests
from sys import argv
import csv


def get_total(user_tasks):
    ''' caluclate the total of tasks completed'''
    total,  done = 0,   0
    for task in user_tasks:
        total += 1
        if task.get('completed'):
            done += 1
    return total,   done


def get_name(user_data):
    ''' get the user name'''
    for data in user_data:
        name = data.get('name')
        if name:
            return name


def export_to_csv(user_id, user, todos):
    if not user or not todos:
        return

    username = get_name(user)
    file_name = f"{user_id}.csv"
    
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username, task['completed'], task['title']])
    
    print(f"Data exported to {file_name}")

def main():

    ''' main logic'''
    if len(argv) > 1:

        id = argv[1]
        url_tasks = 'https://jsonplaceholder.typicode.com/todos'
        url_users = 'https://jsonplaceholder.typicode.com/users'
        params_tasks = {"userId": id}
        params_users = {"id": id}
        tasks = requests.get(url_tasks, params=params_tasks)
        user = requests.get(url_users, params=params_users)

        if tasks.status_code == 200 and user.status_code == 200:
            total, done = get_total(tasks.json())
            name = get_name(user.json())
            print(f"Employee {name} is done with tasks({done}/{total}):")
            export_to_csv(user_id=id, user=user.json(), todos=tasks.json())

        else:
            print("erorr")
    else:
        print(f"Usage {argv[0]} user_id")


if __name__ == '__main__':
    main()
