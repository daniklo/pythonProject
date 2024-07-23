import re

def age_check():
    age = 0
    while age == 0:
        str_age = input("אנא הזן את גילך: ")
        if str_age.isdigit():
            age = int(str_age)
            if age < 5 or age > 100:
                print("יש להזין גיל תיקני בין הגילאים 5 ל100")
                age = 0
        else:
            print("יש להזין מספרים בלבד")
    return age

def additions():
    extension = 0
    condition = 0
    add_infrastructure = ["זיתים", "פטריות", "תירס", "בצל", "עגבניות", "בולגרית"]
    print("אנא בחר תוספות לטוסט הפרד בין התוספות שאתה מעניין באמצעות הסימן פסיק")
    print("התוספות האפשריות הן זיתים , פטריות,תירס, בצל, עגבניות,בולגרית")
    add = input()
    while condition == 0:
        arry_add = add.split(",")
        for item in arry_add:
            trim_array = item.strip()
            if trim_array in add_infrastructure:
                if trim_array in ["זיתים", "תירס", "פטריות"]:
                    extension += 3
                    condition = 1
                elif trim_array in ["בצל", "עגבניות", "בולגרית"]:
                    extension += 4
                    condition = 1
            else:
                if trim_array == "לא רוצה":
                    print("בטוח? תוספות מוסיפות המון")
                    add = input()
                    if add in ["בטוח", "כן"]:
                        print("חבל, אתה מפסיד")
                        condition = 1
                        break
                    else:
                        add = input("אז מה תרצה להזמין?")
                        break
                print(trim_array + " לא ברשימה אנא הזן  מחדש רשימה תיקנית של תוספות")
                condition = 0
                extension = 0
                add = input()
                break
    return extension

def drink():
    extension_drink = 0
    breaker = 0
    print("מה בא לך לשתות? קולה או מיץ תפוזים?")
    print("אם אתה לא רוצה כלום הקש שלח הזמנה?")
    add = input()
    while breaker == 0:
        if add in ["תפוזים", "קולה"]:
            extension_drink = 8
            breaker = 1
        elif add == "שלח הזמנה":
            extension_drink = 0
            breaker = 1
        else:
            print("יש לבחור שתיה אחת מתוך הרשימה בלבד \"קולה\", \"תפוזים")
            add = input()
    return extension_drink
