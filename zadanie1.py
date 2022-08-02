from bs4 import BeautifulSoup
import requests
import csv
import json
from tqdm import tqdm

URLC = "https://www.polskawliczbach.pl/Miasta"
page = get(URLC)
bs = BeautifulSoup(page.content, 'html.parser')
table_rows = soup.find("tbody").find_all("tr")

for row in tqdm(rows, desc="Scraping cities"):
    
    #miasta

    columns = row.find_all("td")
    _miasto = {}
    _miasto["name"] = columns[1].a.text

    #polozenie

    polozenie = resp.find("div", {"id": "polozenie"})
    polozenie = polozenie.find_all("div")[1]
    polozenie = polozenie.li.find_all("span")
    _miasto["coordinates"] = {
        "lat": float(polozenie[0].text), 
        "lon": float(polozenie[1].text)
        }

    for li in powierzchnia:
        if "Powierzchnia" in li.text:
            _miasto["area"] = float(li.span.text[:-4].replace(",",".").replace(" ",""))

    del _miasto["nazwa_uri"]

    miasta.append(_miasto)

with open ("text.json","w",encoding="utf-8") as f:
    f.write(json.dumps(miasta, ensure_ascii=False))

#for x in city:
#    x = city
#    tab = []
#    tab.append(x)
#URL = "https://www.polskawliczbach.pl/", city

#data=

URLW = "https://www.polskawliczbach.pl/Wsie"
page2 = get(URLW)
bs2 = BeautifulSoup(page2.content, 'html.parser')
table_rows2 = soup.find("tbody").find_all("tr")

for row in table_rows2:
    village = row.find_all("td")[1].text

f = open('path/to/csv_file', 'w', encoding='UTF8', newline='')

writer = csv.writer(f)

#writer.writerow(data)

f.close()
