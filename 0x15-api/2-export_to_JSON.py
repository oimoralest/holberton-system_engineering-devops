#!/usr/bin/python3
"""This script, using a REST API, for a given employee ID, returns information
about his/her TODO list progress
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    userInfo = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + argv[1]).json()
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]).json()
    tasksDictList = [
        {'task': task.get('title'), 'completed': task.get('completed'),
         'username': userInfo.get('username')} for task in tasks]
    with open('{}.json'.format(argv[1]), mode='w') as employeeFile:
        json.dump(
            {tasks[0].get('userId'): tasksDictList}, employeeFile, indent=4)
