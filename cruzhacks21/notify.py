import smtplib
import pandas as pd
import datetime
from datetime import date, time, timedelta

end_date = pd.to_datetime("17th of jan, 2021")
days = datetime.timedelta(1)
notify_date = end_date-days
today=date.today()
if(today == notify_date):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("JoJobaCruzHacks@gmail.com", "jojobahacks")
    server.sendmail("JoJobaCruzHacks@gmail.com", "Ultrafine159487326@gmail.com", "testing")
    server.quit()

