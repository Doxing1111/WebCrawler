from bs4 import BeautifulSoup
import requests

lottery=requests.get('http://www.taiwanlottery.com.tw/').content

soup=BeautifulSoup(lottery,'html.parser')

links=soup.findAll('a')

for link in links:
    print(link.string)