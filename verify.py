import json
from flourish_prep import names, date_count
from config import MAIN_IN_FILE, VERIFICATION_OUT_FILE

names_aggregate = dict()

f = open(f"./data/{MAIN_IN_FILE}")
content = f.read()
f.close()

for n_ in names:
    m_name = f'{n_}:'
    file_count = content.count(m_name)
    names_aggregate[n_] = {
        'file': file_count,
        'count': 0
    }

for _date in date_count:
    for _name in date_count[_date]:
        names_aggregate[_name]['count'] += date_count[_date][_name]


out = open(f'./output/{VERIFICATION_OUT_FILE}', 'w')
out.write(json.dumps(names_aggregate))
out.close()