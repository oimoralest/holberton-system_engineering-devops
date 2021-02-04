#!/usr/bin/python3
"""This script defines two functions to get all the hot articles for a given
subreddit
"""
import requests
headers = {'User-Agent': 'Godfather'}


def append_to_list(hot_list, data):
    """Appends the titles of the article in hot_list

    Args:
        hot_list ([list]): hot_list
        data ([dict]): data to append
    """
    for topic in data:
        hot_list.append(topic.get('data').get('title'))


def recurse(subreddit, hot_list=[], after='null'):
    """Recursively makes request for a subreddit

    Args:
        subreddit ([str]): subreddit to get
        hot_list (list, optional): hot_list. Defaults to [].
        after (str, optional): after parameter. Defaults to 'null'.

    Returns:
        [list]: list with all the hot articles for a given subreddit
    """
    if after is None:
        return hot_list
    else:
        try:
            data = requests.get(
                'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'.format(
                    subreddit, after), headers=headers).json().get('data')
            after = data.get('after')
            append_to_list(hot_list, data.get('children'))
            recurse(subreddit, hot_list, after)
            return hot_list
        except:
            return None
