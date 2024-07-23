import allure
import pytest
from selenium import webdriver

# driver = None

# def pytest_exception_interact(report):
#     if report.failed:
#         global driver
#         allure.attach(body=driver.get_screenshot_as_png(), name="screenshot",
#         attachment_type=allure.attachment_type.PNG)

# @pytest.fixture (scope="session",autouse=True)
# def set_up():
#     global driver
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     yield driver
#     driver.quit()


