import csv
import time
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://danielauto.net/practice/loginPage/loginpageTest.html")

with open(r'C:\selenium\csv.csv', 'r') as myFile:
    myReader = csv.reader(myFile)
    l = list(myReader)
def locat() :
    us = driver.find_element(By.ID, 'uaertName')
    pas = driver.find_element(By.ID, 'password')
    btn = driver.find_element(By.ID, 'send')
    err = driver.find_element(By.ID, 'err')
    return (us,pas,btn,err)




for i, it in enumerate(l) :
    driver.get("http://danielauto.net/practice/loginPage/loginpageTest.html")
    us, pas, btn, err = locat()
    us.send_keys(it[0])
    pas.send_keys(it[1])
    btn.click()
    time.sleep(1)
    if it[2] == 'FALSE' :
        try:
            err.text
            print(f'line {i} pass')
        except :
            print(f'line {i} fail')

    else:
        try:
            driver.find_element(By.TAG_NAME, 'h1')
            print(f'line {i} pass')
        except :
            print(f'line {i} fail')

