import requests
from bs4 import BeautifulSoup

getpage= requests.get('http://127.0.0.1:8000/prop/home/')

getpage_soup= BeautifulSoup(getpage.text, 'html.parser')

all_class_topsection= getpage_soup.findAll('p', {'class':'topsection'})

for para in all_class_topsection:
    print (para)