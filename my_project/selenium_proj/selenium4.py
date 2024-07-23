import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome()
#driver.maximize_window()

#time zone

# driver.get("https://whatismytimezone.com/ ")
# driver.implicitly_wait(10)
# print(driver.find_element(By.XPATH,"//section/article[1]").text)
#
# dev_tools = driver.execute_cdp_cmd('Page.enable', {})
# driver.execute_cdp_cmd('Emulation.setTimezoneOverride', {
#     'timezoneId': 'America/Denver'
# })
# driver.refresh()
# driver.implicitly_wait(10)
# print(driver.find_element(By.XPATH,"//section/article[1]").text)

#location

# driver.get("https://where-am-i.org/")
#
# driver.implicitly_wait(10)
# print(driver.find_element(By.ID,'address').text)
#
# driver.execute_cdp_cmd('Emulation.setGeolocationOverride', {
#     'latitude': 51.507351,
#     'longitude': -0.127758,
#     'accuracy': 100
# })
#
# driver.refresh()
# driver.implicitly_wait(10)
# print(driver.find_element(By.ID,'address').text)

#device mode

# driver.get("https://www.b144.co.il/")
#
# driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
#     'width': 360,
#     'height': 740,
#     'deviceScaleFactor': 50,
#     'mobile': True
# })
# driver.refresh()


# #console log
#
# driver.get("https://www.ynet.co.il/")
# driver.execute_cdp_cmd('Log.enable', {})
#
# # גישה ללוגים באמצעות CDP
# def get_browser_logs(driver):
#     logs = driver.get_log('browser')
#     return logs
#
# driver.get("https://www.b144.co.il/")
#
# # המתנה לטעינת האתר
# time.sleep(5)
#
# # הדפסת הלוגים שנלכדו
# logs = get_browser_logs(driver)
# for log in logs:
#     print(f"Log: {log['message']}, Level: {log['level']}")

#סוג חיבור

#driver.execute_cdp_cmd('Network.enable', {})

# הגדרת תנאי הרשת
# driver.execute_cdp_cmd('Network.emulateNetworkConditions', {
#     'offline': False,    'latency': 20,
#     'downloadThroughput': 200 * 1024 / 8,
#     'uploadThroughput': 500 * 1024 / 8,
#     'connectionType': 'cellular4g'
#      })


# התעלמות מבעיות ssl

#options = Options()
#options.add_argument('--ignore-certificate-errors')  # התעלמות מבעיות בתעודות SSL
# עדכן את הנתיב ל-chromedriver

driver = webdriver.Chrome()
driver.maximize_window()
# פתיחת DevTools session
driver.execute_cdp_cmd('Log.enable', {})
driver.execute_cdp_cmd('Security.setIgnoreCertificateErrors', {'ignore': True})

# גישה לאתר הלא מאובטח
driver.get("http://expired.badssl.com/")



input("x")