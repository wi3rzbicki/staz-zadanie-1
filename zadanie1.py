from bs4 import BeautifulSoup
from requests import get
import csv

URLC = "https://www.polskawliczbach.pl/Miasta"
page = get(URLC)
bs = BeautifulSoup(page.content, 'html.parser')

for line in bs.find_all('td'):
    city = line.find('a', href=True)

for x in city:
    tab[x]=city
    x += 1
    #URLx = "https://www.polskawliczbach.pl/", tab[x]

#data=

URLW = "https://www.polskawliczbach.pl/Wsie"
page2 = get(URLW)
bs2 = BeautifulSoup(page2.content, 'html.parser')

for line2 in bs.find_all('td'):
    village = line2.find('a', href=True)

import csv

f = open('path/to/csv_file', 'w', encoding='UTF8', newline='')

writer = csv.writer(f)

#writer.writerow(data)

f.close()
