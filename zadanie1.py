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

get_cities()

def get_geo():
    
    for row in tqdm(rows, desc="Scraping cities"):

        columns = row.find_all("td")

        _city["name"] = columns[1].a.text
        _city["name"] = _city["name"].replace(' ', '_').replace('-', '_').replace('Ó', 'O').replace('ó', 'o').replace('Ę', 'E').replace('ę', 'e').replace('Ą', 'A').replace('ą', 'a').replace('Ś', 'S').replace('ś', 's').replace('Ł', 'L').replace('ł', 'l').replace('Ż', 'Z').replace('ż', 'z').replace('Ź', 'Z').replace('ź', 'z').replace('Ć', 'C').replace('ć', 'c').replace('Ń', 'N').replace('ń', 'n')


        #_city["name_uri"] = "https://www.polskawliczbach.pl/"_city["name"]""

        resp = get(_city["name_uri"])
        resp = BeautifulSoup(resp.text, "html.parser")

        #polozenie

        geo = resp.find("div", {"id": "geo"})
        geo = geo.find_all("div")[1]
        geo = geo.li.find_all("span")
        _city["coordinates"] = {
            "lat": float(geo[0].text), 
            "lon": float(geo[1].text)
            }

#get_geo()

#del _city["name_uri"]

    #cities.append(_city)

#cities = []

#URLW = "https://www.polskawliczbach.pl/Wsie"
#page2 = get(URLW)
#bs2 = BeautifulSoup(page2.content, 'html.parser')
#rows2 = bs2.tbody.find_all("tr") 

#for row in table_rows2:
#    village = row.find_all("td")[1].text

#f = open('path/to/csv_file', 'w', encoding='UTF8', newline='')

#writer = csv.writer(f)

#writer.writerow(data)

#f.close()
