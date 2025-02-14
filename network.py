import requests
class Network:
    initialize = False
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.initialize:
            cls.initialize = True
            cls.instance = super().__new__(cls)
        return cls.instance


    def __init__(self,url,typeRequest='get',data=0,header="{"auth":""}",allow_headers=True,timeout=5):
        self.url=url
        self.typeRequest=typeRequest
        self.data=data
        self.header=header
        self.aheaders=allow_headers
        self.timeout=timeout
        self.__typeR()
       


    def __get(self):
        """function to send the get request to the server"""
        try:
            datas=requests.get(self.url,allow_redirects=self.header,timeout=self.timeout,headers=self.header)
            if(datas.status_code==200):
                self.fdata=datas.json()
            print(self.fdata)
            datas.raise_for_status()
        # exception catch if any    
        except requests.exceptions.ConnectionError:
            print("connection error ! Really sahi dalo")
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error he sahi se daal: {e}")
        except requests.exceptions.Timeout as e:
            print(f"Timeout error he sahi se daalo na: {e}")            
        except requests.exceptions.RequestException as e:
            print(f"A request error: {e}")
        except Exception as e:
            print(e)    


    def __typeR(self):
        """Function to check the type of the request and raise the exception """
        try:
            if self.typeRequest.lower()=='get':
                self.__get()
            else:
                raise Exception("Your request type is not correct")
        except Exception as e:
            print(e)

urlinput=input("Enter url")
userRequest=Network(urlinput)

