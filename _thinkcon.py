import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from datetime import datetime

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

    if tag == "기획" or tag == "아이디어": n=2
    elif tag == "과학" or tag == "공학": n=11
    elif tag == "게임" or tag =="소프트웨어": n=12
    else:
        return "태그 오류"

    url = "https://www.thinkcontest.com/Contest/CateField.html?c={}".format(n)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    contlist = soup.find("ul", attrs = {"class" : "contest-banner-list"}).find_all("li")
    now = datetime.now()

    i = 1
    for li in contlist:
        try:
            browser.get(url)
            
            due = browser.find_element(by = By.XPATH, value = "//*[@id='main']/div/div[2]/ul[2]/li[{}]/div/p[1]".format(i)).text
            month, day = int(due[18:20]), int(due[21:23])
            deadline = datetime(2022, month, day)
            due = deadline - now
            due = "D-" + str(due.days)

            elem = browser.find_element(by = By.XPATH, value = "//*[@id='main']/div/div[2]/ul[2]/li[{}]/a/h4".format(i))
            elem.click()

            soup = BeautifulSoup(browser.page_source, "lxml")
            
            title = soup.find("span", attrs = {"class" : "title"}).get_text()
            try:
                link = soup.find("a", attrs = {"class" : "linker"})['href']
            except TypeError:
                link = "링크 없음"
            
            data = {
                "title" : title,
                "due" : due,
                "link" : link,
            }

            list.append(data)
            # print(data)

            i += 1            

        except:
            pass
    
    # print(list)
    # print(len(list))
    return list

def cycle():
    list = crawl("아이디어")
    for data in list:
        try:
            IdeaData(title = data['title'], due = data['due'], link = data['link']).save()
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

    print("크롤링 완료")

if __name__ == '__main__':
    cycle()
    print("크롤링 완료")