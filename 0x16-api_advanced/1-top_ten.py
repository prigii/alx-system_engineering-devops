#!/usr/bin/python3
""" gives top ten posts on a reddit page"""
import requests


def top_ten(subreddit):
    # Define the Reddit API URL for the given subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid issues
    headers = {'User-Agent': 'MyBot/1.0'}

    try:
        # Send a GET request to the API
        response = requests.get(url, headers=headers)

        # Check if the response is successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract and print the titles of the first 10 hot posts
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            # If the subreddit is invalid or other error occurred, print None
            print(None)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
