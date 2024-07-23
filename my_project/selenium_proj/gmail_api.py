import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time





def test1(set_up):
    driver = set_up
    username = "username"
    password = "password"
    driver.get("http://omayo.blogspot.com/search")
    driver.find_element(By.NAME, "userid").send_keys(username)
    driver.find_element(By.NAME, "pswrd").send_keys(password)
    driver.find_element(By.XPATH, "//input[@value=\"Login\"]").click()

    alert_text = driver.switch_to.alert.text

    with open("filename.txt", "a", encoding="utf-8") as out:
        out.write(f"בבדיקה של שם משתמש {username} וסיסמא {password} התקבלה הודעה {alert_text}\n")

    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)


def test2(set_up):
    driver = set_up
    driver.find_element(By.NAME, "userid").clear()
    driver.find_element(By.NAME, "pswrd").clear()

    driver.find_element(By.NAME, "userid").send_keys("333")
    driver.find_element(By.NAME, "pswrd").send_keys("333")

    time.sleep(1)

    user_txt = driver.find_element(By.NAME, "userid").get_attribute("value")
    pass_txt = driver.find_element(By.NAME, "pswrd").get_attribute("value")

    if user_txt == "333" and pass_txt == "333":
        driver.find_element(By.CSS_SELECTOR, "input[type='reset']").click()

        time.sleep(1)

        user_cancel = driver.find_element(By.NAME, "userid").get_attribute("value")
        pass_cancel = driver.find_element(By.NAME, "pswrd").get_attribute("value")

        if not user_cancel and not pass_cancel:
            with open("filename.txt", "a", encoding="utf-8") as out:
                out.write("בלחיצה על Cancel השדות טקסט נמחקו\n")
        else:
            with open("filename.txt", "a", encoding="utf-8") as out:
                out.write("בלחיצה על Cancel השדות טקסט לא נמחקו\n")
    else:
        with open("filename.txt", "a", encoding="utf-8") as out:
            out.write("הטקסט 333 לא נכתב בשדות\n")


def test3(set_up):
    driver= set_up
    driver.find_element(By.NAME, "userid").send_keys("SeleniumByArun")
    driver.find_element(By.NAME, "pswrd").send_keys("Test143$")
    driver.find_element(By.XPATH, '//input[@value=\"Login\"]').click()

    time.sleep(3)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    time.sleep(3)
    id_attr = driver.find_element(By.ID, "Header1_headerimg").get_attribute("id")
    with open("filename.txt", "a", encoding="utf-8") as out:
        out.write(f"{id_attr}\n")

    time.sleep(1)

def test4(set_up):
    from_email = "daniklo0110@gmail.com"
    password = "oiqy phqb hlun kexb"
    to_email = "daniklo0110@gmail.com"

    # הגדרת הודעת המייל
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ", ".join(to_email)
    msg['Subject'] = "login test"
    msg.attach(MIMEText("מצורף קובץ עם תוצאות הבדיקות \n תודה", 'plain'))

    attachment_path = "filename.txt"
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

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)

    # שליחת המייל
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)

    # סגירת החיבור לשרת
    server.quit()
    print("the mail been sent successfully")
