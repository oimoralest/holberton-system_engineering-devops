#!/usr/bin/python3
"""This script, using a REST API, for a given employee ID, returns information
about his/her TODO list progress
"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    userInfo = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + argv[1]).json()
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]).json()
    with open('{}.csv'.format(argv[1]), mode='w') as employeeFile:
        writer = csv.writer(
            employeeFile, delimiter=',', quotechar='"',
            quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow(
                [userInfo.get('id'), userInfo.get('name'),
                 task.get('completed'), task.get('title')])
