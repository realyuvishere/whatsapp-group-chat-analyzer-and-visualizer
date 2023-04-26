import json
from config import MAIN_OUT_FILE, FLOURISH_JSON_OUT_FILE, FLOURISH_OUT_FILE

f = open(f'./output/{MAIN_OUT_FILE}')
content = f.readlines()
f.close()

date_count = dict()
names = dict()

for line in content[1:]:
    l = line.strip().split(',')
    date = l[0]
    time = l[1]
    name = l[2]

    if name not in names:
        names[name] = []
    
    if date in date_count:
        if name in date_count[date]:
            date_count[date][name] += 1
        else:
            date_count[date][name] = 1
    else:
        date_count[date] = dict()

flourish_headers = ['names']

for date_ in date_count:
    # Fa
    flourish_headers.append(date_)
    for name_ in names:
        if name_ in date_count[date_]:
            # write here
            break




out = open(f'./output/{FLOURISH_JSON_OUT_FILE}', 'w')
out.write(json.dumps(date_count))
out.close()