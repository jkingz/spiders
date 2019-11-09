import requests
import openpyxl
from bs4 import BeautifulSoup
from openpyxl import Workbook

data = requests.get('https://www.pesobility.com/stock')
soup = BeautifulSoup(data.text, 'html.parser')
datas = soup.find_all('tr')

headers = ['Symbol','Name','Current Price (%)','Previous Close', '52-Week High(%)', '52-Week Low(%)', 'PE', '2018 Cash Div (%)']
filename = "hello_world.xlsx"
workbook = Workbook()
sheet = workbook.active
sheet.title = 'Philippine Stock Exchange Companies'
sheet.append(headers)

for tr in datas:
    for td in tr.find_all('td'):
        values = [td.text for td in tr.find_all('td')]
        print(values)
        sheet.append(values)

sheet.freeze_panes = "C2"
workbook.save(filename=filename)