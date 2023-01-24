import json

import excel
import oreht
import ozon
import telegram_bot
import widberries


def parser():
    print("Started!")
    filename = 'Копия Прайслист.xlsx'
    filename = 'ПарсингBOT (1).xlsx'
    ids = excel.read_file(filename)
    result = []  # recht photo, articul, recht_name, photo_wb, articul_wb, photo_ozon, id_ozon
    a = 0
    to_write = []
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
        to_write.append(result)
        print(f"Выполено: {a} / {len(ids)}")

        with open(file='log.json', mode='w', encoding='utf-8') as f:
            f.write(json.dumps(result))
        f.close()

        if a % 100 == 0:
            print('Отправка файла!')
            excel.write_file(to_write, filename)
            telegram_bot.send_document_to_telegram()
            to_write = []
    excel.write_file(result, filename)
    telegram_bot.send_document_to_telegram()


if __name__ == '__main__':
    import threading
    thread1 = threading.Thread(target=parser)
    thread2 = threading.Thread(target=telegram_bot.bot)
    thread1.start()
    thread2.start()
