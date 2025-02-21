import csv
import json
import io

class CSVTJSON:
    """class that convert csv to json"""
    def __init__(self,paths):
        self.path=paths
        self.__conversion()

    def __conversion(self):
        """__conversion method convert the csv file to json file"""
        try:
            with open("converted.json",'w') as jsonF:
                with open(self.path,"r") as csvF:
                    # read the csv file as a dictionary
                    data=csv.DictReader(csvF,delimiter=";",quotechar='"', quoting=csv.QUOTE_ALL)
                    temp=[]
                    for i in data:
                        temp.append(i) # making of the json object
                    json.dump(temp,jsonF,indent=3) # dumping the json object into the jsonF file 
            print("Json file is created name converted.json")        
        except Exception as e:
            print(e)               

class JSONTCSV:
    """class to convert the json file into csv"""
    def __init__(self,paths=""):
        self.path=paths
        self.__conversion()

    def __conversion(self):
        """__conversion method convert the json file to csv file"""
        try:
            with open("test.json",'r') as jsonF:
                data=[json.loads(i) for i in jsonF] # read each line from the json and convert it into dictionary and make the list
                headers=list(data[0].keys()) # extracting the header
                with open("test.csv",'w') as file:
                    csvw=csv.writer(file,delimiter=",", quotechar='"',quoting=csv.QUOTE_ALL)
                    csvw.writerow(headers) # making the header of the csv
                    for i in data:# taking each json one by one from the json file
                        temp=[]
                        for j in i.keys():
                            temp.append(str(i[j]))
                        csvw.writerow(temp) # wriring the row in the csv 
                    print("CSV file is created name test.csv")    
        except Exception as e:
            print(e)

def dictTostring(dic):
    """function to make the StringIO string from the dictionary"""
    strings=io.StringIO()
    header=list(dic.keys())
    strings.write(",".join(header)+"\n") # writing the header in the strings
    strings.write(",".join([str(dic[i]) for i in header])) 
    strings.seek(0) # as the pointer will be pointing to the last we go to the first position so that we can read the whole data
    print(strings.read())# reading and printing the string



#----------------------------------------------     
                  
dictTostring( {
      "Username": "booker12",
      " Identifier": "9012",
      "First name": "Rachel",
      "Last name": 0
   })


csv_tojson=CSVTJSON("username.csv")
json_tocsv=JSONTCSV("test.json")

