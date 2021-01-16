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

#'Company Name','Location', 'Job Title', 'Seniority Level', 'Employment Type'
    job1 = ['Apple', 'Cupertino', 'Software Enigneer 2', 'Manager', 'Full-Time']
    job2 = ['Tesla', 'Fremont', 'Software Enigneer 3', 'Associate', 'Full-Time']
    job3 = ['Amazon', 'Seattle', 'Hardware Engineer 3', 'Manager', 'Full-time']
    job4 = ['Boeing', 'Seattle', 'Hardware Engineer 1', 'Associate', 'Full-time']
    data = [job1,job2]

# Create the pandas DataFrame
    df = pd.DataFrame(data, columns=['Company Name',
                                       'Location', 'Job Title', 'Seniority Level', 'Employment Type'])
# print dataframe
    print(df)
# Export dataframe to csv file
    df.to_csv('jobApps.txt', index=False)
# Export dataframe to excel file
    df.to_excel("output.xlsx")

# Add new job to new database
    def addNewJob(job):
        new_df = pd.DataFrame([job], columns = ['Company Name',
                                             'Location', 'Job Title','Seniority Level', 'Employment Type'])
        print(new_df)
        return new_df

    df = df.append(addNewJob(job3), ignore_index=True)
    df = df.append(addNewJob(job4), ignore_index=True)

    print(df)

