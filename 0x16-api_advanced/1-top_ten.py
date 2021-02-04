#!/usr/bin/python3
"""This script defines the top_ten function
"""


def top_ten(subreddit):
    """Prints the top 10 hot posts for a given subreddit

    Args:
        subreddit ([str]): subreddit to get
    """
    import requests
    headers = {'User-Agent': 'Godfather'}
    try:
        data = requests.get(
            'https://www.reddit.com/r/{}/hot.json'.format(
                subreddit), headers=headers).json().get('data').get('children')
        for i in range(10):
            print(data[i].get('data').get('title'))
    except:
        print(None)
