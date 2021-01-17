"""
    Implementation of methods and classes for data management and integration
    with Firebase.

    Author(s)  :  Nishanth Jayram (https://github.com/njayram44)
                  Sean Touchstone (https://github.com/seant001)
                  Jay Wei         (https://github.com/Jay1020431)
    
    Date       :  January 17, 2021
"""
import pandas as pd
import scraper as sc
import openpyxl
import csv
import time
import sys
# import pyrebase
# from firebase_admin import auth as authen

# config = {
#   "apiKey": "AIzaSyBVQ2tMd1fIGawv-V5Yo7ZUCIFBEY4QjNw",
#   "authDomain": "jojoba-internship-tracker.firebaseapp.com",
#   "databaseURL": 'https://jojoba-internship-tracker-default-rtdb.firebaseio.com/',
#   "storageBucket": "jojoba-internship-tracker.appspot.com"#,
#   #"serviceAccount": "C:/jojoba-internship-tracker-firebase-adminsdk-txgdn-0c5ea2f8bb.json"
# }

# firebase = pyrebase.initialize_app(config)

class datahandler:
    def __init__(self,data):
        self.df = pd.DataFrame(data, columns=['Company Name',
                                       'Location', 'Job Title', 'Seniority Level', 'Employment Type'])
        # Get a reference to the database service
        # self.db = firebase.database()

# Add new job to new database
    def addNewJob(self, job):
        new_df = pd.DataFrame([job], columns = ['Company Name',
                                             'Location', 'Job Title','Seniority Level', 'Employment Type'])
        self.df = self.df.append(new_df, ignore_index=True)

# Update and Upload the pandas dataframe to firebase
    # def updateUpload(self):
    #     self.db.child("Jobs").set(self.df.values.tolist())

# Export dataframe to Excel file
    def exportToExcel(self, filename="jobApplications.xlsx"):
        self.df.to_excel(filename)

# Export dataframe to CSV file
    def exportToCSV(self, filename="jobApplications.csv"):
        self.df.to_csv(filename, index=False)

# Get all jobs from database and print
    # def getFirebaseData(self):
    #     return self.db.child("Jobs").get().val()

def main():
    JOB_FILE = sys.argv[1]
    dataList = sc.scraper(JOB_FILE) # Scrape data from pages

    # Create the pandas DataFrame
    dh = datahandler(dataList)
    print(dh.df)

    exportFlag = input("Export to Excel file? (y/n) ")
    if (exportFlag == "y"):
        print("Exporting to jobApplications.xlsx...")
        time.sleep(1)
        dh.exportToExcel()
        print("Export complete")
    elif (exportFlag == "n"):
        print("Thank you, have a great day!")
    else:
        print("Invalid input")

    # # Get a reference to the auth service
    # auth = firebase.auth()
    # default_app = firebase_admin.initialize_app()

    # # Log the user in
    # email = 'seantouchstonejr@gmail.com'
    # password = 'ShyShy123!'
    # user = auth.sign_in_with_email_and_password(email, password)

    # # Log the user in anonymously.
    # #user = auth.sign_in_anonymous()
    # dh.updateUpload()
    # #Get all jobs from database and print
    # print(dh.getFirebaseData())

if __name__ == "__main__":
    main()