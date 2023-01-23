import json

import excel
import oreht
import ozon
import widberries


def main():
    print("Started!")
    filename = 'Копия Прайслист.xlsx'
    ids = excel.read_file(filename)
    result = []  # recht photo, articul, recht_name, photo_wb, articul_wb, photo_ozon, id_ozon
    a = 0
    print(f'{len(ids)} data loaded!')
    for q in ids:
        a += 1
        q = q.split('-')[1]
        try:
            oreht_name, oreht_image = oreht.scrape(q)
        except:
            oreht_name, oreht_image = [], []
        try:
            id_ozon, photo_ozon = ozon.scrape(oreht_name)
        except:
            id_ozon, photo_ozon = [], []
        try:
            id_wildberries, photo_wildberries = widberries.scrape(oreht_name)
        except:
            id_wildberries, photo_wildberries = [], []
        try:
            articul = 'PCB-' + q
        except:
            articul = q
        result.append([oreht_image, articul, oreht_name, photo_wildberries, id_wildberries, photo_ozon, id_ozon])
        print(f"Выполено: {a} / {len(ids)}")
        with open(file='log.json', mode='w', encoding='utf-8') as f:
            f.write(json.dumps(result))
        f.close()

    excel.write_file(result, filename)


if __name__ == '__main__':
    main()
