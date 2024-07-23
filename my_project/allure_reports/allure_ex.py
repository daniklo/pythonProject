import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By





#מידע חינוכי
@allure.suite("info")
@allure.description("link 1 under info")
def test_info_link1(set_up):
    driver = set_up
    element = driver.find_element(By.XPATH, "//span[text()=\"מידע חינוכי\"]")
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    time.sleep(2)
    element2 = driver.find_element(By.XPATH, "//div[@class=\"whiteBox boxshadow\"]//a[contains(@href,\"rama\")]")
    element2.click()
    time.sleep(2)
    assert driver.title == "דוחות ראמ\"ה"


@pytest.mark.skip
@allure.suite("info")
@allure.description("link 2 under info")
def test_info_link2(set_up):
    driver=set_up
    element = driver.find_element(By.XPATH, "//span[text()=\"מידע חינוכי\"]")
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    time.sleep(2)
    element2 = driver.find_element(By.XPATH, "//div[@class=\"whiteBox boxshadow\"]//a[contains(@href,\"educational-programs\")]")
    element2.click()
    time.sleep(2)
    assert driver.title == "מאגר התוכניות והמענים החינוכיים"

@pytest.mark.skip
@allure.suite("info")
@allure.description("link 3 under info")
def test_info_link3(set_up):
    driver = set_up
    element = driver.find_element(By.XPATH, "//span[text()=\"מידע חינוכי\"]")
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    time.sleep(2)
    element2 = driver.find_element(By.XPATH, "//div[@class=\"whiteBox boxshadow\"]//a[contains(@href,\"digital-learning\")]")
    element2.click()
    time.sleep(2)
    assert driver.title == "למידה דיגיטלית"

@pytest.mark.skip
#קולות קוראים
@allure.suite("voices")
@allure.description("link 1 under voices")
def test_voices_link1(set_up):
    driver = set_up
    element = driver.find_element(By.XPATH, "//span[text()=\"קולות קוראים\"]")
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    time.sleep(2)
    element2 = driver.find_element(By.XPATH, "//div[@class=\"whiteBox boxshadow\"]//a[contains(@href,\"kolkore\")]")
    element2.click()
    time.sleep(2)
    assert driver.title == "רשימת קולות קוראים"


@allure.suite("voices")
@allure.description("link 2 under voices")
def test_voices_link2(set_up):
    driver = set_up
    element = driver.find_element(By.XPATH, "//span[text()=\"קולות קוראים\"]")
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    time.sleep(2)
    element2 = driver.find_element(By.XPATH, "//div[@class=\"whiteBox boxshadow\"]//a[contains(@href,\"textbooks-borrowing\")]")
    element2.click()
    time.sleep(2)
    assert driver.title == "השאלת ספרי לימוד טעות מכוונת"


@pytest.mark.skip
@allure.suite("voices")
@allure.description("link 3 under voices")
def test_voices_link3(set_up):
    driver = set_up
    element = driver.find_element(By.XPATH, "//span[text()=\"קולות קוראים\"]")
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    time.sleep(2)
    element2 = driver.find_element(By.XPATH, "//div[@class=\"whiteBox boxshadow\"]//a[contains(@href,\"summer-school\")]")
    element2.click()
    time.sleep(2)
    assert driver.title == "גנים ובתי ספר של החופש הגדול"



