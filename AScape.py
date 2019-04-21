from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sqlite3

# opening up the connection and grabbing the page
my_url = 'https://www.newegg.com/global/in-en/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=samsung&N=-1&isNodeId=1'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")
title = page_soup.find_all("a", {"title": "View Details"})
product_link = page_soup.find_all("a", {"title": "View Details"})
selling_price1 = page_soup.find_all("li", {"class": "price-current"})
selling_price=[]
for i in range(0, len(selling_price1)):
    k1 = []
    k = selling_price1[i].text
    k1 = k.split()
    if k1 == []:
        k1.append('0')
        k1.append('0')
    selling_price.append(int(k1[1].replace(",", "")))
seller = "Newegg"
conn = sqlite3.connect('Database.db')
cursor = conn.cursor()
cursor.execute(
    'create table if not exists Database (title varchar, product_link varchar,selling_price int,seller varchar)')
i = 0
l = 10

if len(title) < 10:
    l = len(title)
while i < l:
    if selling_price[i] != 0:

        cursor = conn.cursor()
        conn.execute("INSERT INTO Database VALUES(?,?,?,?)",
                     (title[i].text, product_link[i].get("href"), selling_price[i], seller))
        conn.commit()
        print("\n")
    i += 1
