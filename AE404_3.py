# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:21:57 2020

@author: kylel
"""
from bs4 import BeautifulSoup
import requests
res = requests.get('https://www.books.com.tw/web/sys_saletopb/books')
soup = BeautifulSoup(res.text,'html.parser')
lis = soup.find_all("li",class_="item")

for each_li in lis:
    
    img = each_li.find("img")
    print(img)
    
for each_li in lis:
    img = each_li.find("img")
    imgSrc = img['src']
    bookName = img['alt']
    print(bookName ,imgSrc)
    
for each_li in lis[:30]:
    img = each_li.find("img")
    imgSrc = img['src']
    bookName = img['alt']
    
    imgRespond = requests.get(imgSrc)
    print(imgRespond) 
    print(imgRespond.content)
    with open(bookName+".jpg","bw") as file:
       file.write(imgRespond.content)