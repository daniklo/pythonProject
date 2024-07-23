def get_age():
    while True:
        age_input = input(" מה גילך? ")
        if not age_input.isdigit():
            print(" אנא הכנס מספרים בלבד.")
            continue

        age = int(age_input)
        if 5 <= age <= 100:
                return age
        else:
                print(" אנה הזן גיל בין 5-100")



def calculate_discount(age):
    if 15 <= age <= 18:
        return 5
    return 0

def addons():
    while True:
        q1=input(" האם אתה מעוניין בתוספות בטוסט ? כן/לא ")
        if q1.lower()== 'לא':
            q2 = input(" בטוח שלא תרצה תוספת ? ")
            if q2.lower() == 'כן':
                return 0
            elif  q2.lower() == 'לא':
                continue

        elif q1 == 'כן' :
                while True:
                    addons_amount = input(" כמה תוספות תרצה? ")
                    if not addons_amount.isdigit():
                        print(" אנא הכנס מספרים בלבד.")
                        continue
                    return int(addons_amount)


def drink():
    while True:
        drink_choice = input(" איזה שתייה תרצה? (פפוזים/קולה) ")
        if drink_choice in ["פפוזים","קולה"]:
            return drink_choice
        else:
            print(" אנא תבחר רק קולה או פפוזים")
