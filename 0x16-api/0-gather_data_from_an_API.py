#!/usr/bin/python3
"""
given employee ID, returns information about his/her TODO list progress
"""
import json
import os
import sys
import requests


if __name__ == "__main__":

    count = 0
    id_to_check_for = sys.argv[1]
    """
    req to get name matching user id , given by sys.argv[1]
    """
    req = requests.get('https://jsonplaceholder.typicode.com/users',
                       verify=False).json()
    for x in range(len(req)):
        if int(id_to_check_for) == req[x]['id']:
            the_name = req[x]['name']

    """
    req to get completed tasks #  and task names of completed tasks
    """
    my_list = []
    req1 = requests.get('https://jsonplaceholder.typicode.com/todos',
                        verify=False).json()
    for x in range(len(req1)):
        if (req1[x]['userId'] == int(id_to_check_for) and
            req1[x]['completed'] is True):
            my_list.append(req1[x]['title'])
            count += 1

    print("Employee {} is done with tasks ({}/20):".format(the_name, count))
    for thing in my_list:
        print("\t {}".format(thing))
