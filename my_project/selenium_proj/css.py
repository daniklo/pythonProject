import csv
import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get("http://danielauto.net/practice/loginPage/loginpageTest.html")
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.b144.co.il/%D7%9E%D7%9C%D7%95%D7%A0%D7%95%D7%AA/%D7%9E%D7%93%D7%A8%D7%99%D7%9A/%D7%94%D7%92%D7%99%D7%A2-%D7%94%D7%96%D7%9E%D7%9F-%D7%9C%D7%A0%D7%A4%D7%95%D7%A9-7-%D7%98%D7%99%D7%A4%D7%99%D7%9D-%D7%9C%D7%97%D7%99%D7%A4%D7%95%D7%A9-%D7%97%D7%95%D7%A4%D7%A9%D7%94-%D7%91%D7%90%D7%99%D7%A0%D7%98%D7%A8%D7%A0%D7%98/");



def test_f1():

   logo = driver.find_element(By.ID, "logoB144")
   w = logo.size['width']
   h = logo.size['height']
   # print(f"{w} ** {h}")
   assert w == 40 and h == 40



def test_f2():
  title = driver.find_element(By.TAG_NAME, "h1")
  assert title.value_of_css_property("font-size") == "32px"




def test_f3():
  title = driver.find_element(By.XPATH, "//div[@class='ArticlePage_readingTime__uQPbY']/span")
  print(title.value_of_css_property("color"))
  assert title.value_of_css_property("color") == "rgba(22, 37, 79, 1)"

def test_f4():
  icon =  driver.find_element(By.XPATH, "//button//img[@class='menuIcon']")
  location = icon.location
  assert location['x'] == 19
  assert location['y'] == 11


def test_f5():

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@id=\"FirstEx\"]//iframe")))

    driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@id=\"FirstEx\"]//iframe"))
    titles = driver.find_elements(By.XPATH, "//div[@class='line-container']//p")
    errors = []
    for title in titles:
        try:
            assert title.value_of_css_property("font-weight") == "701", title.text + " not good"
        except AssertionError as e:
            errors.append(str(e))

    if errors:
        pytest.fail("Errors occurred:\n" + "\n".join(errors))







