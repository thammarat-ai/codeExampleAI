#Example 11.5 Wiki table scrap with Beautiful Soup
#pip install requests beautifulsoup4 
from bs4 import BeautifulSoup
import requests
import csv

#url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
url = "https://en.wikipedia.org/wiki/World_population"
soup = BeautifulSoup(requests.get(url).text, 'html.parser')

tables = soup.find_all('table', class_='sortable')
print(len(tables))

for table in tables:
    ths = table.find_all('th')
    headings = [th.text.strip() for th in ths]
    #print(headings)

table = tables[4]
population = []
for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    #print(tds)        
    if not tds:
        continue
    population.append(tds[0].text.replace('\n', ' ').strip())
print(population)
