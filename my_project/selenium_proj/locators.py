

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
driver.maximize_window()

# פתיחת האתר בדפדפן
driver.get("http://danielauto.net/practice/newLocator/locator.html")

# תרגיל 1
driver.find_element(By.ID, "myText").send_keys("name")
driver.find_element(By.ID, "btn").click()

textA = driver.find_element(By.ID, "myText2").text
textB = "name"
if textA == textB:
    print("exercise 1 pass")
else:
    print("exercise 1 fall")

driver.back()

# תרגיל 2
driver.find_element(By.NAME, "by_Name").click()
img_name = driver.find_element(By.NAME, "by_Name").get_attribute("src")
if img_name == "https://danielauto.net/practice/newLocator/name_red.png" :
    print( "ex2 pass")

#setTimeout(() => { debugger; }, 10000)
# תרגיל 3
tn = driver.find_element(By.TAG_NAME, "h3").text
cl = driver.find_element(By.CLASS_NAME, "c_name").text
print(tn + " " + cl)

# תרגיל 4
print(driver.find_element(By.XPATH, "/html/body/p[5]").text)

# תרגיל 5
driver.find_element(By.LINK_TEXT, "Click me to check link text").click()
print(driver.find_element(By.ID, "link_text").text)
driver.back()

# תרגיל 6
driver.find_element(By.PARTIAL_LINK_TEXT, "Click me to check partial link text").click()
print(driver.find_element(By.ID, "p_link_text").text)
driver.back()

# תרגיל 7
driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()
print(driver.find_element(By.ID, "btn").text)

# סגירת הדפדפן
driver.quit()
