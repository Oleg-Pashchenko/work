import requests
import bs4


def scrape(q: str):
    try:
        r = requests.get(f'https://www.oreht.ru/modules.php?name=orehtPriceLS&op=ShowInfo&code={q}')
        soup = bs4.BeautifulSoup(r.text, features='lxml')
        name = soup.find('div', {'class': 'mg-h1text'}).text
        img = soup.find('div', {'class': 'mg-glimage'}).find('img').get('src')
        if name:
            name = name.strip()
        if img:
            img = "https://www.oreht.ru/" + img.strip()
        return name, img
    except:
        return '', ''
