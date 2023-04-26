import re

filename = '_chat.txt'

f = open(f"./data/{filename}")

data = list()
content = f.readlines()
f.close()
headers = ['date', 'time', 'user', 'media']
message_count = 0
for line in content:
    l = line.strip()
    date_re = r"\d\d/\d\d/\d\d, \d+:\d\d:\d\d [A|P]M"
    date_match = re.search(date_re, l)
    if date_match:
        message_count += 1
        media_re = r"[GIF|image|audio|sticker] omitted"
        media_match = re.search(media_re, l)

        message_date = date_match.group()
        name = l[l.index(message_date) + len(message_date) + 2:].split(':')[0].rstrip().replace('\u202a', '').replace('\u202c', '').replace('\u00a0', '')
        hasMedia = str(int(bool(media_match)))
        data.append(','.join([message_date, name, hasMedia]))


print(f"Number of messages: {message_count}")
out = open('./output/output.csv', 'w')
out.write('\n'.join([','.join(headers)] + data))
out.close()