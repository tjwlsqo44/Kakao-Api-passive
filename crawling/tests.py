from django.test import TestCase

# Create your tests here.
import requests
from bs4 import BeautifulSoup
from datetime import date

list = []
url = "http://spartan.ssu.ac.kr/board/board_list?code=notice"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
now = date.today()

body = soup.find("tbody")
rows = body.find_all("tr")

for row in rows:
    row.find('td').decompose()
    row.find('td', attrs = {'class' : 'm_non'}).decompose()
    post_month = int(row.find('td', attrs = {'class' : 'm_non'}).get_text()[5:7])

    if now.month-post_month > 1 :
        break

    title = row.find("a").get_text()
    link = row.find("a")['href']
    
    data = {
        "title" : title,
        "link" : "http://spartan.ssu.ac.kr/" + link,
    }
    
    print(data)
    list.append(data)
