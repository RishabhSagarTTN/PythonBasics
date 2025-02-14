import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
class Email:
  def __init__(self,jobs,picture,attachmentfiles):
    self.dic=[]
    self.jobs=jobs
    self.picture=picture
    self.attachmentfiles=attachmentfiles
    self.main() # call the main function to connect with the mail


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
            if len(imagename)==0 and self.picture==True:#check for the image file only
                continue
            if len(attachment)==0 and self.attachmentfiles==True:# check for the attachment
                continue        
            nattachment=len(attachment) 

            messaged=self.service.users().messages().get(userId="me", id=data).execute()['snippet']
            subject=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][21]["value"]           
            # this part will run for job filter and also run if job filter is not choosen means
            #for the attachment and the image file
            if self.attachmentfiles==True or self.picture==True or ('hell' in subject) or ('hell' in messaged):
                date=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][18]["value"]
                fromemail=self.service.users().messages().get(userId="me", id=data).execute()["payload"]["headers"][17]["value"]
                nwords=len(messaged.split())
                nline=len(messaged.split('\n'))
                
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
        self.retrival() 
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")

    
try: # put it in the try block so that if the user doesnt give numberic value it will catch
    selection=int(input("Please select from the following option - 1.Job\n 2.Attachment\n 3.Image files only\n"))
    print("Please wait while it being retrieved\n")
    if selection == 1:
        Email(True,False,False)
    elif selection == 2:
        Email(False,False,True)
    elif selection ==3:
        Email(False,True,False) 
    print("Completed please open the Email.json file to see the output \U0001f600")    
except ValueError as e:
    print(e)           