from bs4 import BeautifulSoup
import requests
url = 'http://example.com'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
print(soup)
