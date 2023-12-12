import requests
import json
from bs4 import BeautifulSoup

url="https://tengrinews.kz/news/"

responce=requests.get(url)
soup = BeautifulSoup(responce.text, 'lxml')

zagolovki = soup.find_all('span',class_="tn-hidden")
links_of_news= soup.find_all('a', class_="tn-link")

# for i in range(len(links_of_news)):
#     if links_of_news[i]:
#         print(zagolovki[i].text)

for i in links_of_news:
    print(i.text)
    
# for zagolovok in zagolovki:
#     print(f"{zagolovok.text}\n")
