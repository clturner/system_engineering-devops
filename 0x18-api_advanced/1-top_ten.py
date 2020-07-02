#!/usr/bin/python3
import requests
import json


def top_ten(subreddit):
    """
     Queries Reddit API prints titles of the first 10 hot posts for subreddit
    """
    try:
        url = "https://www.reddit.com/r/{}/hot.json?count=10".format(subreddit)
        req = requests.get("{}".format(url), headers={'User-Agent': 'Mozilla'})
        count = 0
        for x in req.json().get('data').get('children'):
            if count < 10:
                count += 1
                if x['data']['title'] is None:
                    print("None")
                else:
                    print(x['data']['title'])
    except:
        print("None")
