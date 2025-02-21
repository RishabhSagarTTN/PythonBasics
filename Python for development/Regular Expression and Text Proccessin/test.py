from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


def listing(link,type,name,price):
    global ans
    data=(requests.get(link).text)
    temp=BeautifulSoup(data,"html.parser").find("div",class_="pd_summary").p.text
    print((temp))
    pattern=re.compile(r"\d\.\s*[ a-zA-Z]*",flags=(re.I|re.M))
    ans=pattern.findall(temp)
    tempdict={
                "Link":"",
                "Name":"",
                "Type":"",
                "Price":""
                        }
    tempdict["Link"]=link
    tempdict["Price"]=price
    tempdict["Type"]=type
    tempdict["Name"]=name
    if type=="combo":
        for i in range(0,len(ans)):
            tempnamecombo=ans[i].split(".")[1]
            tempdict[f"Name{i+1}"]=tempnamecombo     
    print(tempdict)           
    return tempdict


ansdict=[]
try:
    number=1
    count=0
    type=["combo", "clump", "leaf", "plant", "pub","variegated"]
    while True:
        if number <2:
            temp=requests.get(f"https://fermosaplants.com/collections/sansevieria?page={number}").text
            soup = BeautifulSoup(temp, 'html.parser').find_all("div",class_="product-item-v5")
            temp=[]
            for i in soup:
              
                upper=i.div
                link="https://fermosaplants.com"+upper.h4.a.get("href")
                name=upper.h4.a.string
                type=""
                if "combo" in name.lower():
                   type="combo"
                if "clump" in name.lower():
                   type="clump"
                if "leaf" in name.lower():
                   type="leaf"
                if "plant" in name.lower():
                   type="plant" 
                if "pub" in name.lower():
                   type="pub"
                if "Variegated" in name.lower():
                   type="Variegated"
                count+=1
                
                price=upper.find("p",class_="price-product mb-0").span.string
                lister=listing("https://fermosaplants.com/collections/sansevieria/products/sansevieria-combo-offer-of-6-l",type,name,price)
                ansdict.append(lister)
                print(len(ansdict))
                break
            print(count)         
            number+=1
                
        else: 
            break
            
except Exception as e:
    print(e)
