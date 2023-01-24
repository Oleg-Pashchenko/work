import json
import excel

file = json.loads(open('log.json', 'r', encoding='UTF-8').read())
print(file)
excel.write_file(file, '')
