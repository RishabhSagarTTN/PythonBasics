import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json
import base64
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
class Email:
  def __init__(self,jobs,picture,attachmentfiles):
    self.dic=[]
    self.jobs=jobs
    self.picture=picture
    self.attachmentfiles=attachmentfiles
    self.__connection() # call the connection function to connect with the mail
  
  def pictures(self,data,imagename,attachment):
    if len(imagename)==0 and self.picture==True:#check for the image file only
        return
    self.__api(data,attachment)    


  def attachementf(self,data,attachment):
    if len(attachment)==0 and self.attachmentfiles==True:# check for the attachment
        return
    self.__api(data,attachment)


  def job(self,data,attachment):
    messaged=self.service.users().messages().get(userId="me", id=data).execute()['snippet']
    subject=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][21]["value"]
    if ('job' in subject) or ('job' in messaged) or  ('jobs' in subject) or ('jobs' in messaged):
        self.__api(data,attachment)  


  def __api(self,data,attachment):
        """retrive the data from the email and make the temp dictionary to store it 
         in the email.json """
        nattachment=len(attachment) 
        nlineencode=""
        messaged=self.service.users().messages().get(userId="me", id=data).execute()['snippet']
        subject=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][21]["value"]           
        date=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][18]["value"]
        fromemail=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][17]["value"]
        nwords=len(messaged.split())
        if nattachment==0:
            nlineencode=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["parts"][0]["body"]["data"]
        else:
            nlineencode=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["parts"][0]["parts"][0]["body"]["data"]
        nlinedecode=base64.b64decode(nlineencode).decode('utf-8')
        nlinelist= nlinedecode.splitlines()
        nline = len(nlinelist)
                
        #making of the temp dictionary for the specific mail
        temp={ 
            "date":date,
            "fromemail":fromemail,
            "subject":subject,
            "message":messaged,
            "Number of words":nwords,
            "Number of line":nline,
            "Number of attachment":nattachment,
            "File name":attachment
            }
        self.dic.append(temp)
            # dump the dictionary in the email.json file
        with open("Email.json", "w") as file:
            json.dump(self.dic, file, indent=4)  

  def retrival(self):
      """Retrieve the data from the gmail with the give specific option or filter"""
      for i in self.ids:
            data=i['id']
            attachment=[]
            imagename=[]
            a_list=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["parts"]
            #check all the attachment in the specific mail 
            for i in a_list:        
                temp=i["filename"]
                imageType=i['mimeType']
                if temp == '':
                    continue
                attachment.append(temp)
                if imageType.startswith("image"):
                    imagename.append(temp)
            if self.attachmentfiles==True: self.attachementf(data,attachment)
            if self.picture==True: self.pictures(data,imagename,attachment)
            if self.jobs==True:self.job(data,attachment)



  def __connection(self):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        self.service = build("gmail", "v1", credentials=creds)
        self.ids=self.service.users().messages().list(userId="me").execute().get("messages")
        # function to retrive the email from the gmail
        self.retrival() 
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")


    

decision='yes'    
# put it in the try block so that if the user doesnt give numberic value it will catch

while decision=='yes':
    try:    
        decision=str(input("Do you want to continue if yes please enter yes if no please enter no \t"))
        if decision.lower()=='yes':
            selection=int(input("Please select from the following option -------\n 1.Job\n 2.Attachment\n 3.Image files only\n"))
            if selection > 3 or selection <0: raise ValueError("Please enter correct number. Please \U0001f600")
            print("Please wait while it being retrieved \U0001f600\n")
            if selection == 1:
                Email(True,False,False)
            elif selection == 2:
                Email(False,False,True)
            elif selection ==3:
                Email(False,True,False) 
            print("---------Completed please open the Email.json file to see the output \U0001f600---------")
        elif decision.lower()=='no':
            break
        else:
            raise ValueError("You enter the wrong input")

    except ValueError as e:
        print(e)
        decision='yes'