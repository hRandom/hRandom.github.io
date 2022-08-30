import requests
import webbrowser
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import random

p = 1
stars = ("angela-white","abella-danger","melissa-may")
n = random.randint(0,len(stars)-1)
exists = True
morePages = False
while exists == True:
    request = requests.get('https://www.pornhub.com/pornstar/{}/videos?page={}'.format(stars[n],p))
    if request.status_code == 200:
        p += 1
        print("E")
        morePages = True
    else:
        exists = False
        print("X")
p -= 1
print(p)

if morePages == False:
    url = "https://www.pornhub.com/pornstar/{}".format(stars[n])
else:
    pageNum = random.randint(1,p)
    url = "https://www.pornhub.com/pornstar/{}/videos?page={}".format(stars[n],pageNum)

result=[]
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
for c in soup.find_all('span', class_="title"):
    for link in c.find_all('a'):
        a = link.get('href')
        result.append(a)

n = random.randint(10,len(result)-1)
webbrowser.open("https://www.pornhub.com{}".format(result[n]))
