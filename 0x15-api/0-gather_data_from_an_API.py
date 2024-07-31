#!/usr/bin/python3

''' this module intract with a web api to fetch a user TODO list data'''

import requests
from sys import argv


def get_total(user_tasks):
    ''' caluclate the total of tasks completed'''
    total,done = 0,0
    for task in user_tasks:
        total += 1
        if task.get('completed'):
            done += 1
    return total,done

def get_name(user_data):
    ''' get the user name'''
    for data in user_data:
        name =  data.get('name')
        if name:
            return name

def print_done_tasks(user_tasks):
    ''' print completed tasks'''
    for task in user_tasks:
        if task.get('completed'):
            print(f"\t {task.get('title')}")

def main():
    ''' main logic'''
    if len(argv) > 1:
        id = argv[1]
        url_tasks = 'https://jsonplaceholder.typicode.com/todos'
        url_users = 'https://jsonplaceholder.typicode.com/users'
        params = {
            "userId":id
        }

        tasks = requests.get(url_tasks, params=params)
        users = requests.get(url_users, params=params)

        if tasks.status_code == 200 and users.status_code == 200:
            total,done = get_total(tasks.json())
            name = get_name(users.json())
            print(f"Employee {name} is done with tasks({done}/{total}):")
            print_done_tasks(tasks.json())
        else:
            print("erorr")
    else:
        print(f"Usage {argv[0]} user_id")


if __name__ == '__main__':
    main()