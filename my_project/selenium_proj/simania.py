from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# פתיחת דפדפן וניווט לאתר
driver = webdriver.Chrome()
driver.get("https://simania.co.il/")

# הזנת החיפוש ולחיצה על כפתור החיפוש
search_box = driver.find_element(By.ID, "query")
search_box.send_keys("אין ילדים רעים")
search_button = driver.find_element(By.XPATH, "//input[@value='חפש']")
search_button.click()
time.sleep(3)

# שליפת שם המחברת
try:
    author_name = driver.find_element(By.TAG_NAME, "h3").text
    print(author_name)
except Exception as e:
    print("שליפת שם המחבר/ת נכשלה")

# שליפת מספר המתעניינים בספר - משומש
try:
    book_price = driver.find_elements(By.XPATH, "//div[@class='showrating']//span[@class='tag']")[1].text
    print(book_price)
except Exception as e:
    print("שליפת המחיר נכשלה")

# שליפת מספר הביקורות
try:
    review_count = driver.find_element(By.XPATH, "//book-reviews//div[@class='simaniaTitleSmall2']//a").text
    print(review_count)
except Exception as e:
    print("שליפת מספר המדרגים נכשלה")

# שליפת שמות המדרגים
try:
    # לחיצה על דירוגים נוספים
    driver.find_element(By.XPATH, "//div[@id='comments']//button[@ng-click='toggleCollapse();']").click()
    time.sleep(2)
    rating_names = driver.find_elements(By.XPATH, "//book-reviews//a//div[@class='imageOverlay']")
    for rating_name in rating_names:
        print(rating_name.get_attribute("innerHTML").strip())
except Exception as e:
    print("שליפת שמות המדרגים נכשלה")
    print(e)

# סגירת הדפדפן
driver.quit()
