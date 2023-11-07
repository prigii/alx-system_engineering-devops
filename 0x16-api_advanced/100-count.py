#!/usr/bin/python3
""" recursive fxn that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords"""
import requests


def count_words(subreddit, word_list, after=None, word_counts=None):
    # Base case: if no more keywords to count, return
    if not word_list:
        return

    # Initialize the word_counts dictionary on the first call
    if word_counts is None:
        word_counts = {}

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

            # Extract and count the occurrences of keywords in hot post titles
            for post in data['data']['children']:
                title = post['data']['title'].lower()
                for keyword in word_list:
                    if title.count(keyword) > 0:
                        if keyword in word_counts:
                            word_counts[keyword] += title.count(keyword)
                        else:
                            word_counts[keyword] = title.count(keyword)

            # Recursively call the function with the next page (after) token
            after = data['data']['after']
            count_words(subreddit, word_list, after, word_counts)
        else:
            # If the subreddit is invalid or other error occurred, return
            return
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return

    # Sort and print the word counts in descending order by count,
    # and then alphabetically by keyword
    for keyword, count in sorted(word_counts.items(),
                                 key=lambda x: (-x[1], x[0])):
        print(f"{keyword}: {count}")
