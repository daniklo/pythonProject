import os
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import  smtplib

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email,attachment_path):
    from_email = "daniklo0110@gmail.com"
    password = "oiqy phqb hlun kexb"

    # הגדרת הודעת המייל
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ", ".join(to)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))




    if attachment_path:
        filename = os.path.basename(attachment_path)
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase('text', 'plain')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={filename}'
            )
            msg.attach(part)

    # חיבור לשרת ה-SMTP של Gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)

    # שליחת המייל
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)

    # סגירת החיבור לשרת
    server.quit()
    print("the mail been sent successfully")

to = "daniklo0110@gmail.com"
# שימוש בפונקציה לשליחת מייל
send_email("my test result",
           "This is the result of the test today",
           to,
           r"C:\my_file.txt")



# def send_email(subject, body, to) :
#     sender = 'daniklo0110@gmail.com'
#     pas = 'Dani1982levy'
#     smtp_server = 'smtp.gmail.com'
#     smtp_port = 587
#
#     msg = MIMEMultipart()
#     msg['From'] = sender
#     msg['To'] =to
#     msg['Subject'] = subject
#     msg.attach(MIMEText(body,'plain'))
#
#     try :
#          with smtplib.SMTP(smtp_server,smtp_port) as server :
#              server.starttls()
#              server.login(sender,pas)
#              text = msg.as_string()
#              server.sendmail(sender,to,text)
#          print("email send")
#     except Exception as e :
#         print(f"fail + {e}")
#
#
# send_email("test sub","text body","daniklo0110@gmail.com")


# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://simania.co.il/")








input("press any key to close ")








# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get("https://danielauto.net/practice/usefull/useful1.html")
