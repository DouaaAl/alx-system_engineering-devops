#!/usr/bin/python3
"""
A script to fetch the number of subscribers for a given subreddit using the Reddit API.
"""

from requests import get


def number_of_subscribers(subreddit):
    """Function to get the subscriber count from a subreddit."""
    if subreddit and isinstance(subreddit, str):
        subscribers = 0
        url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
        headers = {'User-Agent': 'my-app/0.0.1'}
        req = get(url, headers=headers)
        if req.status_code == 200:
            data = req.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
