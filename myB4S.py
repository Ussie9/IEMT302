#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests


if __name__ == '__main__':
    website = 'https://cloudykitchen.com/'
    response = requests.get(website)
    content = response.text
    
    soup = BeautifulSoup(content,'lxml')
    print(soup.prettify())
