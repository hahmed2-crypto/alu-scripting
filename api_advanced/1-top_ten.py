#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    Prints None if the subreddit is invalid.
    """
    url = "https://reddit.com{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0.0 (by /u/tim_britton)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get("data", {}).get("children", [])
            for post in children:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
    except Exception:
        print(None)
