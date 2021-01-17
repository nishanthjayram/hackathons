"""
    Implements functionality to webscrape job information from LinkedIn pages.

    Author  :   Nishanth Jayram (https://github.com/njayram44)
                Sean Touchstone (https://github.com/seant001)
                Jay Wei         (https://github.com/Jay1020431)
    Date    :   January 16, 2021
"""

import smtplib
import datetime
import pandas as pd
from datetime import date, time, timedelta


Reciever_email=input("Enter your email address here: ")

data = pd.read_excel(r"path where the excel file is stored")
print(data)
columns = list(data)
cname = pd.DataFrame(data, columns=["Company Name"])
loc = pd.DataFrame(data, columns=["Location"])
jtitle = pd.DataFrame(data, columns=["Job Title"])
Seniority = pd.DataFrame(data, columns=["Seniority Level"])
type = pd.DataFrame(data, columns=["Employment Type"])
deadline = pd.DataFrame(data, columns=["end_dates"])

deadlines = list(deadline)
for i in range(len(deadlines)):
    days=datetime.timedelta(7)
    notify_date=deadline-days
    today=date.today()
    if(today==notify_date):
        for k in columns:
            server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("JoJobaCruzHacks@gmail.com", "jojobahacks")
            server.sendmail("JoJobaCruzHacks@gmail.com", Reciever_email, "print(data[i][k])", "Ends in 7 days")
            server.quit()
    else:
        i=i+1



