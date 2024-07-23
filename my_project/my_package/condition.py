# תרגיל ראשון:

x = int(input("enter num 1"))
y = int(input("enter num 2"))
print("סכום המספרים הוא  " + str(x+y))


# תרגיל שני:

win1 = "המספר הראשון גדול יותר"
win2 = "המספר השני גדול יותר"

x = int(input("enter num 1"))
y = int(input("enter num 2"))

if x > y:
    print(win1)
else:
    print(win2)

# תרגיל שלישי:

input = int(input("Input number: "))

if input > 0:
    print("Number is positive")
elif input < 0:
    print("Number is negative")
else:
    print("Number is zero")


# תרגיל 4:

num1 = int(input("Input the 1st number: "))
num2 = int(input("Input the 2nd number: "))
num3 = int(input("Input the 3rd number: "))

if num1 > num2:
    if num1 > num3:
        print("The greatest: " + str(num1))
if num2 > num1:
    if num2 > num3:
        print("The greatest: " + str(num2))
if num3 > num1:
    if num3 > num2:
        print("The greatest: " + str(num3))


# תרגיל 5:

x = int(input("enter num 1 : "))

if x % 2 == 0:
    print("המספר " + str(x) + " זוגי")
else:
    print("המספר " + str(x) + " לא זוגי")

# תרגיל 6:

x = int(input("enter num between 1-100"))

if x > 1 and x < 100:
    print(x)
if x < 1:
    print("המספר קטן מידי")
if x > 100:
    print("המספר גדול מידי")

# תרגיל 7:

x = int(input("enter your age"))

if x > 20 and x < 50:
    print("enter your tall")
    y = int(input())
    if y > 180:
        print("התקבלת")
    else:
        print("אינך  בגובה המתאים")
else:
    print("אינך בגיל המתאים")
