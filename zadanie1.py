from bs4 import BeautifulSoup
import requests
import csv
import json
from tqdm import tqdm

URLC = "https://www.polskawliczbach.pl/Miasta"
page = get(URLC)
bs = BeautifulSoup(page.content, 'html.parser')
rows = soup.tbody.find_all("tr")

miasta = []

table_rows = soup.find("tbody").find_all("tr")

for row in tqdm(rows, desc="Scraping cities"):
    
    #miasta

    columns = row.find_all("td")
    _miasto = {}
    _miasto["name"] = columns[1].a.text
    _miasto["nazwa_uri"] = columns[1].a["href"]

    resp = requests.get(_miasto["nazwa_uri"])
    resp = BeautifulSoup(resp.text, "html.parser")

    #polozenie

    polozenie = resp.find("div", {"id": "polozenie"})
    polozenie = polozenie.find_all("div")[1]
    polozenie = polozenie.li.find_all("span")
    _miasto["coordinates"] = {
        "lat": float(polozenie[0].text), 
        "lon": float(polozenie[1].text)
        }

    del _miasto["nazwa_uri"]

    miasta.append(_miasto)

URLW = "https://www.polskawliczbach.pl/Wsie"
page2 = get(URLW)
bs2 = BeautifulSoup(page2.content, 'html.parser')
rows2 = soup.tbody.find_all("tr")

for row in table_rows2:
    village = row.find_all("td")[1].text

f = open('path/to/csv_file', 'w', encoding='UTF8', newline='')

writer = csv.writer(f)

#writer.writerow(data)

f.close()
