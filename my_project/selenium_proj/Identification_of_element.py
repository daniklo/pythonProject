from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time




# # יצירת דרייבר חדש לפייתון
driver = webdriver.Chrome()
driver.maximize_window()
#
# # תרגיל 1
driver.get("https://stackoverflow.com/tags")
time.sleep(3)

tags = driver.find_elements(By.XPATH, "//a[@rel='tag']")
questions = driver.find_elements(By.XPATH, "//div[contains(@class,'mt-auto')]//div[contains(.,'questions')]")

for i in range(len(tags)):

    print("in " + tags[i].text + " We have " + questions[i].text)

# תרגיל 2
# try:
#     driver.get("https://www.albar.co.il/רכבים-מכירת-רכב/")
#     driver.implicitly_wait(10)
#     pageNum = 1
#     first = True
#     co = 0
#
#     for  x in range (2) :
#     #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='tabpanel tabpanel-mimun panel-large']//bdi[not(ancestor::section[@class='more-offers'])]")))
#         time.sleep(2)
#         list = driver.find_elements(By.XPATH, "//div[@class='row']/div[1]//span[@class='carDetailsContt']")
#         list_name = driver.find_elements(By.CSS_SELECTOR,".CarNamee")
#         counter = len(list)
#
#         c = counter-6
#         for i in range((c),(len(list)),1):
#
#             print(list[co].text , list_name[co].text, co)
#             co +=1
#
#         time.sleep(2)
#         driver.find_element(By.CLASS_NAME, "loadMore").click()
#
# except Exception  as e:
#     # סגירת דרייבר
#     #driver.quit()
#     print(e)
#     input("press x")

input("press x")























