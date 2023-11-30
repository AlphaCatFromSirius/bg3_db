import csv
import requests

from bs4 import BeautifulSoup


URL = 'https://baldursgate3.wiki.fextralife.com/Weapons'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}

response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, features="lxml")

table_rows = soup.find('table').find_all('tr')
l = []

with open('weapon.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    for row in table_rows:
        l.append(row.get_text().strip().split('\n'))

    for l2 in l:
        map(str.strip, l2)
        writer.writerow(l2)
