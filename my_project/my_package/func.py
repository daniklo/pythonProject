#1
"""
def print_line():
    print("_" * 15)

print("hello world")
print_line()
print("my name is X")
print_line()

#תרגיל 1 באמצעות לולאה

def print_line():
   for x in range (15) :
     print("_", end='')
   print()

print("hello world")
print_line()
print("my name is X")
print_line()


2

def compare_names(first_name, last_name):
    if first_name == last_name:
        print(f"The names {first_name} and {last_name} are identical")
    else:
        print(f"The names {first_name} and {last_name} are not identical")

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

compare_names(first_name, last_name)

"""
3

def num_space(string) :
    space_count = 0
    for char in string :
        if char == " " :
           space_count +=1

    print(f"the number of cher in the string is {len(string)}")
    print(f"the number of cher without spaces  spae in the string is {len(string)-space_count}")


num_space("hello world world")

#3 - פתרון נוסף
"""
def count_characters(string):
    without_spaces = string.replace(" ", "")


    print(f"Number of characters without spaces: {len(without_spaces)}")
    print(f"Number of characters with spaces: {len(string)}")


count_characters("input string")

#תרגיל 4

#function 1
def in_array(num1, num2,num3) :
    arr= [num1,num2, num3]
    big = find_max_number(arr)
    return big



#function 2
def find_max_number(arr):
    # מחזיר את המספר הגדול ביותר מהמערך
    return max(arr)

#function 3
def sender(to_send):
    printer(to_send)


#function 4
def printer(to_print):
    print(to_print)


#ריצה
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

big = in_array(num1,num2,num3)
print(big)
sender("hello")


#אופציה נוספת למציאת האיבר הגדול ביותר במערך

# def largest(arr):
#   max = arr[0]
#   for i in range(1, len(arr)):
#     if arr[i] > max:
#       max = arr[i]
#   return max
#
# m = largest([1,2,4,6,9])
# print(m)

"""