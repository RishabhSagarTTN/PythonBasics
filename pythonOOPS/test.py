# In download email assingment,

# Provision to download only selective email. For example:

# - To download only emails wich have attachements
# - To download only email which are related to Job
# - To download only the email which have picture attached
# VIEW LESS



import os.path
import pickle
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
    self.main()
  def job(self):
      for i in self.ids:
            data=i['id']
            attachment=[]
            a_list=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["parts"]
            for i in a_list:        
                temp=i["filename"]
                if temp == '':
                    continue
                attachment.append(temp)
               

            nattachment=len(attachment) 
            messaged=self.service.users().messages().get(userId="me", id=data).execute()['snippet']
            subject=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][21]["value"]
            if 'job' in subject or 'job' in messaged:
                print(messaged,subject)
                
            
                date=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][18]["value"]
                fromemail=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][17]["value"]
                nwords=len(messaged.split())
                nline=len(messaged.split('\n'))
                
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
                             
  def picture(self):
      for i in self.ids:
            data=i['id']
            attachment=[]
            imagename=[]
            a_list=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["parts"]
            for i in a_list:        
                temp=i["filename"]
                imageType=i['mimeType']
                if temp == '':
                    continue
                attachment.append(temp)
                if imageType.startswith("image"):
                    imagename.append(temp)
            if len(imagename)==0:
                continue    
            nattachment=len(attachment) 
            messaged=self.service.users().messages().get(userId="me", id=data).execute()['snippet']
            subject=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][21]["value"]
            date=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][18]["value"]
            fromemail=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][17]["value"]
            nwords=len(messaged.split())
            nline=len(messaged.split('\n'))
            
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
              
  def emaildata(self):
       count=0
       for i in self.ids:
            data=i['id']
            attachment=[]
            a_list=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["parts"]
            for i in a_list:        
                temp=i["filename"]
                if temp == '':
                    continue
                attachment.append(temp)
            if len(attachment)==0:
                continue    
            print(self.service.users().messages().get(userId="me", id=data).execute())
            nattachment=len(attachment) 
            messaged=self.service.users().messages().get(userId="me", id=data).execute()['snippet']
            subject=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][21]["value"]
            date=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][18]["value"]
            fromemail=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][17]["value"]
            nwords=len(messaged.split())
            nline=len(messaged.split('\n'))
            
            temp={
                "date":date,
                "fromemail":fromemail,
                "subject":subject,
                "message":messaged,
                "Number of words":nwords,
                "Number of line":nline,
                "Number of attachment":nattachment,
                "File Name":attachment
            }
            self.dic.append(temp)
          
            with open("Email.json", "w") as file:
                json.dump(self.dic, file, indent=4)         



  def main(self):
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
        # self.emaildata()
        self.job()
        # self.picture()
        # self.emaildata()#attachment
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")

    


emaildata=Email()