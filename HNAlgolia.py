import requests

def default_news():
    url = "https://hn.algolia.com/api/v1/search"

    querystring = {"tags":"story"}

    payload = ""
    response = requests.request("GET", url, data=payload, params=querystring)

    return response
