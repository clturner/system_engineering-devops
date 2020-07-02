#!/usr/bin/python3
"""
recursive function queries Reddit API returns list of titles of all hot
articles for a given subreddit
"""
import requests
import sys
import json


def recurse(subreddit, hot_list=[]):

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get("{}".format(url), headers={'User-Agent': 'Mozilla'})
    for x in req.json().get('data').get('children'):
        hot_list.append(x['data']['title'])
    print(len(hot_list))
    if x['data']['title'] is None:
        return (len(hot_list))
    return recurse(subreddit, hot_list[1:])
