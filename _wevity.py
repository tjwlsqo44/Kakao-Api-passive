import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "kapi.settings")
django.setup()
from crawling.models import IdeaData, WebData, EngineeringData, SwData

option = webdriver.ChromeOptions()
option.add_argument("headless")
option.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=option)

def crawl(tag):
    list = []

    if tag == "기획" or tag == "아이디어": n=1
    elif tag == "웹" or tag == "모바일" or tag == "IT": n=20
    elif tag == "게임" or tag =="소프트웨어": n=21
    elif tag == "과학" or tag == "공학": n=22
    else:
        return "태그 오류"

    for i in range(5):
        url = "https://www.wevity.com/?c=find&s=1&mode=ing&gub=1&cidx={}&gp={}".format(n, i+1)
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        browser.get(url)

        titles = soup.find_all("div", attrs = {"class" : "tit"})
        days = soup.find_all("div", attrs = {"class" : "day"})
        
        cnt = 0
        
        for t, d in zip(titles, days):
            cnt += 1
            if cnt == 1:  continue
            
            try:
                t.find('span').decompose()
                title = t.find("a").get_text().strip()
            except AttributeError:
                title = t.find("a").get_text().strip()

            d.find('span').decompose()
            due = d.get_text().strip()
            
            browser.get(url)
            elem = browser.find_element(by = By.XPATH ,value = "//*[@id='container']/div[2]/div[1]/div[2]/div[3]/div/ul/li[{}]/div[1]/a".format(cnt))
            elem.click()
            
            try:
                link = browser.find_element(by = By.XPATH, value = "//*[@id='container']/div[2]/div[1]/div[2]/div/div[2]/div[2]/ul/li[8]/a").text
            except:
                link = "링크 없음"
            
            data = {
                "title" : title,
                "due" : due,
                "link" : link,
            }

            list.append(data)
            # print(data)

    # print(list)
    # print(len(list))
    
    return list

if __name__ == '__main__':
    list = crawl("아이디어")
    for data in list:
        try:
            IdeaData(title = data['title'], due = data['due'], link = data['link']).save()
        except django.db.utils.IntegrityError:
            pass

    list = crawl("웹")
    for data in list:
        try:
            WebData(title = data['title'], due = data['due'], link = data['link']).save()
        except django.db.utils.IntegrityError:
            pass

    list = crawl("공학")
    for data in list:
        try:
            EngineeringData(title = data['title'], due = data['due'], link = data['link']).save()
        except django.db.utils.IntegrityError:
            pass

    list = crawl("소프트웨어")
    for data in list:
        try:
            SwData(title = data['title'], due = data['due'], link = data['link']).save()
        except django.db.utils.IntegrityError:
            pass