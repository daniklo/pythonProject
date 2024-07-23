def get_number(a,b,c) :
    list = [a,b,c]
    big = biger(list)
    return big

def biger (list) :

    for x in list:
        big = list[0]
        if x > big :
            big = x
    return big
def send (number) :
   printer(number)

def printer (number) :
    print(number)



