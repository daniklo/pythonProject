import pyautogui

from selenium.webdriver.common.by import By


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.co.il/")

driver.find_element(By.LINK_TEXT,'חיפוש תמונות').click()
driver.find_element(By.NAME,'q').send_keys("hackeru" + Keys.ENTER)
time.sleep(3)

x, y = 440, 440
pyautogui.moveTo(x, y)
pyautogui.rightClick(x, y)
time.sleep(1)
for i in range (7) :
    pyautogui.press('down')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite(r'd:\robot.png', interval=0.05)
pyautogui.press('enter')
input("x ")
