#!/usr/bin/python3
"""a recursive Python function that queries the Reddit API and
returns a list containing
the titles of all hot articles for a given subreddit """
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []
    # Base case: if hot_list has 10 or more items, return it
    if len(hot_list) >= 10:
        return hot_list[:10]

    # Define the Reddit API URL for the given subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    # If after is provided, add it to the URL to paginate the results
    if after:
        url += f'&after={after}'

    # Set a custom User-Agent to avoid issues
    headers = {'User-Agent': 'MyBot/1.0'}

    try:
        # Send a GET request to the API
        response = requests.get(url, headers=headers)

        # Check if the response is successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract and append the titles of hot posts to the hot_list
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])

            # Recursively call the function with the next page (after) token
            after = data['data']['after']
            return recurse(subreddit, hot_list, after)
        else:
            # If the subreddit is invalid or other error occurred, return None
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
