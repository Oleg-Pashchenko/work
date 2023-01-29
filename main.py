from scrapers import widberries, oreht, ozon
import db


def main():
    print('Execution started!')
    while True:
        words_count = int(open('dependencies/count', 'r').read())
        data = db.get_new_article()
        print(data)
        id, article = data[0], data[1]
        oreht_name, oreht_image = oreht.scrape(article)
        id_ozon, photo_ozon, ozon_names = ozon.scrape(oreht_name, words_count)
        id_wildberries, photo_wildberries, wildberries_names = widberries.scrape(oreht_name, words_count)
        print(article, oreht_name, oreht_image, 'ozon', id_ozon, photo_ozon, 'parsed', ozon_names)
        db.write_row(article, oreht_name, oreht_image, 'ozon', id_ozon, photo_ozon, 'parsed', ozon_names)
        db.write_row(article, oreht_name, oreht_image, 'wildberries', id_wildberries, photo_wildberries, 'parsed', wildberries_names)
        db.delete_row_by_id(id)


if __name__ == '__main__':
    main()
