# from PyTest.conftest import *


import pdb
import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="session")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(r'--load-extension=C:\Users\ofir\Documents\1.58')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    # chrome_options.add_argument("--window-size=1220,1080")
    # chrome_options.add_argument('--headless')
    yield driver
    driver.quit()


def test_shofersal(driver):
    driver.get("https://www.shufersal.co.il/online/he/")
    driver.implicitly_wait(10)
    search = driver.find_element(By.ID, "js-site-search-input")
    search.send_keys("שניצל תירס טבעול")
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    price = driver.find_element(By.XPATH,"//*[@data-product-code='P_300900']//following-sibling::div//span[@class='number']").text
    global prices
    prices['shofersal'] = float(price)


# @pytest.mark.skip()
def test_ramilevi(driver):
    driver.get("https://www.rami-levy.co.il/he/online/market")
    driver.implicitly_wait(10)
    search = driver.find_element(By.ID, "destination")
    search.send_keys("שניצל תירס טבעול")
    search.send_keys(Keys.ENTER)
    time.sleep(5)
    price2 = driver.find_element(By.XPATH,"//div[@id='product-8445291373921']/div[2]/div[1]/div[1]/span[1]/span[1]").text
    price2 = price2.replace("₪","")
    global prices
    prices['ramilevi'] = float(price2)


def test_quik(driver):
    driver.get("https://www.quik.co.il/")
    driver.implicitly_wait(10)
    search = driver.find_element(By.XPATH, "//input[@type='search']")
    search.send_keys("שניצל תירס טבעול")
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    price3 = driver.find_element(By.XPATH, "//*[@class=\"item  product\"][1]//span[@class=\"price\"]").text
    price3 = price3.replace("₪","")
    global prices
    prices['quik'] = float(price3)


prices = {
    "shofersal": 10,
    "ramilevi":7,
    "quik": 10
}

def test_finder():
    min_price = min(prices.values())
    min_stores = [key for key, price in prices.items() if price == min_price]
    print(f"The lowest price found in {' and in ' .join(min_stores)} store and costs {min_price} ₪ ")
#דניאל תנסה להריץ את הפונקציה האחרונה לבד כדי לראות איך כל הסופרים רצים יחדיו עם המחיר 10 ולא מה שמתקבל מהריצה






# בהתתחלה כתבתי את זה ככה אבל ראיתי שאתה הכנסת גם יינות ביתן וזה לא הגיוני ואם ארצה להוסיף עוד כמב רשתות זה יהפוך לקוד ארוך ומסורבל מדי
# זה כרגע לא יעבוד כי הטסטים בסוף מעבירים לעדכון של  ה dictionary

# shofersal = 0
# ramilevi = 0
# quik = 0
# def test_finder():
#     global shofersal, ramilevi, quik
#     if shofersal < ramilevi and shofersal < quik:
#         print(f"המחיר הכי זול נמצא בשופרסל ועולה {shofersal}")
#     elif ramilevi < shofersal and ramilevi < quik:
#         print(f"המחיר הכי זול נמצא ברמי לוי ועולה {ramilevi}")
#     elif quik < shofersal and quik < ramilevi:
#         print(f"המחיר הכי זול נמצא בקוויק ועולה {quik}")
#     elif shofersal == ramilevi and shofersal < quik:
#         print(f"המחיר הכי זול נמצא בשופרסל וברמי לוי ועולה {shofersal}")
#     elif shofersal == quik and shofersal < ramilevi:
#         print(f"המחיר הכי זול נמצא בשופרסל ובקוויק ועולה {shofersal}")
#     elif ramilevi == quik and ramilevi < shofersal:
#         print(f"המחיר הכי זול נמצא ברמי לוי ובקוויק ועולה {ramilevi}")
#     elif shofersal == ramilevi and shofersal == quik:
#         print(f"המחיר הכי זול נמצא בשופרסל, רמי לוי וקוויק ועולה {shofersal}")














