from pprint import pprint
from time import sleep

import requests
from bs4 import BeautifulSoup
from random import randint

#открываем файл с урлами
with open('urls.txt', 'r') as f:
    urls = [line.strip() for line in f]

result_file = open('results.txt', 'a')

#ищем содержание дивов с классом listing__title и записываем это в файл
for item in urls:
    resp = requests.get(item)
    soup = BeautifulSoup(resp.text, features="lxml")
    offer = soup.find('div', {'class': 'listing__title'}).text.strip().split(' ')
    result_file.write(f'{item} — {offer[1]}\n')
    random_timeout = randint(5, 10)
    sleep(random_timeout)

pprint('All!')
