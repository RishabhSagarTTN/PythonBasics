import requests
import json

class NPIData:
    """NPIData class is used to fetch the data from the npiregistry website"""
    def __init__(self, filename, jsonfilename):
          self.filename=filename
          self.jsonfilename=jsonfilename
          
    def start(self):
         """Method to start the fetching process"""
         self.__core()

    def __core(self):
        """__core is the main method of the class which fetches the data from the npiregistry website and store the data in the data.json file"""
        with open(self.filename, 'r') as file: # this is the file name where the serial numbers is strored which is used for fetching the data
            with open(self.jsonfilename, "w") as fileJson:# this is where the data is stored
                alldata=[]
                print("Fetching of the data has been started -----")
                for i in file:
                    try:
                            response=requests.post("https://npiregistry.cms.hhs.gov/RegistryBack/npiDetails",json={"number":i.strip('\n"')})
                            response.raise_for_status()
                            response=response.json()

                            # temp is the temporary dictionary used to make the appropriate key value pair from the cluster of key value pair, it
                            #is the dictionary that is stored in json list
                            temp={"Number":"","Enumeration Date":"",
                                "Enumeration Type":"","Sole Proprietor":"",
                                "Satus":"","Addresses":"","Taxonomies":""}
                            temp["Number"]=response.get("number","")
                            temp["Enumeration Date"]=response["basic"].get("enumerationDate", "")
                            temp["NPI Type"]=response["enumerationType"]
                            temp["Sole Proprietor"]=response["basic"].get("soleProprietor", "")
                            if response["basic"]["status"]=="A":
                                temp["Satus"]="Active"
                            else:
                                temp["Satus"]="Inactive"
                            templist=[]
                            tempdictionary=[{"Mailing Address":[]},{"Primary Practice Address":[]}]
                            for i in response["addresses"]:
                                temp2={"Street-1":"","Street-2":"","State":"",
                                "City":"","Pin":"","Phone":"","Fax":"",
                                "Zip":""}
                                temp2["Street-1"]=i["addressLine1"]
                                temp2["Street-2"]=i["addressLine2"]
                                temp2["State"]=i["state"]
                                temp2["City"]=i["city"]
                                temp2["Pin"]=i["postalCode"]
                                temp2["Phone"]=i.get("teleNumber","")
                                temp2["Fax"]=i.get("faxNumber","")
                                temp2["Zip"]=i["postalCode"]
                                templist.append(temp2)
                            tempdictionary[0]["Mailing Address"]=templist[0]
                            tempdictionary[1]["Primary Practice Address"]=templist[1]
                            temp["Addresses"]=tempdictionary
                            temp["Taxonomies"]=response["taxonomies"]
                            alldata.append(temp)# appending each record in the alldata so that at last we can dump it into the json file
                    except requests.exceptions.HTTPError as e:
                        print(f"HTTP error occurred for {i}: {e}")
                    except Exception as e:
                         pass         
                 # dumping of the alldata into the data.json file(fileJson)       
                json.dump(alldata,fileJson,indent=4)
                print("---------------Finisted please review the file----------------------------")        
                        
# ------------------------------TESTING-----------------------------------                        
test=NPIData("number.txt","data.json")
test.start()