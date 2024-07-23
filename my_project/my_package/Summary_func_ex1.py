def ageChack():
  age = 0
  while age == 0:
    strAge = input("אנא הזן את גילך: ")

    # בדיקת שהוזנו מספרים בלבד
    if strAge.isdigit():
      age = int(strAge)

      # בדיקת טווח הגיל
      if 5 <= age <= 100:
        break
      else:
        print("יש להזין גיל תיקני בין הגילאים 5 ל-100")
        age = 0

    else:
      print("יש להזין מספרים בלבד")

  return age

def Additions():
    extension = 0
    condition = True
    first = True

    while condition:
      if first :
        answer = input(
        "האם תירצה תוספות בטוסט? \nתוספות עולות 3 שקלים לכל תוספת. אנא הזן את מספר התוספות. במידה ואינך רוצה תוספות הזן: לא רוצה תוספות: ")
        first = False
      else:
        answer = input("אז כמה תוספות אתה רוצה")
      if answer.lower() == "לא רוצה":
        confirmation = input("בטוח? תוספות מוסיפות המון. אנא אשר: ")
        if confirmation in ["בטוח", "כן"]:
          print("חבל, אתה מפסיד")
          return extension * 3
          extension = 0

          condition = False
          break

        else:
          # קריאה לפונקציה מחדש
          #return Additions()
          continue

      else:
        while extension == 0:
          try:
            additional_items = int(answer)
            print("בקשתך התקבלה")
            extension = additional_items
            condition = False
          except ValueError:
            print("הקשת תווים שאינן ספרות")
            answer = input("כמה תוספות תירצה? ")

    return extension * 3





def drink():
  extension_drink = 0
  breaker = 0

  print("מה בא לך לשתות? קולה או מיץ תפוזים?")
  print("אם את/ה לא רוצה כלום יש להקיש שליחת הזמנה?")

  while breaker == 0:
    answer = input(": ")

    if answer.lower() in ["קולה", "תפוזים"]:
      extension_drink = 8
      breaker = 1

    elif answer.lower() == "שליחת הזמנה":
      extension_drink = 0
      breaker = 1

    else:
      print("יש לבחור שתיה אחת מתוך הרשימה בלבד: \"קולה\", \"תפוזים\" או להקיש שליחת הזמנה להזמנה ללא שתיה")

  return extension_drink
