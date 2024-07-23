

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()



"""""
# סעיף א
try:
    print("----------------   6   -----------------------------")
    driver.get("https://www.supermarker.themarker.com/")
    search_input = driver.find_element(By.ID, "txtSearch")
    search_input.send_keys("מחשבון")
    time.sleep(2)
    print("step א pass")
except Exception as e:
    print("Error in section א:", e)

# סעיף ב
try:

    #זיהוי הרשימה#
    ul = driver.find_element(By.CSS_SELECTOR, ".ui-autocomplete.ui-front.ui-menu.ui-widget.ui-widget-content")
    #יצירת ליסט עם כל רכיבי הרשימה#
    list_items = ul.find_elements(By.TAG_NAME, "li")
    #הקלקה על הרכיב השני ברשימה#
    list_items[1].click()
    print("step ב pass")
except Exception as e:
    print("Error in section ב:", e)

# סעיף ג
try:
    activ = driver.find_element(By.XPATH, "//*[@id=\"rblSelectCalcType\"]/label[1]")
    active_class = activ.get_attribute("class")
    print("חשב לפי אקטיבי" if "ui-state-active" in active_class else "חשב לפי לא אקטיבי")
    print("step ג pass")
except Exception as e:
    print("Error in section ג:", e)

# סעיף ד
try:
    elem = driver.find_element(By.XPATH, "//*[@id=\"mortgageCalculatorType\"]/tbody/tr[3]/td[1]/img")
    ActionChains(driver).move_to_element(elem).perform()
    time.sleep(2)
    print(elem.get_attribute("alt"))
    print("step ד pass")
except Exception as e:
    print("Error in section ד:", e)

# סעיף ה
try:
    driver.find_element(By.XPATH, "//*[@id=\"rblSelectKeren\"]/label[2]/span").click()
    print("step ה pass")
except Exception as e:
    print("Error in section ה:", e)

# סעיף ו
try:
    loan_amount = driver.find_element(By.ID, "txtLoanAmount")
    loan_amount.clear()
    loan_amount.send_keys("500000")
    print("step ו pass")
except Exception as e:
    print("Error in section ו:", e)

# סעיף ז
try:
    element = driver.find_elements(By.CSS_SELECTOR, ".ui-slider-handle.ui-state-default.ui-corner-all")[2]
    move = ActionChains(driver)
    move.click_and_hold(element).move_by_offset(32, 0).release().perform()
    print("step ז pass")
except Exception as e:
    print("Error in section ז:", e)

# סעיף ח
try:
    interest_input = driver.find_element(By.ID, "txtInterest")
    interest_input.clear()
    interest_input.send_keys("3.75")
    print("step ח pass")
except Exception as e:
    print("Error in section ח:", e)

# סעיף ט
try:
    driver.find_element(By.ID, "ibCalc").click()
    time.sleep(1)
    print("step ט pass")
except Exception as e:
    print("Error in section ט:", e)

# סעיף י
try:
    keren_text = driver.find_element(By.ID, "keren").text
    print(keren_text)
    driver.find_element(By.ID, "txtEmail").send_keys(keren_text)
    print("step י pass")
except Exception as e:
    print("Error in section י:", e)

# סעיף יא
try:
    driver.find_element(By.ID, "txtShemPrati").send_keys("name")
    print("step יא pass")
except Exception as e:
    print("Error in section יא:", e)

# סעיף יב
try:
    driver.get("https://www.supermarker.themarker.com/Calculators/Mortgage/MartgageCalculator.aspx")

    time.sleep(3)


    checkbox = driver.find_element(By.ID, "cbTnaim")
    print(1)
    if not checkbox.is_selected():
        checkbox.click()
        print(2)
        #driver.find_element(By.ID, "btnSendLid").click()
    else:
        pass
        #driver.find_element(By.ID, "btnSendLid").click()
    print("step יב pass")
except Exception as e:
    print("Error in section יב:", e)

# סעיף יג
try:
    time.sleep(2)
    email_error = driver.find_element(By.XPATH, "//label[@for='txtEmail' and @class='error']")
    print("msg error mail ok" if email_error.text == "יש להזין כתובת מייל" else "msg error mail fail")
    print("step יג pass")
except Exception as e:
    print("Error in section יג:", e)



# סעיף א
driver.get("https://www.vila4u.com/")
try:
    search_input = driver.find_element(By.ID, "siteSearch")
    search_input.send_keys("וילות בצפון")
except Exception as e:
    print("Error in section א:", e)

# סעיף ב
try:
    driver.find_element(By.NAME, "category").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"searchBox\"]/div[2]/select[1]/option[14]").click()
    driver.find_element(By.XPATH, "//*[@id=\"searchBox\"]/div[2]/div[3]").click()
    time.sleep(1)
except Exception as e:
    print("Error in section ב:", e)

# סעיף ג
try:
    driver.find_element(By.ID, "acc_81").click()
    driver.find_element(By.ID, "acc_85").click()
except Exception as e:
    print("Error in section ג:", e)

# סעיף ד
try:
    driver.find_element(By.ID, "selRooms").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//option[@value='9']").click()
    time.sleep(1)
except Exception as e:
    print("Error in section ד:", e)

# סעיף ה
try:
    driver.find_element(By.XPATH, "//a[@class='submitSearch']").click()
    time.sleep(1)
except Exception as e:
    print("Error in section ה:", e)

# סעיף ו
try:
    villas = driver.find_elements(By.XPATH, "//div[@class='recBox']//div[@class='boxDetails']/a")
    for villa in villas:
        print(villa.text)
except Exception as e:
    print("Error in section ו:", e)
    
  
#######תרגיל 3######
driver.get("https://www.weekend.co.il/glamping/hadkalim#reviews")

while True :
    try:
        driver.find_element(By.XPATH,"//button[contains(text(),\"חוות דעת\")]").click()
        time.sleep(1.5)

    except :
        break

grade = driver.find_elements(By.XPATH,"//div[@class='reviews_review-score__aRHgz']")
sum = 0
for i in grade :
     sum += float(i.text)

# # סעיף ב
print(f"**** sum : {sum:.2f} ******")
print("**** business number : {} ******".format(len(grade)))
#
# סעיף ג

if len(grade) > 0:
    avg = sum / len(grade)
else:
    avg = 0

print(f"**** avg : {avg:.2f} ******")
  """""
