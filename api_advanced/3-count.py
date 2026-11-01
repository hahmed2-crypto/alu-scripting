#!/usr/bin/python3
"""
Module that queries the Reddit API recursively, parses hot article titles,
and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively queries the Reddit API, counts occurrences of case-insensitive
    keywords found in titles, and prints results in descending order.
    """
    if not counts:
        for word in word_list:
            counts[word.lower()] = 0

    url = "https://reddit.com{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0.0 (by /u/tim_britton)"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        after = data.get("after")
        children = data.get("children", [])

        for post in children:
            title = post.get("data", {}).get("title", "").lower()
            # Split title into structural words cleanly
            words = title.split()
            for word in words:
                # Clean punctuation trailing/leading from standard boundaries
                cleaned = word.strip('.,?!_""()[]{}')
                if cleaned in counts:
                    counts[cleaned] += 1

        if after is not None:
            return count_words(subreddit, word_list, after, counts)

        # Sort: Descending by count value, then alphabetically ascending by key
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))

    except Exception:
        return
