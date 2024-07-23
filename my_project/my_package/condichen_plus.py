
#תרגיל 1
"""
day = int(input("Input a number : "))


match day:
    case 1:
        day = "Sunday"
    case 2:
        day = "Monday"
    case 3:
        day = "Tuesday"
    case 4:
        day = "Wednesday"
    case 5:
        day = "Thursday"
    case 6:
        day = "Friday"
    case 7:
        day = "saturday"
    case _:
       day = "not exists"

print("the day you insert is " +day)

#תרגיל 2

month = int(input("Input a month number: "))
year = int(input("Input a year: "))

month_name= None
numner_day = None

match month :
    case 1:
     month_name = "January"
     numbers_day= 31
    case 2:
     month_name = "February"
     numbers_day  = 29 if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) else 28
    case 3:
     month_name= "March"
     numbers_day= 31
    case 4:
     month_name= "April"
     numbers_day= 30
    case 5:
     month_name= "May"
     numbers_day = 31
    case 6:
     month_name  = "June"
     numbers_day= 30
    case 7:
     month_name = "July"
     numbers_day= 31
    case 8:
     month_name = "August"
     numbers_day= 31
    case 9:
     month_name = "September"
     numbers_day= 30
    case 10:
     month_name = "October"
     numbers_day = 31
    case 11:
     month_name = "November"
     numbers_day= 30
    case 12:
     month_name = "December"
     numbers_day = 31
    case _:
     month_name = "Unknown"
     numbers_day =  0

print("The month of {} in {} has {} days".format(month_name,year,numbers_day) )


#אופציה שניה לתרגיל 2
import calendar
y = input("insert year")
m = input("insert month")
d = calendar.monthrange(y, m)[1]
print(d)




#תרגיל 3

a1 = int(input("enter grade 1 : "))
a2 = int(input("enter grade 2 : "))
a3 = int(input("enter grade 3 : "))
avg = (a1+a2+a3)/3

grade = None

if avg>90 :
    grade = "A"
elif avg >=70 and avg <=90 :
    grade = "B"
elif avg >= 50 and avg <= 70:
    grade = "C"
elif avg < 50 :
    grade = "D"

print("your avg is : {} and your grade is : {}".format(avg,grade))

#תרגיל 4

num_products = int(input("Enter number of products purchased: "))
price_per_unit = float(input("Enter price per unit: "))

total_price = num_products * price_per_unit

if total_price < 100:
    discount = 0
elif 100 <= total_price <= 120:
    discount = 0.1
elif 120 < total_price <= 200:
    discount = 0.2
else:
    discount = 0.25

final_price = total_price * (1 - discount)



print("Total price before discount: {}".format(int(total_price)))
print("Discount: {}%".format(discount * 100))
print("Final price after discount: {}".format(int(final_price)))


#תרגיל 5

try:
    month = int(input("Enter month number (1-12): "))
    month_name = None
    match month:
        case 1:
            month_name =   "January"
        case 2:
            month_name = "February"
        case 3:
            month_name = "March"
        case 4:
            month_name = "April"
        case 5:
            month_name = "May"
        case 6:
            month_name = "June"
        case 7:
            month_name = "July"
        case 8:
            month_name = "August"
        case 9:
            month_name = "September"
        case 10:
            month_name = "October"
        case 11:
            month_name = "November"
        case 12:
            month_name = "December"
        case _:
            month_name = "error"

    if 1 <= month <= 4:
        print(f"very cold in {month_name}")
    elif 5 <= month <= 7:
        print(f"Quite comfortable in {month_name}")
    elif 8 <= month <= 12:
        print(f"very hot in {month_name}")
    else:
        print("There is no such month")

except :
    print("There is an error")

"""
#תרגיל 6

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    if num1 == num2 == num3:
        print("All numbers are equal")
    elif num1 != num2 and num2 != num3 and num1 != num3:
        print("No number is equal")
    else:
        print("Some numbers are equal")
except ValueError:
    print("Error: Please enter valid numbers")



