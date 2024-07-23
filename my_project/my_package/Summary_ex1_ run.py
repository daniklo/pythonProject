from my_project.my_package.Summary_func_ex1 import *

# הדפסת כותרת המסעדה
print("**ברוכים הבאים למסעדת הטוסט הלוהט**")

# הגדרת מחיר הטוסט
tost_price = 15

# קבלת גיל הלקוח
age = ageChack()  # 15

# קבלת תוספות
extension_price = Additions()  # 9

# קבלת סוג השתייה
drinking_price = drink()  # 8

# חישוב מחיר כולל
total_price = tost_price + extension_price + drinking_price

# בדיקת זכאות להנחה
if 15 <= age <= 18:
  # הדפסת הודעה על הנחה
  print("יש לנו הנחה לבני נוער- קיבלת 5 שקלים הנחה")

  # חישוב מחיר לאחר הנחה
  discounted_price = total_price - 5

  # הדפסת מחיר הטוסט לאחר הנחה
  print(f"מחיר הטוסט שלך הוא רק {discounted_price} שקלים")

  # הדפסת מחיר הטוסט המקורי
  print(f"במקום {total_price} שקלים")

  # הדפסת איחולי תאבון
  print("בתאבון!")

else:
  # הדפסת מחיר הטוסט ללא הנחה
  print(f"מחיר הטוסט שלך הוא {total_price} שקלים")

  # הדפסת איחולי תאבון
  print("בתאבון!")
