#!/usr/bin/python3
"""This script records all tasks from all employees in a json file
"""
import json
import requests


if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todoDictionary = {}
    for user in users:
        tasks = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId=' +
            str(user.get('id'))).json()
        tasks = [
            {'username': user.get('username'), 'task': task.get('title'),
             'completed': task.get('completed')} for task in tasks]
        todoDictionary.update({user.get('id'): tasks})
    with open('todo_all_employees.json', mode='w') as employeeFile:
        json.dump(todoDictionary, employeeFile, indent=4)
