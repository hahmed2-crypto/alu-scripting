#!/usr/bin/python3
"""
Module that queries the Reddit API recursively to return a list containing
the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    """
    url = "https://reddit.com{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0.0 (by /u/tim_britton)"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        after = data.get("after")
        children = data.get("children", [])

        for post in children:
            hot_list.append(post.get("data", {}).get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after)

        return hot_list
    except Exception:
        return None
