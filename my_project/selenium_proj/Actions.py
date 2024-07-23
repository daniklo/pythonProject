from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # פתרון באמצעות לולאה
    driver.get("http://marcojakob.github.io/dart-dnd/basic/")
    list_page = driver.find_elements(By.XPATH, "//img[@class='document']")
    for draggable in list_page:
        droppable = driver.find_element(By.CLASS_NAME, "trash")
        ActionChains(driver).drag_and_drop(draggable, droppable).perform()

except Exception as e:
    print("targil 1 fail")
"""
try:
    # פתרון ללא לולאה

    driver.get("http://marcojakob.github.io/dart-dnd/basic/")
    # נייר 1
    draggable = driver.find_element(By.XPATH, "//img[@class][1]")
    droppable = driver.find_element(By.XPATH, "//div[@class='trash']")
    ActionChains(driver).drag_and_drop(draggable, droppable).perform()

    # נייר 2
    draggable2 = driver.find_element(By.XPATH, "//img[@class][1]")
    droppable2 = driver.find_element(By.XPATH, "/html/body/div/div")
    ActionChains(driver).drag_and_drop(draggable2, droppable2).perform()

    # נייר 3
    draggable3 = driver.find_element(By.XPATH, "//img[@class][1]")
    droppable3 = driver.find_element(By.XPATH, "/html/body/div/div")
    ActionChains(driver).drag_and_drop(draggable3, droppable3).perform()

    # נייר 4
    draggable4 = driver.find_element(By.XPATH, "//img[@class][1]")
    droppable4 = driver.find_element(By.XPATH, "/html/body/div/div")
    ActionChains(driver).drag_and_drop(draggable4, droppable4).perform()
    print("targil 1 pass")
except Exception as e:
    print(f"targil 1 fail {e}" )

# 2.
try:
    driver.get("http://danielauto.net/practice/action/multipick.html")
    list = driver.find_elements(By.CSS_SELECTOR, "SELECT#city *")
    ActionChains(driver).key_down(Keys.SHIFT).click(list[0]).click(list[2]).key_up(Keys.SHIFT).perform()
    time.sleep(1)
    driver.save_screenshot("d:\\failure.png")

    # ActionChains(driver).key_down(Keys.CONTROL).click(list[0]).click(list[1]).click(list[2]).click(list[4]).click(
    #     list[0]).key_up(Keys.CONTROL).perform()
    # time.sleep(1)
    driver.save_screenshot("d:\\failure2.png")
    # print("targil 2 pass")
except Exception as e:
    print(f"targil 2 fail {e}")

# 3.
try:
    driver.get("http://danielauto.net/practice/action/multipick.html")
    double_click_element = driver.find_element(By.ID, "dbl_click")
    ActionChains(driver).double_click(double_click_element).perform()
    time.sleep(2)
    if driver.find_element(By.ID, "demo").text == "הלחיצה על התמונה עברה בהצלחה":
        print("התמונה נלחצה בהצלחה")
    else:
        print("התמונה לא נלחצה")
    print("targil 3 pass")
except Exception as e:
    print(f"targil 3 fail {e}")

# 4.
try:
    driver.get("http://danielauto.net/practice/action/multipick.html")
    builder = ActionChains(driver)
    element = driver.find_element(By.ID, "over")
    builder.move_to_element(element).perform()
    time.sleep(1)
    element1 = driver.find_element(By.ID, "dbl_click")
    builder.move_to_element(element1).perform()
    time.sleep(1)
    builder.move_to_element(element).perform()
    number = driver.find_element(By.ID, "demo2").text
    if number == "2":
        print("המספר 2 מופיע")
    else:
        print("המספר 2 אינו מופיע")
    print("targil 4 pass")
except Exception as e:
    print("targil 4 fail")

# 5.
try:
    driver.get("http://danielauto.net/practice/action/multipick.html")
    time.sleep(3)
    menu = driver.find_element(By.XPATH, "//*[@id='mouseover']/button")
    actions = ActionChains(driver)
    actions.move_to_element(menu).perform()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "ynet").click()

    
    time.sleep(2)
    print(driver.title)
    print("targil 5 pass")
except Exception as e:
    print("targil 5 fail")


#6

try:
    driver.get("http://danielauto.net/practice/action/multipick.html")
    element = driver.find_element(By.ID, "myRange")
    count = 1
    num = int(driver.find_element(By.ID,'progNumber').text)

    while num <= 88 :

        ActionChains(driver).drag_and_drop_by_offset(element,count,0).perform()
        time.sleep(1)
        count-=3
        num = int(driver.find_element(By.ID, 'progNumber').text)
        if num ==88 :
            break



    print("targil 6 pass")
except Exception as e:
    print("targil 6 fail")

7.
try:
    driver.get("http://danielauto.net/practice/action/multipick.html")
    time.sleep(2)
    element = driver.find_element(By.XPATH, "//img[@alt='baby_scroll']")
    #driver.execute_script("arguments[0].scrollIntoView(true);", element)
    ActionChains(driver).move_to_element(element)
    time.sleep(2)
    scr_file2 = driver.save_screenshot("d:\\failure10.png")
    print("targil 6 pass")
except Exception as e:
    print(f"targil 6 fail {e}")


"""

input("press x ")

# משחקים

# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("https://jqueryui.com/slider/#custom-handle")
#
# driver.switch_to.frame(driver.find_element(By.CLASS_NAME,'demo-frame'))
# time.sleep(2)
# element = driver.find_element(By.CSS_SELECTOR,'.ui-slider-handle.ui-corner-all.ui-state-default')
#
# action = ActionChains(driver)
#
# #action.drag_and_drop_by_offset(element,150,0).perform()
#
# count = 0
# num = int(element.text)
# while num < 40 :
#
#     action.drag_and_drop_by_offset(element,count,0).perform()
#     time.sleep(1)
#     count+=0.5
#     num = int(element.text)
#     if num ==40 :
#         break
#
# time.sleep(2)
#
#
# input("press x ")
