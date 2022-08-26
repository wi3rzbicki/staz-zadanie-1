from bs4 import BeautifulSoup
from requests import get
import csv
from tqdm import tqdm
    
URLC = "https://www.polskawliczbach.pl/Miasta"
page = get(URLC)
bs = BeautifulSoup(page.content, 'html.parser')
rows = bs.tbody.find_all("tr")
_city = {}

def get_cities():

    for row in tqdm(rows, desc="Scraping cities"):
    
        columns = row.find_all("td")
    
        #miasta

        _city["name"] = columns[1].a.text
        _city["name"] = _city["name"].replace(' ', '_').replace('-', '_').replace('Ó', 'O').replace('ó', 'o').replace('Ę', 'E').replace('ę', 'e').replace('Ą', 'A').replace('ą', 'a').replace('Ś', 'S').replace('ś', 's').replace('Ł', 'L').replace('ł', 'l').replace('Ż', 'Z').replace('ż', 'z').replace('Ź', 'Z').replace('ź', 'z').replace('Ć', 'C').replace('ć', 'c').replace('Ń', 'N').replace('ń', 'n')

        print(_city)

#get_cities()

def get_geo():
    
    for row in tqdm(rows, desc="Scraping cities"):

        columns = row.find_all("td")

        _city["name"] = columns[1].a.text
        _city["name"] = _city["name"].replace(' ', '_').replace('-', '_').replace('Ó', 'O').replace('ó', 'o').replace('Ę', 'E').replace('ę', 'e').replace('Ą', 'A').replace('ą', 'a').replace('Ś', 'S').replace('ś', 's').replace('Ł', 'L').replace('ł', 'l').replace('Ż', 'Z').replace('ż', 'z').replace('Ź', 'Z').replace('ź', 'z').replace('Ć', 'C').replace('ć', 'c').replace('Ń', 'N').replace('ń', 'n')
        if columns[3] == 'mazowieckie':
            _city["name"] = _city["name"].replace('jozefow', 'jozefow_mazowieckie')
        else:
            _city["name"] = _city["name"].replace('jozefow', 'jozefow_lubelskie')

        _city["name_uri"] = "https://www.polskawliczbach.pl/" + _city["name"]

        resp = get(_city["name_uri"])
        resp = BeautifulSoup(resp.text, "html.parser")

        #polozenie

        geo = resp.find("div", {"id": "polozenie"})
        geo = geo.find_all("div")[1]
        geo = geo.li.find_all("span")
        _city["coordinates"] = {
            "E": float(geo[0].text), 
            "N": float(geo[1].text)
            }

        print(_city["name"],_city["coordinates"])

fieldnames = ['name', 'coordinates' ]

get_geo()

rows = [
    {'name': _city["name"],
    'coordinates': _city["coordinates"]}
]

with open('cities.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
