import time

from selenium import webdriver
from bs4 import BeautifulSoup


def scrape(q: str):
    try:
        result_id = []
        result_photo = []
        browser = webdriver.Chrome('chromedriver')
        browser.get(f'https://www.ozon.ru/search/?text={q}&from_global=true')
        data = BeautifulSoup(browser.page_source, features='lxml')
        browser.close()
        data = data.find_all('div', {'class': 'k8z kz9'})
        for i in data:
            result_id.append(i.find('img').get('src').split('/')[-1].split('.')[0])
            result_photo.append(i.find('img').get('src'))
        return result_id, result_photo
    except:
        return [], []

