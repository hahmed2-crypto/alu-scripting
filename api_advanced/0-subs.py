#!/usr/bin/python3
"""
Module to query the Reddit API and find the number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the total number of subscribers
    for a given subreddit. If the subreddit is invalid, returns 0.
    """
    url = "https://reddit.com{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0.0 (by /u/tim_britton)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        return 0
    except Exception:
        return 0
