from pandas import DataFrame, read_csv
# General syntax to import a library but no functions:
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import openpyxl
import csv
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
class datahandler:

#Company, Job Title, Job Type, Location, Date Posted, Date Applied, Status
    job1 = ['Apple', 'Software Engineer 2', 'Full-time', 'Santa Cruz', '1/4/2021', '1/6/2021', 'TBA']
    job2 = ['Tesla', 'Software Engineer 3', 'Full-time', 'Fremont', '1/8/2021', '1/14/2021', 'Rejected']
    data = {'Company Name': ['myKaarma'], 'Location': ['Long Beach, CA'], 'Job Title': ['Summer Engineering Intern'],
            'Seniority Level': ['Internship'], 'Employment Type': ['Internship']}

# Create the pandas DataFrame
    df = pd.DataFrame.from_dict(data)
# print dataframe
    print(df)
# Export dataframe to csv file
    df.to_csv('jobApps.txt', index=False)
# Export dataframe to excel file
    df.to_excel("output.xlsx")

    job3= ['Amazon', 'Seattle', 'Hardware Engineer 3', 'Manager', 'Full-time']
    new_df = pd.DataFrame([job3], columns = ['Company Name',
                                             'Location', 'Job Title','Seniority Level', 'Employment Type'])
    print(new_df)
    df = df.append(new_df, ignore_index=True)

    print(df)

