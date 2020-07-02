#!/usr/bin/python3
"""
given employee ID, returns information about his/her TODO list progress
"""
import json
import os
import requests
import sys


if __name__ == "__main__":

    id_to_check_for = sys.argv[1]
    req1 = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(id_to_check_for), verify=False).json()
    username = req1.get('username')
    req2 = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(id_to_check_for), verify=False).json()

    filename = "{}.json".format(id_to_check_for)
    finished_dict = {}
    my_list = []
    for x in req2:
        my_dict = {}
        my_dict["task"] = x.get("title")
        my_dict["completed"] = x.get("completed")
        my_dict["username"] = username
        my_list.append(my_dict)

    finished_dict = {id_to_check_for: my_list}

    with open(filename, 'w') as file:
        json.dump({id_to_check_for: my_list}, file)
