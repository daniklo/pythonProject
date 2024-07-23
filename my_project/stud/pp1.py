from pp2 import get_age, calculate_discount, addons, drink

def pp1():
    print("Welcome to --- !!!!Toast Haaa LoheT!!!")

    age = get_age()
    discount = calculate_discount(age)



    toast_price = 15
    print(f"מחיר הטוסט הינו {toast_price} ₪  ")

    addons_count= addons()
    addons_price = addons_count * 3
    print(f" הוספת {addons_count} תוספות , מחיר התוספות הוא {addons_price} ₪ ")

    drink_choice = drink()
    drink_price = 8
    print(f"המחיר של {drink_choice} הוא {drink_price} ₪ ")

    if discount > 0:
        print("קיבלת הנחת נוער בסך 5 ₪ בשל גילך ")
    total_price = toast_price + addons_price + drink_price - discount


    print(f"המחיר הסופי שלך הוא {total_price} ₪ ")


if __name__ == "__main__":
        pp1()










