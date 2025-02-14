import requests
class Network:
    initialize=False
    instance=None
    def __new__(cls,*args,**kwargs):
        if cls.initialize==False:
            cls.initialize=True
            cls.instance=super(cls)
            return cls.instance
        else:
            return cls.instance 


    def __init__(self,url,typeRequest='get',data=0,header=""):
        self.url=url
        self.typeRequest=typeRequest
        self.data=data
        self.header=header
        self.__typeR()


    def __get(self):
        """function to send the get request to the server"""
        try:
            datas=requests.get(self.url)
            if(datas.status_code==200):
                self.fdata=datas.json()
                # print(self.fdata)
            else:
                raise Exception("Bad request")
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


userRequest=Network("https://jsonplaceholder.typicode.com/posts")
userRequest1=Network("https://jsonplaceholder.typicode.com/posts")
print(userRequest is userRequest1)


