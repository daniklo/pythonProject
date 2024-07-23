from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://danielauto.net/practice/tabls/tables.html")
"""
try:
    print("----------------   1   -----------------------------")
    driver.get("http://danielauto.net/practice/tabls/tables.html")
    time.sleep(1)

    # תרגיל 1
    tr = driver.find_elements(By.TAG_NAME, "tr")
    print("the tr number is :", len(tr))

    td = driver.find_elements(By.XPATH, "//tr[1]//td")
    print("the td number is :", len(td))
except Exception as e:
    print(e)

try:
    print("----------------   2   -----------------------------")
#    driver.get("http://danielauto.net/practice/tabls/tables.html")
    time.sleep(1)

    company_groups = driver.find_elements(By.XPATH, "//td[2]")
    a = b = c = 0
    for i in range(1, len(company_groups)):
        group = company_groups[i].text

        if group == "A":
            a += 1
        elif group == "B":
            b += 1
        elif group == "C":
            c += 1

    print("group a :", a, "  group b :", b, "  group c :", c)
except Exception as e:
    print(e)

try:
    print("----------------   3   -----------------------------")
#    driver.get("http://danielauto.net/practice/tabls/tables.html")


//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/span[1]/div[1]/div[2]
//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/span[2]/div[1]/div[2]
//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/span[3]/div[1]/div[2]
//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/span[243]/div[1]/div[2]

    prices = driver.find_elements(By.XPATH, "//td[3]")
    הכנסה למשתנה בשם max_price את האיבר הראשון ברשימה#
    max_price = float(prices[0].text)  
    
    לולאה שרצה על כל המערך#
    for price in prices[1:]:  # דילוג על האינדקס הראשון
      הסרת פסיקים על מנת שיהיה ניתן להפוך למספר#
        price_text = price.text.replace(",", "") 
        המרת האיבר ברשימה למספר עשרוני#
        current_price = float(price_text)
        בדיקה - אם האיבר הנוכחי בלולאה גדול יותר מהאיבר הקודם#
        if current_price > max_price:
         אם כן אז הmax_price מקבל את הערך הגדול יותר# 
            max_price = current_price

    print("Maximum current price is :", max_price)
except Exception as e:
    print(e)  # הדפסת שגיאה אם ישנה

try:
    print("----------------   4   -----------------------------")
    driver.get("http://danielauto.net/practice/tabls/tables.html")
    time.sleep(3)

    #   שמות החברות
    company_names = driver.find_elements(By.XPATH, "//td[1]")

    for name_element in company_names[1:]:  # דילוג על האינדקס הראשון
        name_text = name_element.text.lower()

        if name_text.startswith('a'):
            print(name_text)

except Exception as e:
    print("An error occurred:", e)


try:
    print("----------------   5   -----------------------------")
    driver.get("http://danielauto.net/practice/tabls/tables.html")
    time.sleep(3)

    # איתור רשימות שמות החברות והקבוצות
    company_names = driver.find_elements(By.XPATH, "//td[1]")
    company_groups = driver.find_elements(By.XPATH, "//td[2]")

    for i in range(1,len(company_groups),1) :
        if company_names[i].text.lower().startswith('a') and company_groups[i].text.lower()=='c' :
            print(company_names[i].text)

except Exception as e:
    print("An error occurred:", e)

try:
    print("----------------   6   -----------------------------")
 #   driver.get("http://danielauto.net/practice/tabls/tables.html")


    changes = driver.find_elements(By.XPATH, "//td[5]")
    sum = 0.0
    for change in changes[1:]:
        text = change.text.strip().replace("+ ", "")
        m = float(text)
        sum += m

    print("Total profit in percentages {:.2f}".format(sum))

except Exception as e:
    print("An error occurred:", e)
    
"""
try:
    print("----------------   7   -----------------------------")
    driver.get("http://danielauto.net/practice/tabls/tableDynamic.html")
    time.sleep(3)

    rows = driver.find_elements(By.TAG_NAME, "tr")

    for i, row in enumerate(rows):
        cells = row.find_elements(By.TAG_NAME, "td")
        last_text = driver.find_element(By.XPATH, f"//tr[{i+1}]/td[last()]").text
        print(last_text)

except Exception as e:
    print("Error in exercise 7:", e)
