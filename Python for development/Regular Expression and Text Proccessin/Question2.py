from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


class FermosaExtracter:
    """Fermosa class is used for fetching the data from the fermosa site which main
    aim is to fetch the the data of the plant from the site it consist three
    method name----
    __makeData-> making the dictionary of the particular plant which consist all the info aboutthe plant
    savedata-> saving the data to the excel file
    __core -> it make the request to the page which consist all the plant in that page
    class takes four parameter----
    outputname------ output file name with default value given result.xlsx
    totalpagesno ----- take the totalpagesno which user want to extract the data
    url ----- url for the baseurl for extracting the data

    """


    def __init__(self,url,totalpagesno,outputname="result.xlsx"):
        self.ansdict=[]
        self.outputname=outputname
        self.totalpages=totalpagesno
        self.url=url
        self.__core()

    def makeData(self,link,type,name,price,varigated):
        "making the dictionary of the particular plant which consist all the info aboutthe plant"
        try:
            data=(requests.get(link).text)
            temp=BeautifulSoup(data,"html.parser").find("div",class_="pd_summary").p.text
            pattern=re.compile(r"\d\.\s*[ a-zA-Z]*",flags=re.I)
            ans=pattern.findall(temp)

            #making of the temp dict for the particular plant 
            tempdict={
                        "Link":"",
                        "Name":"",
                        "Type":"",
                        "Price":"",
                        "Variegated":""
                                }
            tempdict["Link"]=link
            tempdict["Price"]=price
            tempdict["Type"]=type
            tempdict["Name"]=name
            tempdict["Variegated"]=varigated
            if type=="combo":
                for i in range(0,len(ans)):
                    tempnamecombo=ans[i].split(".")[1].split("Images")[0]
                    tempdict[f"Name{i+1}"]=tempnamecombo  
        except Exception as e:
            print(e)
            return f"Error hogaya {e}"               
        return tempdict


    def __core(self):
        """it make the request to the page which consist all the plant in that page"""

        try:
            number=1
            count=0
            type=["combo", "clump", "leaf", "plant", "pub","variegated"]
            while True:
                if number <self.totalpages:
                    temp=requests.get(f"{self.url}?page={number}").text
                    soup = BeautifulSoup(temp, 'html.parser').find_all("div",class_="product-item-v5")
                    temp=[]
                    for i in soup:
                        varigated="Not Valid"
                        upper=i.div
                        link="https://fermosaplants.com"+upper.h4.a.get("href")
                        name=upper.h4.a.string
                        type="Uncategorized"
                        if "combo" in name.lower():
                            type="combo"
                        elif "clump" in name.lower():
                            type="clump"
                        elif "leaf" in name.lower():
                            type="leaf"
                        elif "plant" in name.lower():
                            type="plant" 
                        elif "pub" in name.lower():
                            type="pub"
                        if "combo" not in name.lower():
                            if "variegated" in name.lower():
                                varigated="Variegated"
                            else:
                                varigated="Not Varigeted"
                        
                        price=upper.find("p",class_="price-product mb-0").span.string
                        lister=self.makeData(link,type,name,price,varigated)
                        self.ansdict.append(lister)
                        count+=1
                    number+=1
                        
                else: 
                    break
                    
        except Exception as e:
            print(e)

        # calling the saveData method to save the data in the excel file    
        self.saveData()    

    def saveData(self):
        """saving the data to the excel file"""


        df = pd.DataFrame(self.ansdict)
        df.to_excel(self.outputname, index=False, engine='openpyxl')



FermosaExtracter("https://fermosaplants.com/collections/sansevieria",8)

