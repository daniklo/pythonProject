import re
email_list = ["dalia@yahoo.com", "ruthi@yahoo.com", "morya@yahoo.com", "benny@yahoo.com"]
updated_email_list = [email.replace("@yahoo.com", "@gmail.com") for email in email_list]
#1

email_list = ["dalia@yahoo.com", "ruthi@yahoo.com", "morya@yahoo.com", "benny@yahoo.com"]
new_email_list =[]

for email in email_list :
    new_email_list.append(email.replace("yahoo", "gmail"))

print(new_email_list)

#2

email_list = ["dalia@yahoo.com", "rothi@yahoo.com", "morya@yahoo.com", "benny@yahoo.com"]
user = []
domain = []

for m in email_list :
    temp = m.split('@')
    user.append(temp[0])
    domain.append(temp[1])

print(user)
print(domain)

#3

is_read = False

for x in range(3) :
    col = input("enter the color you like ")
    col = col.strip().lower()
    if col == "red" :
        is_read = True

if is_read :
        print("I knew you were a Hapoel fan")
else:
        print("yoy choose a nice color")

#4

phone = input("enter your phone number ")

valid_phone = r"\d{2,3}[-]?\d{7}"
if re.match(valid_phone, phone) :
    print("the phone number is ok")
else:
    print("the phone number is not valid")
