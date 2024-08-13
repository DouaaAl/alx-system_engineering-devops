#!/usr/bin/python3

"""
Script that returns all subscribers of a subreddit
"""


import requests

def number_of_subscribers(subreddit):
	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	headers = {
		 'User-Agent': 'Mozilla/5.0'
		}
	response = requests.get(url, headers=headers, allows_redirects=False)

	if (response.status_code == 200):
		data = response.json()
		subscribers = data['data']['subscribers']
		return subscribers
	else:
		return 0
