#!/usr/bin/python3
"""This script defines the function count_words
"""
import re
import requests
headers = {'User-Agent': 'Godfather'}


def count_words(subreddit, word_list, after='null'):
    """recursive function that queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces. Javascript should count as
    javascript, but java should not)

    Args:
        subreddit ([str]): subreddit to get
        word_list ([dict]): word list to find in every title
        after (str, optional): after parameter. Defaults to 'null'.
    """
    if after is 'null':
        word_list = list(map(lambda word: word.lower(), word_list))
        word_list.sort()
        word_list = {key: 0 for key in word_list}
    if after is None:
        for key, value in word_list.items():
            if value:
                print('{}: {}'.format(key, value))
    else:
        try:
            data = requests.get(
                'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'
                .format(
                    subreddit, after), headers=headers).json().get('data')
            after = data.get('after')
            for topic in data.get('children'):
                title = topic.get('data').get('title')
                for word in word_list:
                    find = re.findall(r'\b{}\b'.format(word), title, re.I)
                    if re.findall(r'\b{}\b'.format(word), title, re.I):
                        word_list[word] += len(find)
            count_words(subreddit, word_list, after)
        except:
            print()
