import random


def convert_to_number(choice):
    if choice == "אבן":
        return 1
    elif choice == "נייר":
        return 2
    elif choice == "מספריים":
        return 3
    else: return 4


def convert_to_string(choice):
    if choice == 1:
        return "אבן"
    elif choice == 2:
        return "נייר"
    elif choice == 3:
        return "מספריים"

def fighting(computer_choice, user_choice):
    if user_choice == 1:
        if computer_choice == 1:
            return "תיקו"
        elif computer_choice == 2:
            return "אני"
        else:
            return "אתה"
    elif user_choice == 2:
        if computer_choice == 1:
            return "אתה"
        elif computer_choice == 2:
            return "תיקו"
        else:
            return "אני"
    elif user_choice == 3:
        if computer_choice == 1:
            return "אני"
        elif computer_choice == 2:
            return "אתה"
        else:
            return "תיקו"


user_win = 0
computer_win = 0
tie = 0

print("ברוכים הבאים למשחק אבן נייר ומספריים")
print("בא נראה מי הטוב מבין חמש משחקים")
counter = 1
while counter <= 5 :

    result_user = input("תבחר אבן נייר או מספריים : ")
    user_choice = convert_to_number(result_user)
    if user_choice ==4 :
        print("בחירה שגויה, יש לבחור רק מהאופציות אבן נייר או מספריים")
        continue

    computer_choice = random.randint(1, 3)
    computer_choics_str = convert_to_string(computer_choice)

    result = fighting(computer_choice, user_choice)

    print(f"אתה בחרת : {result_user}")
    print(f"אני בחרתי : {computer_choics_str}")

    print(f"המנצח הוא : {result}\n")

    if result == "אתה":
        user_win += 1
    elif result == "אני":
        computer_win += 1
    elif result == "תיקו":
         tie += 1
    counter +=1

print("**תוצאות המשחקים הם:")
print(f"אתה נצחת {user_win} פעמים\nאני נצחתי {computer_win} פעמים\nויצאנו תיקו {tie} פעמים")



