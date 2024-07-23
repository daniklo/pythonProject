import random

# תרגיל 1

for x in range(1, 11):
    if x == 4:
        continue
    print(x)

# תרגיל 2

for x in range(1, 101):
    if x % 3 == 0 and x % 7 == 0:
        print(x)

# תרגיל 3
sum = 0
for x in range(1, 21):
    sum = sum + x
print(sum)

# תרגיל 4
sum = 0
for x in range(5):
    sum = sum + int(input("please enter a number : "))
print(sum)

# תרגיל 5

sum = 0
avg = 0
user_num = None

for i in range(10):
    user_num = int(input("enter a number : "))
    if user_num == 0:
        break
    sum = sum + user_num

print("sum is {}".format(sum))
print("amount is : {} ".format(i))
print("avg is : {} ".format(int(sum / float(i))))



# תרגיל 6

for x in range(1, 11):
    for y in range(1, 11):
        if x * y < 10:
            print("0", x * y, ",", end='', sep='')
        else:
            print(x * y, ",", end='', sep='')
    print()

# תרגיל 7
# פתור בתוך תרגיל 6
# תרגיל 8


x = random.randint(1, 10)
counter = 1
first = 1

while counter <= 5:
    if first == 1:
        print("הזן מספר בין 1 ל 10 ונסה לנחש את המספר")
        first = 2

    else:
        print("הזן ניחוש נוסף")

    y = int(input())
    if x == y:
        print("הצלחת")
        break

    if y > x:
        print("המספר שלך גבוה מידי ")

    else:
        print("המספר שלך נמוך מידי ")

    counter += 1

if counter == 6:
    print("הפסדת")

# תרגיל 9

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527]

for x in numbers:
    if x < 237:
        print(x, end=',')
