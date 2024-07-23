from Summary_func_ex2 import *
print("**ברוכים הבאים למסעדת הטוסט הלוהט**")
tost = 15 # מחיר טוסט גולמי לפני תוספות והנחה
age = age_check() # מפעיל את פונקציית הגיל, יקבל בחזרה את הגיל של המשתמש
extension = additions() # מפעיל את פונקציית תוספות - יקבל בחזרה את הסכום שיש לשלם על התוספות
drinking = drink() # מפעיל את פונקציית שתיה - יקבל בחזרה את הסכום שיש לשלם על שתיה
# בודק את הגיל שקיבלנו האם הוא זכאי להנחה - ניתן לבצע זאת גם בתוך הפונקציה של הגיל ולקבל רק מחיר
with_discount = tost + extension + drinking - 5
without_discount = tost + extension + drinking
if age >= 15 and age <= 18 :
    print("יש לנו הנחה לבני נוער- קיבלת 5 שקלים הנחה")
    print(f"מחיר הטוסט שלך הוא רק   {with_discount} שקלים ")
    print(f" במקום   {without_discount} שקלים ")
    print(" בתאבון! ")
else :
    print(f" מחיר הטוסט שלך הוא    {without_discount} שקלים ")
    print(" בתאבון! ")


