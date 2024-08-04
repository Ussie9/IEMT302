from bs4 import BeautifulSoup
import requests


website = 'https://cloudykitchen.com/'
response = requests.get(website)
content = response.text

soup = BeautifulSoup(content,'lxml')
print(soup.prettify())
