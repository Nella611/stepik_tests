import requests
way = input()
with open(way) as inf:
    for line in inf:
        adr = line.strip()
#print(adr)
def open_file(address):
    text = requests.get(address).text

    if text[0:2] == 'We':
       print(text)
    else:
        address_2 = 'https://stepic.org/media/attachments/course67/3.6.3/' + text
        print(address_2)
        return open_file(address_2)

open_file(adr)