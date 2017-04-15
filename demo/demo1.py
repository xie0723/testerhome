# -*- coding: utf-8 -*-
import re

__Author__ = "xiewm"
__Date__ = '2017/3/8 15:47'

import requests
from bs4 import BeautifulSoup

html = requests.get('https://testerhome.com/xie_0723/favorites').text

soup = BeautifulSoup(html, 'html.parser')

# print(soup.find_all(text))
for tag in soup.find_all('td', {'class': 'title'}):
    if tag.a:
        print(tag.a.get_text(), tag.a['href'])
    else:
        pass

    # print(tag.a)

# print(soup.find_all('a', herf=re.compile("/topics/6911")))
# print(soup.select('a[href="/topics/6911"]'))
