from urllib.parse import urlencode
import requests
import json
from pprint import pprint

API_URL = 'https://api.vk.com/method/'
API_VERSION = '5.80'
TOKEN = '3b09c897a3f09521cdcbdbbe6d7ea2e56743be8541865dbab8fc33e06de432eb213dda4d56735bcbb632c'
APP_ID = 6612494
AUTH_URL = 'https://oauth.vk.com/authorize'
auth_params = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': API_VERSION
}
METHOD = 'friends.getMutual'
response = requests.get('?'.join((AUTH_URL, urlencode(auth_params))))
print('?'.join((AUTH_URL, urlencode(auth_params))))


def make_request_url(param):
    return f'{API_URL}/{METHOD}?{urlencode(param)}'


def find_mutual_friends(first_id, second_id):
    param = {
        'target_uid': first_id,
        'source_uid': second_id,
        'access_token': TOKEN,
        'v': API_VERSION
    }

    request_url = make_request_url(param)
    friends_response = requests.get(request_url).text

    return json.loads(friends_response)['response']


def friends_links(id):
    return f'https://vk.com/id{id}'


def mutual_friends_list(id_list):

    mutual_friends_list = list()
    for id in id_list:
        mutual_friends_list.append(friends_links(id))

    return mutual_friends_list


first_id = int(input('Введите id первого пользователя:'))
second_id = int(input('Введите id второго пользователя:'))

mutual_friends = find_mutual_friends(first_id, second_id)
mutual_friends_list = mutual_friends_list(mutual_friends)

print(f'У пользователей с id{first_id} и id{second_id } найдено {len(mutual_friends_list)} общих друзей')
pprint(mutual_friends_list)
