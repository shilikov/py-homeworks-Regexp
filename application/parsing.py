import re
from pprint import pprint

PHONE_SEARCH_PATTERN = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PHONE_SUB_PATTERN = r'8(\2)\3-\4-\5 \6\7'

def read_raw_data(data):
    result = list()
    for row in data:
        pprint(row)
        record = list()
        pprint(record)
        full_name = re.findall(r'(\w+)', ' '.join(row[:3]))
        # full_name = ' '.join(row[:3]).split(' ')
        # result = [full_name[0], full_name[1], full_name[2], row[3], row[4],
        #           re.sub(PHONE_SEARCH_PATTERN, PHONE_SUB_PATTERN, row[5]),
        #           row[6]]
        # record.append(result)
        pprint(full_name)
        full_name.append('') if len(full_name) < 3 else ... # https://proglib.io/p/30-ulovok-na-yazyke-python-kotorye-sdelayut-vas-luchshim-programmistom-2021-02-14
        pprint(full_name)
        
        record += full_name
        pprint(record)
        
        record.append(row[3])
        pprint(f'"3" добавляем место работы ,{record}')
        record.append(row[4])
        pprint(f'"4" Добавляем Био,{record}')
        record.append(re.sub(PHONE_SEARCH_PATTERN, PHONE_SUB_PATTERN, row[5]).strip())
        pprint(f'"5" Добавляе телефон ,{record}')
        record.append(row[6])
        pprint(f'"6" Емейл,{record}')
        result.append(record)
   
    return result

def true_contact_list(data):
    result = dict()
    for item in data:
        result[item[0]] = merge_doubl(item, result[item[0]]) if item[0] in result else item
    return result.values()

def merge_doubl(record_one, record_two):
    result = list()
    for index in range(len(record_one)):
        result.append(record_one[index]) if record_one[index] else result.append(record_two[index])
    return result

