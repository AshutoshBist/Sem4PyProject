import tkinter
from tkinter import *
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sqlite3


def on_click():
    # CONNECT TO DATABASE

    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE if exists Database')  #CLEAR PREVIOUS EXISTING TABLE
    cursor.execute(
        'create table if not exists Database (title varchar, product_link varchar,selling_price int,seller varchar)') #ADDS TABLE IT DOES NOT EXIST

    text = Sbox.get()   #GETS THE TEXT FROM THE SEARCH BOX

    F_link = 'https://www.flipkart.com/search?q=' + text.replace(" ","+") + '&sort=relevance' #CREATES THE LINK
    # opening up the connection and grabbing the page
    my_url = F_link
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")
    title = page_soup.find_all("div", {"class": "_3wU53n"})
    product_link = page_soup.find_all("a", {"class": "_31qSD5"})
    selling_price1 = page_soup.find_all("div", {"class": "_1vC4OE _2rQ-NK"})
    selling_price = []
    i = 0
    for i in range(0, len(selling_price1)):
        k = selling_price1[i].text
        k = k.replace(",", "")
        selling_price.append(int(k.replace("₹", "")))
    seller = "Flipkart"

    i = 0
    l = 10
    if len(title) < 10:
        l = len(title)
    gcount = l
    while i < l:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Database VALUES(?,?,?,?)",
                       (title[i].text, product_link[i].get("href"), selling_price[i], seller))
        conn.commit()
        print("\n")
        i += 1

    E_link = 'https://www.newegg.com/global/in-en/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=' + text.replace(" ","+") + '&N=-1&isNodeId=1'
    # opening up the connection and grabbing the page
    my_url = E_link
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")
    title = page_soup.find_all("a", {"class": "item-title"})
    product_link = page_soup.find_all("a", {"class": "item-title"})
    selling_price1 = page_soup.find_all("li", {"class": "price-current"})

    i = 0
    selling_price = []
    for i in range(0, len(selling_price1)):
        k1 = []
        k = selling_price1[i].text
        k1 = k.split()
        selling_price.append(int(k1[1].replace(",", "")))
    seller = "Newegg"

    i = 0
    l = 10
    if len(title) < 10:
        l = len(title)
    gcount = gcount + l
    while i < l:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Database VALUES(?,?,?,?)",
                       (title[i].text, product_link[i].get("href"), selling_price[i], seller))
        conn.commit()
        print("\n")
        i += 1

    root = Frame(main, width=768, height=576)
    root.pack()
    db_title = []
    db_productlink = []
    db_productprice = []
    db_company = []
    cursor.execute('SELECT title,product_link,selling_price,seller FROM Database ORDER BY selling_price ASC')
    for row in cursor.fetchall():
        db_title.append(row[0].strip())
        db_productlink.append(row[1])
        db_productprice.append(row[2])
        db_company.append(row[3])


    for i in range(0, 20):
        print(db_title[i])
    for i in range(0, 20):
        print(db_productlink[i])
    for i in range(0, 20):
        print(db_productprice[i])
    for i in range(0, 20):
        print(db_company[i])

main = Tk()
main.title("Best Deals")
main.configure(bg='#999999')
main.geometry("800x600")

L1 = Label(main, text='Best Deal', fg='#CD3131', bg='#999999', font="Georgia 20 bold", bd=20)
L1.pack(side=TOP)

Sbox = Entry(main, text='Product Name', bd=5, width=50, font="Georgia 16 ")
Sbox.pack(side=TOP)

E_Searched = tkinter.Button(main, text="Go", font="Georgia 16 ", activebackground='#30D9D8', command=on_click)
E_Searched.pack(side=TOP, padx=5, pady=5)

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

main.mainloop()
