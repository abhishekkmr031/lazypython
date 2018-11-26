### this web crawler will use BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Enter the url : ")
page = urlopen(url)
data = page.read().decode('utf-8')

soup = BeautifulSoup(data)
##print(soup.get_text())
for link in soup.find_all('a'):
    print(link.get('href'))
