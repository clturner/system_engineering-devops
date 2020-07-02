#!/usr/bin/python3
"""
given employee ID, returns information about his/her TODO list progress
"""
import csv
import json
import os
import requests
import sys

if __name__ == "__main__":
    my_list = []
    great_list = []
    count = 0
    id_to_check_for = sys.argv[1]
    req = requests.get('https://jsonplaceholder.typicode.com/users',
                       verify=False)
    req1 = requests.get('https://jsonplaceholder.typicode.com/todos',
                        verify=False)
    json_data = req.json()
    json_data1 = req1.json()
    for x in json_data:
        if id_to_check_for == str(x.get("id")):
            the_username = x.get("username")
    for x in json_data1:
        my_list = []
        if x['userId'] == int(id_to_check_for):
            my_list.append(id_to_check_for)
            my_list.append(the_username)
            my_list.append(x.get('completed'))
            my_list.append(x.get('title'))
            great_list.append(my_list)

    filename = "{}.csv".format(sys.argv[1])
    with open(filename, "w") as output:
        writer = csv.writer(output, delimiter=',', quoting=csv.QUOTE_ALL)
        for x in great_list:
            writer.writerow(x)
