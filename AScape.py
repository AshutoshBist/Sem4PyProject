from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sqlite3

# opening up the connection and grabbing the page
my_url = 'https://www.amazon.in/s?k=samsung+mobile&ref=nb_sb_noss_2'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")
title = page_soup.find_all("div", {"class": "_3wU53n"})
product_link = page_soup.find_all("a", {"class": "_31qSD5"})
selling_price = page_soup.find_all("div", {"class": "_1vC4OE _2rQ-NK"})
seller = "Flipkart"

conn = sqlite3.connect('Database.sql')
cursor = conn.cursor()
cursor.execute(
    'create table if not exists Database (title varchar, product_link varchar,selling_price varchar,seller varchar)')
i = 0
while i < len(title):
    cursor = conn.cursor()
    conn.execute("INSERT INTO Database VALUES(?,?,?,?)", (title[i].text, product_link[i].get("href"),selling_price[0].text, seller))
    conn.commit()
    print("\n")
    i += 1