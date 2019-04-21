import tkinter
from tkinter import *
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sqlite3
import webbrowser


def on_click():
    # CONNECT TO DATABASE

    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE if exists Database')  # CLEAR PREVIOUS EXISTING TABLE
    cursor.execute(
        'create table if not exists Database (title varchar, product_link varchar,selling_price int,seller varchar)')  # ADDS TABLE IT DOES NOT EXIST

    text = Sbox.get()  # GETS THE TEXT FROM THE SEARCH BOX

    # FLIPKART SCRAPE 1

    F_link = 'https://www.flipkart.com/search?q=' + text.replace(" ", "+") + '&sort=relevance'  # CREATES THE LINK
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
                       (title[i].text, 'https://www.flipkart.com' + product_link[i].get("href"), selling_price[i],
                        seller))
        conn.commit()
        print("\n")
        i += 1

    # FLIPKART SCRAPE 2

    my_url = F_link
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")
    title = page_soup.find_all("a", {"class": "_2cLu-l"})
    product_link = page_soup.find_all("a", {"class": "_2cLu-l"})
    selling_price1 = page_soup.find_all("div", {"class": "_1vC4OE"})
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
    while i < l:
        cursor = conn.cursor()
        conn.execute("INSERT INTO Database VALUES(?,?,?,?)",
                     (title[i].text, 'https://www.flipkart.com/' + product_link[i].get("href"), selling_price[i],
                      seller))
        conn.commit()
        print("\n")
        i += 1

    # NEW EGG SCRAPE

    E_link = 'https://www.newegg.com/global/in-en/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=' + text.replace(
        " ", "+") + '&N=-1&isNodeId=1'
    # opening up the connection and grabbing the page
    my_url = E_link
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")
    title = page_soup.find_all("a", {"title": "View Details"})
    product_link = page_soup.find_all("a", {"title": "View Details"})
    selling_price1 = page_soup.find_all("li", {"class": "price-current"})
    selling_price = []
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


    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=760, height=500)

    def open_url(url):
        pass
        link = url
        webbrowser.open_new_tab(link)

    outer = Frame(main, height=760, width=500)
    outer.pack(padx=5, pady=5)
    canvas = Canvas(outer)
    root = Frame(canvas)
    myscrollbar = Scrollbar(outer, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)
    myscrollbar.pack(side="right", fill="y")

    for i in range(0, len(db_title)):
        product = Frame(root)
        l1 = Label(product, text=db_title[i], font="Georgia 16", wraplength=700)
        l1.pack(padx=5, pady=5)
        l2 = Label(product, text='Price : ₹ ' + str(db_productprice[i]), font="Georgia 16")
        l2.pack(padx=5, pady=5)
        l3 = Label(product, text=db_productlink[i], font="Georgia 16", wraplength=700, fg="blue", cursor="hand2")
        url = l3.cget("text")
        l3.bind("<Button-1>", lambda e, url=url: open_url(url))
        l3.pack()
        l3.pack(padx=5, pady=5)
        l4 = Label(product, text=db_company[i], font="Georgia 16")
        l4.pack(padx=5, pady=5)
        product.pack(padx=5, pady=5)
        separator = Frame(root, height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

    canvas.pack(side=LEFT)
    canvas.create_window((0, 0), window=root, anchor='nw')
    root.bind("<Configure>", myfunction)


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
