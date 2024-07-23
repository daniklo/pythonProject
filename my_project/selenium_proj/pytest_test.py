import time

import allure
import pytest
from selenium.webdriver import Keys

from conftest import  *
from selenium import webdriver
from selenium.webdriver.common.by import By

Shufersal = 0
quick = 0
priceRami = 0
#תרגיל 1
def gimatrya(letter) :
    gematria_dict = {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
        'י': 10, 'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40, 'נ': 50, 'ן': 50,
        'ס': 60, 'ע': 70, 'פ': 80, 'ף': 80, 'צ': 90, 'ץ': 90, 'ק': 100, 'ר': 200,
        'ש': 300, 'ת': 400
    }
    return gematria_dict.get(letter, 0)

# def test_letter1 ():
#     print("5/0")
#     assert gimatrya("א")==1
#
#
# def test_letter2 ():
#
#     assert gimatrya("ב")==3
#
#
# def test_letter3 ():
#     assert gimatrya("מ")==50
# def test_letter4 ():
#     assert gimatrya("ר")==200

#תרגיל 2

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.g1
def test_letter1 ():
    assert gimatrya("א")==1
@pytest.mark.g1
def test_letter2 ():
    assert gimatrya("ד")==4
@pytest.mark.g2
def test_letter3 ():
    assert gimatrya("מ")==50
@pytest.mark.g2
def test_letter4 ():
    assert gimatrya("ר")==200


#פקודת הרצה
# pytest pytest_test.py -v -m "g1"

#תרגיל 3
# @pytest.mark.parametrize("letter,result", [("ג",3), ("ק",100) , ("צ",20),("ע",70)])
# def test_letter_param (letter,result):
#     assert gimatrya(letter)==result

"""

#תרגיל 4

def test_Shufersal(set_up) :
    driver = set_up
    driver.get("https://www.shufersal.co.il/online/he/")
    driver.find_element(By.ID,"js-site-search-input").send_keys("שניצל תירס טבעול")
    driver.find_element(By.XPATH,"//button[@class=\"btnSubmit js_search_button\"]").click()
    time.sleep(1)
    price =  driver.find_element(By.XPATH,"//li[@class='SEARCH tileBlock miglog-prod miglog-sellingmethod-by_unit'][1]//span[@class='number'][1]").text
    price = price.replace("₪", "")
    price = price.strip()
    print(price)
    global Shufersal
    Shufersal = float(price)
    print(f"The price in Shufersal is {Shufersal}")


def test_ramiLevy(set_up) :
    driver = set_up
    driver.get("https://www.rami-levy.co.il/he/shop")
    driver.find_element(By.ID,"destination").send_keys("שניצל תירס טבעול" + Keys.ENTER)
    time.sleep(3)

    price_a = driver.find_element(By.CSS_SELECTOR,"#product-7290000536743 span[data-v-be4bebca] > span").text.replace("₪","").strip()

    print(price_a, "**")

    #price = int(price_a) + int((price_b/100))
    global priceRami
    priceRami = float(price_a)
    print(f"The price in Rami Levy is {priceRami}")


def test_quik(set_up) :
    driver = set_up
    driver.get("https://quik.co.il/")
    driver.find_element(By.XPATH,"//input[@type]").send_keys( "שניצל תירס טבעול" + Keys.ENTER)
    time.sleep(1)
    #driver.find_element(By.CSS_SELECTOR,".no-design.icon.dark").click()
    time.sleep(5)
    price = driver.find_element(By.XPATH,"//*[@class=\"item  product\"][1]//span[@class=\"price\"]").text.replace("₪","").strip()

    global quick
    quick = float(price)
    print(f"The price in City Shok is {quick} ")

def test_comper():

    print(Shufersal,"**",priceRami, "***", quick)
    if (Shufersal < priceRami and Shufersal < quick) :
        print("Shufersal is the cheepest!")
    elif (priceRami < Shufersal and priceRami < quick) :
        print("Rami Levy is the cheepest!")
    elif (quick < priceRami and quick < Shufersal) :
        print("Bitan Wines is the cheepest!")

    elif (Shufersal == priceRami) :
        if (Shufersal < quick) :
            print("Shufersal and Rami Levy cheepest ")

    elif (Shufersal == quick) :
            if (Shufersal < priceRami) :
                print("Shufersal and quick cheepest ")

    elif (quick == priceRami) :
        if (quick < Shufersal) :
            print("quick  and Rami Levy cheepest ")


    elif (quick == priceRami and Shufersal == quick ) :
        print("Everything is super pricy!")

"""
