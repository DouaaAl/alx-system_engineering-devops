#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
	"""Returns the number of total subscribers"""
	url = "https://api.reddit.com/r/{}/about.json".format(subreddit)
	headers = {'User-Agent': 'Mozilla/5.0'}
	response = requests.get(url, headers=headers, allow_redirects=False)

	if response.status_code != 200:
        	return 0

	try:
		response_data = response.json()
		return response_data.get('data', {}).get('subscribers', 0)
	except ValueError:
		print("Failed to parse JSON.")
		return 0
