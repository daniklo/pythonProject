import time

import pyautogui
import pyperclip
from selenium import webdriver
import pyautogui
from pynput.keyboard import Key, Controller
driver = webdriver.Chrome()
driver.maximize_window()




driver.get("https://www.jobmaster.co.il/");
time.sleep(2)
# טקסט בעברית
text = 'בדיקות תוכנה'
# העתקת הטקסט ללוח
pyperclip.copy(text)
location = pyautogui.locateOnScreen(r'C:\selenium\sikuliImages\Stype.png',  confidence=0.6)
pyautogui.click(pyautogui.center(location))
pyautogui.typewrite('QA', interval=0.05)
time.sleep(2)
keyboard = Controller()
"""
# התחלת הקומבינציה של Ctrl+V
keyboard.press(Key.ctrl)
# לוחצים ושוחררים V
keyboard.press('v')
keyboard.release('v')
# שוחררים את Ctrl
keyboard.release(Key.ctrl)

"""
time.sleep(2)
pyautogui.press('alt')

location = pyautogui.locateOnScreen(r'C:\selenium\sikuliImages\Sbtn.png')
if location:
    pyautogui.click(location)

try :
    time.sleep(5)
    location = pyautogui.locateOnScreen(r'C:\selenium\sikuliImages\logo.png', confidence=0.8)
    print("logo pass")

except  Exception as e :
       print(f" logo fail {e}")

try :
    location = pyautogui.locateOnScreen(r'C:\selenium\sikuliImages\gius.png', confidence=0.8)
    print(f"gius pass {location}")


except  Exception as e :

   print(f" gius fail {e}")


input("x ")