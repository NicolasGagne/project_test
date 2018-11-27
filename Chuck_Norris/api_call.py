"""
File interger all the call to the Apis
"""


import requests
import json
def get_categorie(url):
    """
    :param url: the url to make the request
    :return: List of categorie form the url.
    """

    categorie = requests.get(url).content.decode("utf-8")

    return json.loads(categorie)


def get_quote(url, cat = None):
    """
    :param url: the base url for the API
    :param cat: Category of the quote requested.
    :return: Dict of the responce form the API
    """
    if cat == None:
        responce = requests.get(url).content
    else:
        payload = {"category": cat}
        responce = requests.get(url, params=payload).content

    return json.loads(responce)