import requests


def getpost(token):
    data = requests.get('https://test-stand.gb.ru/api/posts', params={'owner', 'notMe'},
                        headers={'X-Auth-Token': token})
    return [i['title'] for i in data.json()['data']]


def get_post_description(token):
    data = requests.get('https://test-stand.gb.ru/api/posts', params={},
                        headers={'X-Auth-Token': token})
    return [i['description'] for i in data.json()['data']]


def create_post(token, title, description, content):
    data = requests.post('https://test-stand.gb.ru/api/posts', params={'title': title,
                                                                       'description': description,
                                                                       'content': content},
                         headers={'X-Auth-Token': token})
    return description
