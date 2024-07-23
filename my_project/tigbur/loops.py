import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#1##
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://freesbe.com/used-car-for-sale")
# time.sleep(10)
#


# data = driver.find_elements(By.XPATH, "//h4[contains(@class,'mui-style-8gcpke')]")
#
#
# list_years = list()
# for y in data:
#     pars_years = y.text.split(" | ")
#     list_years.append(pars_years[1])
#     if int(pars_years[1]) < 2021:
#         print(y.text)

#2##
"""
def ageChack():

  while  True:
    strAge = input("אנא הזן את גילך: ")

    # בדיקת שהוזנו מספרים בלבד
    if strAge.isdigit():
      age = int(strAge)

      # בדיקת טווח הגיל
      if 5 <= age <= 100:
        break
      else:
        print("יש להזין גיל תיקני בין הגילאים 5 ל-100")


    else:
      print("יש להזין מספרים בלבד")

  return age


age = ageChack()
print(f"your age is {age}")

"""
#3##
x = random.randint(1, 10)
counter = 1
check = True
for i in range(1,6):

   if check :
    user_num = int(input("המחשב בחר מספר נסה לנחש אותו"))
    check = False
   else:
    user_num = int(input("נסה שוב"))

   if user_num > x :
     print("המספר שבחרת גדול מידי")
   if user_num < x :
    print("המספר שבחרת קטן מידי")
   if x==user_num :
     print("ניצחת")
     break
   counter+=1


if counter == 6 :
  print("הפסדת")

# counter = 1
# first = 1
#
# while counter <= 5:
#     if first == 1:
#         print("הזן מספר בין 1 ל 10 ונסה לנחש את המספר")
#         first = 2
#
#     else:
#         print("הזן ניחוש נוסף")
#
#     y = int(input())
#     if x == y:
#         print("הצלחת")
#         break
#
#     if y > x:
#         print("המספר שלך גבוה מידי ")
#
#     else:
#         print("המספר שלך נמוך מידי ")
#
#     counter += 1
#
# if counter == 6:
#     print("הפסדת")

"""
#4##

for x in range(1, 11):
    for y in range(1, 11):
        if x * y < 10:
            print("0", x * y, ",", end='', sep='')
        else:
            print(x * y, ",", end='', sep='')
    print()

"""