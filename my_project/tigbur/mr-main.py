import poalim

a = int(input("enter num 1 : "))
b = int(input("enter num 2 : "))
c = int(input("enter num 3 : "))

big = poalim.get_number(a,b,c)
poalim.send(big)