#תרגיל 4
def listen(driver, lang):
    """פונקציה ללחיצה על השמעת קול."""
    try:
        play_button_xpath = "//body[@id='yDmH0d']//c-wiz[@class='sciAJc']/div[@class='QcsUad BDJ8fb sMVRZe hCXDsb wneUed']//div/div[6]/div[1]//button[@jscontroller]//div[3]"
        #play_button_xpath = r"//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div/div[6]/div/div[6]/div[1]/div[2]/span/button/div[3]"
        element = driver.find_element(By.XPATH, play_button_xpath)
        element.click()
        dis = driver.find_element(By.XPATH,'//button[@aria-label=\'האזנה לתרגום\' and @disabled]')
        print(f"the {lang} language cannot be played:")

        time.sleep(1)
    except Exception as e:
        print(f"the {lang} played ")


driver.get("https://translate.google.com/")
driver.implicitly_wait(10)  # המתינות סמויה בשניות

try:
    # הזנת טקסט לתרגום
    text_area = driver.find_element(By.XPATH, "//textarea[@aria-label='טקסט מקור']")
    text_area.send_keys("שלום שמי דניאל")
    time.sleep(1)
    # לחיצה על החץ לשפות נוספות
    driver.find_element(By.XPATH, "//button[@aria-label='עוד שפות יעד']").click()
    time.sleep(1)
    # לקיחת השפות לרשימה
    languages = driver.find_elements(By.XPATH, "//div[@class='ykTHSe']//div[@class='Llmcnf']")

    # ריצה על הרשימה ולחיצה על שפה אחרת
    for i in range(12, 17):  # ריצה מ-2 עד 6 (כולל)
        lang = languages[i].get_attribute("innerHTML")
        time.sleep(1.5)
        languages[i].click()
        time.sleep(1)

        # הפעלת פונקציה להשמעת קול
        listen(driver, lang)
        time.sleep(1)

        # פתיחת חץ השפות שוב
        driver.find_element(By.XPATH, "//button[@aria-label='עוד שפות יעד']").click()

except Exception as e:
    print("Error during exercise:", e)


input("x")