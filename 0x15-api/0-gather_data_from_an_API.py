#!/usr/bin/python3
"""This script, using a REST API, for a given employee ID, returns information
about his/her TODO list progress
"""
import requests
from sys import argv


if __name__ == '__main__':
    userInfo = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + argv[1]).json()
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]).json()
    completedTasks = [
        task.get('title') for task in tasks if task.get('completed')]
    print(
        'Employee {} is done with tasks({}/{}):'.format(
            userInfo.get('name'), len(completedTasks), len(tasks)
        ))
    for task in completedTasks:
        print('\t {}'.format(
            task
        ))
