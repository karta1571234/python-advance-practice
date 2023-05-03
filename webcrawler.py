# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:58:33 2020

@author: karta
"""


import urllib.request as req
import requests


url="https://www.dcard.tw/f"
headers={"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}

#在Http的headers加上User-Agent的資訊
request=req.Request(url,headers=headers)
response=requests.get(url)
print(response)

if response.status_code==requests.codes.ok:
    with req.urlopen(request) as source:
        data=source.read().decode("utf-8")
    #網站的html原始碼
        
    from bs4 import BeautifulSoup
    #引入第三方套件bs4
    soup=BeautifulSoup(data,"html.parser")
    #讓bs解析html
    """
    article=soup.find("article")
    print(article)
    """
    artilist=[]
    
    article=soup.find_all("a",class_="sc-1v1d5rx-3 kPUUNB")
    for item in article:
        print(item.text)
        artilist.append(item.text)
        
    http=soup.find_all("a href")
    for item in http:
        print("http",http)
        
else:
    print(response.status_code)
print("\n")
#開始把抓到的資料放入json裡    
import json
print(artilist)
print(type(article))
print(type(artilist))
print("\n")
#使用dump將python資料型態存成json檔(write)
with open("Dcard.json","w",encoding="utf-8") as DJfile:
    json.dump(artilist,DJfile)
#使用load將儲存的資料讀取進程式裡(read)
with open("Dcard.json","r",encoding="utf-8") as Djfile:
    output=json.load(Djfile)
    print(output)
print(type(output))
#使用Yattag 產生HTML file

from yattag import Doc
from yattag import indent

doc,tag,text=Doc().tagtext()

doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('head'):
        with tag('title'):
            text('Dcard標題')
        with tag('style'):
            text('table,tr,td {border:1px solid gray;border-collaose:collaspse;text-align:center;} \n th {padding:5px;text-align:center;background-color:slateblue;}')
        doc.stag("meta",charset="UTF-8")
    with tag('body'):
        with tag('h6'):
            text(f'狀態:{response}')
        with tag('h1',style="background-color: blanchedalmond;color: cadetblue;text-align: center;"):
            text('Dcard')
        doc.stag('p')
        with tag('table',style="width:100%"):
            with tag('tr'):
                with tag('th',colspan="2"):
                    text('標題')
            for i,item in enumerate(output):
                with tag('tr'):
                    with tag('td'):
                        text(i)
                    with tag('td'):
                        text(item)
#使用Yattag產生出來的HTML
print(indent(doc.getvalue()))   
#將HTML寫到final.html
with open("DcardTitle.html","w",encoding="utf-8") as final:
    final.write(indent(doc.getvalue()))
    final.close()