import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://danielauto.net/practice/usefull/useful1.html")


#   1 - הקפצת אלרט
#driver.execute_script("alert('Hello JavaScript!');")

# 2 לחיצה על אלמנט
#driver.execute_script("document.getElementById('NewTab').click();")

# 3 לחיצה כאשר הזיהוי נעשה בנפרד
#element = driver.find_element(By.ID, "NewTab")
#driver.execute_script("arguments[0].click();", element)

"""
#4  - ניווט בין דפים קדימה ואחורה
driver.get("https://www.google.co.il/")
driver.get("https://www.microsoft.com/he-il")
driver.get("https://github.com/")

#חזרה 2 אחורה אל גוגל
driver.execute_script("history.go(-2)")
time.sleep(2)
# מעבר אחד קדימה אל מיקרוסופט
driver.execute_script("history.go(1)")
time.sleep(2)
#ריפרש במיקורוסופט
driver.execute_script("history.go(0)")

"""
# 5 -גלילה של אלמנט

# element = driver.find_element(By.ID,"myInput")
# driver.execute_script("arguments[0].scrollIntoView(true);", element)

# 6 גלילה על ידי פיקסלים

#driver.execute_script("window.scrollBy(0,8000)", "")

# 7 הפעלת פעולת on click

#driver.switch_to.frame(driver.find_element(By.ID,"frame"))
#driver.execute_script("myFunction()")

# ביטל ההשהיה של ה20 שניות
#driver.execute_script("document.getElementById('showTime').style.display = \"block\";")

#driver.save_screenshot(r"d:\image222.png")




# הדגשת פעולות בצבע
def click(element) :
    for x in range(3) :
        driver.execute_script("arguments[0].style.border='3px solid red'", element)
        time.sleep(0.5)
        driver.execute_script("arguments[0].style.border=''", element)
    element.click()

def use_js_type(element, js_code, text) :
    for x in range(3) :
        driver.execute_script("arguments[0].style.border='3px solid red'", element)
        time.sleep(0.5)
        driver.execute_script("arguments[0].style.border=''", element)

    driver.execute_script(js_code, element, text)

def use_js_action(element,js_code) :
    for x in range(3) :
        driver.execute_script("arguments[0].style.border='3px solid red'", element)
        time.sleep(0.5)
        driver.execute_script("arguments[0].style.border=''", element)

    driver.execute_script(js_code)


click(driver.find_element(By.ID,"alert1"))
driver.switch_to.alert.dismiss()
click(driver.find_element(By.ID,"alert2"))
driver.switch_to.alert.dismiss()
click(driver.find_element(By.ID,"alert3"))
driver.switch_to.alert.dismiss()


""""
#תרגיל במצגת
driver.get("https://danielauto.net/practice/loginPage/loginpageTest.html ")
user = driver.find_element(By.ID,"uaertName")
password = driver.find_element(By.ID,"password")
btn = driver.find_element(By.ID,"send")

use_js_type(user,"arguments[0].value = arguments[1];","admin")
use_js_type(password,"arguments[0].value = arguments[1];", "pass2")
use_js_action(btn,"myFunction()")

"""
input("x ")