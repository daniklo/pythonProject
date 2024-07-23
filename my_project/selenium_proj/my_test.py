import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
#
#
#
@pytest.fixture (scope="session")
def set_up():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://danielauto.net/practice/loginPage/loginpageTest.html")


    yield
    driver.quit()

# def test_as1(set_up):
#     driver.get("https://www.google.co.il/")
#     element = driver.find_element(By.NAME,'q')
#     assert element.is_displayed()
#
# def add(x, y=0):
#     return x+y
# def subtract(x, y=0):
#     return x-y
# def mul(x, y=0):
#     return x*y

# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get("https://www.google.co.il/")

def login():
    driver.find_element(By.ID,"uaertName").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("adminשש")
    driver.find_element(By.ID, "send").click()
    time.sleep(2)
    try:
        element = driver.find_element(By.ID, "err")
        assert not element.is_displayed(), "Element is displayed"
    except NoSuchElementException:
        # If the element is not found, this is the desired outcome
        pass

def check_status():
    h1 = driver.find_element(By.TAG_NAME,'h1')
    assert h1.get_attribute("align")=="center"

def inp() :
    input("x")

@pytest.mark.dependency()
def test_as1(set_up):
    inp()
    login()

@pytest.mark.dependency(depends=["test_as1"])
def test_as2(set_up):
    check_status()


# def test_as3(set_up): # האם האלמנט נמצא במקום מסוים
#     element = driver.find_element(By.XPATH, '//img[@alt=\"Google\"]')
#     assert element.location == {'x': 824, 'y': 258}

# def test_as4(): # האם האלמנט בגודל מסוים
#     element = driver.find_element(By.XPATH, '//img[@alt=\"Google\"]')
#     assert element.size == {'height': 92.0, 'width': 272.0}

#
# @pytest.mark.skip
# def test_mul():
#     print("some print from the test function")
#     assert mul(2, 2) == 6
#
# @pytest.mark.skip
# def test_subtract():
#    assert subtract(5, 2) == 3
#
# def multNum(x) :
#     return x * 2
#
# def test_ex1(input, excected) :
#     assert multNum(input)
#
