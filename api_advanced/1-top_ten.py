#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    Prints None if the subreddit is invalid or an error occurs.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0.0 (by /u/tim_britton)"}
    # Pass limit inside the parameters dictionary explicitly
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children = data.get("data", {}).get("children", [])
            
            if not children:
                print("None")
                return

            for post in children:
                print(post.get("data", {}).get("title"))
        else:
            print("None")
    except Exception:
        print("None")
