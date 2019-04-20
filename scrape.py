
# opening up the connection and grabbing the page
my_url = 'https://www.flipkart.com/search?q=predator&sort=relevance'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")
title = page_soup.find_all("div", {"class": "_3wU53n"})
product_link = page_soup.find_all("a", {"class": "_31qSD5"})
selling_price1 = page_soup.find_all("div", {"class": "_1vC4OE _2rQ-NK"})
selling_price=[]
i=0
for i in range(0,len(selling_price1)):
    k = selling_price1[i].text
    k=k.replace(",","")
    selling_price.append(int(k.replace("₹" , "")))
seller = "Flipkart"


conn = sqlite3.connect('Database.db')
cursor = conn.cursor()
cursor.execute('create table if not exists Database (title varchar, product_link varchar,selling_price int,seller varchar)')

i = 0
l=10
if len(title)<10:
    l=len(title)
while i < l:
    cursor = conn.cursor()
    conn.execute("INSERT INTO Database VALUES(?,?,?,?)", (title[i].text, product_link[i].get("href"),selling_price[i], seller))
    conn.commit()
    print("\n")
    i += 1


