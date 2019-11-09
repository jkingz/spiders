import requests
from bs4 import BeautifulSoup
from csv import writer



data = requests.get('https://www.pesobility.com/stock')
soup = BeautifulSoup(data.text, 'html.parser')
datas = soup.find_all('tr')

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Symbol', 'Name', 'Current Price', 'Prev Close']
    csv_writer.writerow(headers)

    for td in datas:
        values = [td.text for td in td.find_all('td')]
        symbol = values[0]
        name = values[1]
        curr_price = values[2]
        prev_close = values[3]
        print(values)
        csv_writer.writerow([symbol, name, curr_price, prev_close])

