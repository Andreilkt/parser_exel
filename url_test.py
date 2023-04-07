
"""
from urllib.request import urlopen
url = 'http://127.0.0.1:8000/'
page = urlopen(url)
print(page.read().decode('utf-8'))


from bs4 import BeautifulSoup
import requests
url = 'http://127.0.0.1:8000/'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
print(soup)
"""

from urllib.request import urlopen
from lxml import etree
url = 'http://127.0.0.1:8000/'
page = urlopen(url)
html_code = page.read().decode('utf-8')
tree = etree.HTML(html_code)
print(tree.xpath("/html/body/div[1]/table/tbody/tr/td[1]/a/@href")[0])

"""
from urllib.request import urlopen
from lxml import etree
url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones'
page = urlopen(url)
html_code = page.read().decode('utf-8')
tree = etree.HTML(html_code)
sp = tree.xpath("//li/a/@href")
links = set()
for link in sp:
    if link.startswith('http'):
        links.add(link)
for link in links:
    print(link)

"""
