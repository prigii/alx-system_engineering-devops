#!/bin/usr/python3
""" Imports number of subs from a reddit page """
import requests


def number_of_subscribers(subreddit):
    # Define the Reddit API URL for the given subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid issues
    headers = {'User-Agent': 'MyBot/1.0'}

    try:
        # Send a GET request to the API
        response = requests.get(url, headers=headers)

        # Check if the response is successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract the number of subscribers
            subscribers = data['data']['subscribers']

            return subscribers
        else:
            # If the subreddit is invalid or other error occurred, return 0
            return 0
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0
