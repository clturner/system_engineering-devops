#!/usr/bin/python3
"""
given employee ID, returns information about his/her TODO list progress
"""
import sys
import os
import requests
import json

if __name__ == "__main__":

    all_users = requests.get('https://jsonplaceholder.typicode.com/users',\
                             verify=False).json()

    all_todos = requests.get('https://jsonplaceholder.typicode.com/todos',\
                             verify=False).json()

    finished_dict = {}
    my_list = []

    for x in all_todos:
        my_dict = {}
        my_dict["task"] = x.get("title")
        my_dict["completed"] = x.get("completed")
        var = x.get("userId")
        my_dict["username"] = all_users[int(var)-1]['username']
        my_list.append(my_dict)
    finished_dict[var]= my_list
    print(finished_dict)

    with open(filename, 'w') as file:
        json.dump({var: my_list}, file)
