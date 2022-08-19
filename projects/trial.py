import numpy as np
import pandas as pd
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

import pandas as pd
import smtplib

SenderAddress = "anupriya14875@gmail.com"
password = "gqmsybpzssouxluz"

e = pd.read_excel("C:/Users/Google/Desktop/projects/Book2.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = "http://127.0.0.1:5000"
subject = "Hello world"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()
