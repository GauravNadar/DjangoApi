#!/usr/bin/python3.6
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rapidapipractice.settings')
django.setup()
from api.models import PetrolPrice

base_url = "https://www.goodreturns.in"
end_point = "/petrol-price.html"

html_text = requests.get(base_url+end_point).text

soup = BeautifulSoup(html_text, 'lxml')

data = []
state_data = {}

div = soup.find('div', attrs={'class':'fuel-state-list'})
table = div.find('table')
table_body = table.find('tbody')

rows = table.find_all('tr')
dictionary = {}
for row in rows:

    cols = row.find_all('td')  #3 tds

    for i in cols:
        dictionary[i.text.strip()] = i.find(href=True)['href'] if i.find(href=True) else None



i=0
for key, value in dictionary.items():
    data2 = []
    print("key : ", key, "value : ", value)
    if i == 2:
        break
    state_url = base_url+value

    url = state_url
    print('Downloading page %s...' % url)


    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    # op.add_argument(, 'headless')
    #driver = webdriver.Chrome(options=op)
    driver.get(url)

    html = driver.page_source
    soup2 = BeautifulSoup(html, features='lxml')

    # check out the docs for the kinds of things you can do with 'find_all'
    # this (untested) snippet should find tags with a specific class ID
    # see: http://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class
    table_div = soup2.find("div", class_="gold_silver_table")

    find = table_div.find("tbody")



    # rows = find.find_all('tr')
    # for row in rows:
    #     cols = row.find_all('td')
    #     cols = [ele.text.strip() for ele in cols]
    #     data.append([ele for ele in cols if ele])

    rows = find.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele for ele in cols]
        data2.append([ele.text.strip() for ele in cols if ele]) # Get rid of empty values


    state_data[key] = data2

    i=i+1




print(state_data)




all_data = PetrolPrice.objects.all()
all_data.delete()

for key, value in state_data.items():

    for val in value:
        PetrolPrice.objects.create(state=key,
                                        city=val[0],
                                        today_price=val[1],
                                        yesterday_price=val[2])

print("Done check db")

