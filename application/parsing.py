import re
import pprint

PHONE_SEARCH_PATTERN = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PHONE_SUB_PATTERN = r'8(\2)\3-\4-\5 \6\7'

def read_raw_data(data):
    result = list()
    for row in data:
        record = list()
        full_name = re.findall(r'(\w+)', ' '.join(row[:3]))
        full_name.append('') if len(full_name) < 3 else ...
        record += full_name
        record.append(row[3])
        record.append(row[4])
        record.append(re.sub(PHONE_SEARCH_PATTERN, PHONE_SUB_PATTERN, row[5]).strip())
        record.append(row[6])
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

