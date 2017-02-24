#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://ritetag.com/hashtag-search'

r = requests.get(url)

html_content = r.text

soup = BeautifulSoup(html_content, 'lxml')


def woo():
    for div in soup.findAll('table', attrs={'class': 'table'}):
        return div.find('a').contents[0]

print woo()
