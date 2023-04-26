import json

out_file_name='output.csv'

f = open(f'./output/{out_file_name}')
content = f.readlines()
f.close()

date_count = dict()

for line in content[1:]:
    l = line.strip().split(',')
    date = l[0]
    time = l[1]
    name = l[2]

    if date in date_count:
        if name in date_count[date]:
            date_count[date][name] += 1
        else:
            date_count[date][name] = 1
    else:
        date_count[date] = dict()

out = open('./output/flourish_prep.json', 'w')
out.write(json.dumps(date_count))

