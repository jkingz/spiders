import requests
import json
from bs4 import BeautifulSoup


data = requests.get('https://www.pesobility.com/stock')
soup = BeautifulSoup(data.text, 'html.parser')
datas = soup.find_all('tr')


with open('data.json', 'w') as write_file:
    for td in datas:
        values = [td.text for td in td.find_all('td')]
        json.dump(values, write_file)