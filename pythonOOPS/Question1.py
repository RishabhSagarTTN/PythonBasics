import os.path
import pickle
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
class Email:
    def __init__(self):
        self.dic=[]
        self.__connection()
    
    def emaildata(self):
        #check all the attachment in the specific mail 
       for i in self.ids:
            data=i['id']
            attachment=[]
            a_list=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["parts"]
            for i in a_list:        
                temp=i["filename"]
                if temp == '':
                    continue
                attachment.append(temp)
            if len(attachment)==0: # filter the mail if the attachment is not present
                continue    
            self.__storeEmail(attachment,data)


    def __storeEmail(self,attachment,data):
        """it will make the dictionary and store it into the email.json for the particular
        email"""
        nattachment=len(attachment) 
        nlineencode=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["parts"][0]["parts"][0]["body"]["data"]
        nlinedecode=base64.b64decode(nlineencode).decode('utf-8')
        nlinelist= nlinedecode.splitlines()
        nline = len(nlinelist)
        messaged=self.service.users().messages().get(userId="me", id=data).execute()['snippet']
        subject=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][21]["value"]
        date=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][18]["value"]
        fromemail=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][17]["value"]
        nwords=len(messaged.split())
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
          
        with open("Email.json", "w") as file:
            json.dump(self.dic, file, indent=4)     


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
            # calling the function to retrive the data
            self.emaildata()
        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f"An error occurred: {error}")

    


    
try: # put it in the try block so that if the user doesnt give numberic value it will catch
    
    print("Please wait while it being retrieved \U0001f600\n")
    emaildata=Email()
    print("---------Completed please open the Email.json file to see the output \U0001f600---------")    
except ValueError as e:
    print(e)