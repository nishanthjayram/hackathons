import pandas as pd
# General syntax to import a library but no functions:
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import openpyxl
import csv
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
import pyrebase
import firebase_admin
from firebase_admin import auth as authen
class datahandler:

    def __init__(self,data):
        self.df = pd.DataFrame(data, columns=['Company Name',
                                       'Location', 'Job Title', 'Seniority Level', 'Employment Type'])


# Add new job to new database
    def addNewJob(self, job):
        new_df = pd.DataFrame([job], columns = ['Company Name',
                                             'Location', 'Job Title','Seniority Level', 'Employment Type'])
        self.df = self.df.append(new_df, ignore_index=True)



#'Company Name','Location', 'Job Title', 'Seniority Level', 'Employment Type'
job1 = ['Apple', 'Cupertino', 'Software Enigneer 2', 'Manager', 'Full-Time']
job2 = ['Tesla', 'Fremont', 'Software Enigneer 3', 'Associate', 'Full-Time']
job3 = ['Amazon', 'Seattle', 'Hardware Engineer 3', 'Manager', 'Full-time']
job4 = ['Boeing', 'Seattle', 'Hardware Engineer 1', 'Associate', 'Full-time']
dataList = [job1,job2,job3]

# Create the pandas DataFrame
dh = datahandler(dataList)
dh.addNewJob(job3)
# print dataframe
print(dh.df)
# Export dataframe to csv file
dh.df.to_csv('jobApps.txt', index=False)
# Export dataframe to excel file
dh.df.to_excel("output.xlsx")

config = {
  "apiKey": "AIzaSyBVQ2tMd1fIGawv-V5Yo7ZUCIFBEY4QjNw",
  "authDomain": "jojoba-internship-tracker.firebaseapp.com",
  "databaseURL": 'https://jojoba-internship-tracker-default-rtdb.firebaseio.com/',
  "storageBucket": "jojoba-internship-tracker.appspot.com"#,
  #"serviceAccount": "C:/jojoba-internship-tracker-firebase-adminsdk-txgdn-0c5ea2f8bb.json"
}

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()
default_app = firebase_admin.initialize_app()

# Log the user in
email = 'seantouchstonejr@gmail.com'
password = 'ShyShy123!'
user = auth.sign_in_with_email_and_password(email, password)

# Log the user in anonymously
#user = auth.sign_in_anonymous()
data = {"name": "Mortimer 'Morty' Smith"}
# Get a reference to the database service
db = firebase.database()
# Pass the user's idToken to the push method
#results = db.child("users").push(job3, user['idToken'])

def addFirebaseJob(job):
    db.child("users").push(job)
addFirebaseJob(data)
db.child("users").child("MRDnuEa2Eq_oh_Uwk3Z").update({"name": "Sean Touchstone Jr"})
#def removeFirebaseJob(job):

