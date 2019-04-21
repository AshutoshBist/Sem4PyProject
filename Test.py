from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sqlite3

# opening up the connection and grabbing the page
my_url = 'https://www.newegg.com/global/in-en/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=samsung&N=-1&isNodeId=1'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
scraped = page_soup.find_all("a", {"title": "View Details"})
title=[]
for i in range(len(scraped)):
    title.append(scraped[i].text)
for i in range(len(title)):
    print(title[i])


print(title[0])