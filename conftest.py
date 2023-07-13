import pytest
import requests
import yaml

with open("logpass.yaml") as f:
    data = yaml.safe_load(f)

name = data['user']
passwd = data['pass']
addr = data['addr']


@pytest.fixture()
def login():
    r = requests.post(addr, data={'username': name, 'password': passwd})
    return r.json()['token']


@pytest.fixture()
def text1():
    return "Здесь могла быть ваша реклама"


@pytest.fixture()
def text2():
    return "Проклятие монахини"


