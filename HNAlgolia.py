import requests

def default_news():
    url = "https://hn.algolia.com/api/v1/search"

    querystring = {"tags":"story","hitsPerPage":"50"}

    payload = ""
    response = requests.request("GET", url, data=payload, params=querystring)

    return response

def get_news(id):

    url = f'http://hn.algolia.com/api/v1/items/{id}'

    payload = ""
    response = requests.request("GET", url, data=payload)

    return response

def search_news(keywords,by_radio): #for_radio
    '''
    if timestamp is 'all-time':
        pass
    '''
    if by_radio == 'date':
        by='search_by_date'
    else:
        by='search'

    #print(f'Keywords: {keywords} | By: {by_radio} -> {by}')

    url = f'http://hn.algolia.com/api/v1/{by}'
    querystring = {"query":keywords,"tags":"story","hitsPerPage":"100"}
    
    payload = ""
    response = requests.request("GET", url, data=payload, params=querystring)

    return response
