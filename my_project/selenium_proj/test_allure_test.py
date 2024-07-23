import os
import sys
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

from my_project.selenium_proj import conftest



@allure.step("login with user : {user} and passowrd : {password}")
def login(driver, user, password) :

    driver.find_element(By.ID,'uaertName').send_keys(user)
    driver.find_element(By.ID, 'password').get_attribute("class")
    driver.find_element(By.ID, 'send').click()
    txt = driver.find_element(By.TAG_NAME,"h1").text


    return txt

#@allure.description("test for search fild in google ")
def test_as3(set_up):
    driver = set_up
    with allure.step("go to url"):
        driver.get("https://danielauto.net/practice/loginPage/loginpageTest.html")
    with allure.step("call to ligin function"):
        txt = login(driver, "admin", "admin")
    with allure.step("assert the msg"):
        assert txt == 'You\'ve logged in'


@allure.severity(allure.severity_level.CRITICAL)
def test_critical():
    assert 1 == 1

@allure.severity(allure.severity_level.NORMAL)
def test_normal():
    assert 1 == 1

@allure.feature("Login Feature")
@allure.story("User tries to log in with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("This test verifies the login functionality with valid credentials")
@allure.issue("JIRA-123")
@allure.link("https://example.com/login")
def test_minor():
    assert 1 == 1

# @allure.description("test for logo location ")
# def test_as3(): # האם האלמנט נמצא במקום מסוים
#     driver = conftest.set_up
#     element = driver.find_element(By.XPATH, '//img[@alt=\"Googl\"]')
#     assert element.location == {'x': 824, 'y': 258}
#
# @allure.description("test for logo size ")
# def test_as4(): # האם האלמנט בגודל מסוים
#     driver = conftest.set_up
#     element = driver.find_element(By.XPATH, '//img[@alt=\"Google\"]')
#     assert element.size == {'height': 92.0, 'width': 272.0}




