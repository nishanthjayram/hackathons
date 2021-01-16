"""
    Class implementation for handling and organizing data obtained from scraping. Data
    can then be exported to an output file (CSV/Excel spreadsheet).

    Author  :   Nishanth Jayram (https://github.com/njayram44)
                Sean Touchstone (https://github.com/seant001)
                Jay Wei         (https://github.com/Jay1020431)
    Date    :   January 16, 2021
"""

import pandas as pd
import openpyxl
import csv
class DataHandler:
    """Default constructor for initializing dataframe"""
    def __init__(self, data):
        self.df = pd.DataFrame(data, columns=[
            'Company Name', 'Location', 'Job Title', 'Seniority Level', 'Employment Type'
            ])
    
    """Add new job to the database."""
    def addNewJob(self, job):
        new_df = pd.DataFrame([job], columns = ['Company Name',
                                             'Location', 'Job Title','Seniority Level', 'Employment Type'])
        self.df = self.df.append(new_df, ignore_index=True)

def test(input):
    print(input)

# Debugging procedures
def main():
    #'Company Name','Location', 'Job Title', 'Seniority Level', 'Employment Type'
    job1 = ['Apple', 'Cupertino', 'Software Enigneer 2', 'Manager', 'Full-Time']
    # job2 = ['Tesla', 'Fremont', 'Software Enigneer 3', 'Associate', 'Full-Time']
    # job3 = ['Amazon', 'Seattle', 'Hardware Engineer 3', 'Manager', 'Full-time']
    # job4 = ['Boeing', 'Seattle', 'Hardware Engineer 1', 'Associate', 'Full-time']
    # dataList = [job1, job2, job3]

    # # Create the pandas DataFrame
    # dh = DataHandler(dataList)
    # print(dh.df) # Print dataframe
    # dh.addNewJob(job4) # Add new row, then print again
    # print(dh.df)

    # # Export dataframe to CSV file
    # dh.df.to_csv('jobApps.txt', index=False)
    
    # # Export dataframe to Excel file
    # dh.df.to_excel("output.xlsx")
