import time

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


def scrape(q: str):
    if len(q.split()) > 3:
        q = ' '.join(q.split()[:3])
    try:
        result_id = []
        result_photo = []
        options = Options()
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        browser = webdriver.Chrome('chromedriver', options=options)
        browser.get(f'https://www.ozon.ru/search/?text={q}&from_global=true')
        data = BeautifulSoup(browser.page_source, features='lxml')
        browser.close()
        data = data.find_all('div', {'class': 'k8z kz9'})
        for i in data:
            result_id.append(i.find('img').get('src').split('/')[-1].split('.')[0])
            result_photo.append(i.find('img').get('src'))
        return result_id, result_photo
    except Exception as e:
        print(e)
        return [], []
