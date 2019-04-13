from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# opening up the connection and grabbing the page
my_url = 'https://www.flipkart.com/search?q=graphics+card&sort=relevance'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")
containers = page_soup.find_all("div", {"class": "_3liAhj _1R0K0g"})
print(len(containers))
print(containers[0])