from bs4 import BeautifulSoup
from requests import get

URL = "https://www.polskawliczbach.pl/Miasta"
page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

for line in bs.find_all('td'):
    city = line.find('a', href=True)

URL2 = "https://www.polskawliczbach.pl/Wsie"
page2 = get(URL2)
bs2 = BeautifulSoup(page2.content, 'html.parser')

for line2 in bs.find_all('td'):
    village = line2.find('a', href=True)
