# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:26:56 2020

@author: Apoorva
def memes(query):
    
    url='https://9gag.com/search?query='+query
    from selenium import webdriver
    from bs4 import BeautifulSoup as bs4
    import requests
    #driver = webdriver.Chrome()
    page=requests.get(url)
    titles=[]
    c=0
    soup = bs4(page.text, 'html.parser')
 
    a=outermost=soup.find_all("div")
    print(' '.join([x.get_attr("class") for x in a if(x.has_attr("class"))]) )
    b=a[1].find("div",{"class":"container"})
    c=b.find("div",{"class":"page"})
    d=c.find("div",{"class":"main-wrap"})
    e=d.find("section",{"class":"list-view-2"})
    for article in e.find_all("div"):
        titles.append(article.find("div").find("div").find("picture").find("img").getattr("src"))
    print(titles)
    memes("soccer")




from urllib.request import urlopen
url ="https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
html = urlopen(url.format(q="soccer"))
from bs4 import BeautifulSoup
soup = BeautifulSoup(html)
for res in soup.findAll('img'):
  print(res.get('src'))
"""
from urllib.request import Request, urlopen
import random
from firebase import firebase


# Get a database reference to our blog.

from bs4 import BeautifulSoup as soup
firebase = firebase.FirebaseApplication('https://sports-chatbot-267305.firebaseio.com/', None)


url ="https://me.me/t/funny"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
title = page_soup.findAll("img")
for x in title:
    try:
        data = {'url': x['src'],
                 'index': random.randint(1,1000)
          }
        result = firebase.post('/bot/memes/', data)
    except Exception:
        pass


  



