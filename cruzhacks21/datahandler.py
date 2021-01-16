import pandas as pd
# General syntax to import a library but no functions:
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import openpyxl
import csv
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
class datahandler:

    def __init__(self, df):
        self.df = df


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
data = [job1,job2]


# Create the pandas DataFrame
dataFrame = pd.DataFrame(data, columns=['Company Name',
                                       'Location', 'Job Title', 'Seniority Level', 'Employment Type'])
dh = datahandler(dataFrame)
dh.addNewJob(job3)
# print dataframe
print(dh.df)
# Export dataframe to csv file
dataFrame.to_csv('jobApps.txt', index=False)
# Export dataframe to excel file
dataFrame.to_excel("output.xlsx")
