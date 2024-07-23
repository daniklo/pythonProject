#1
"""
class Person :
    name = None
    age = None
    gender = None

    def info(self, name, age,gender):
        print(f"the name {name} and my age is {age} and my gender is {gender}")

p1 = Person()
p1.name = "dani"
p1.age = 15
p1. gender = "male"


p1.info(p1.name,p1.age,p1.gender)
"""
# 2
"""
class Person:

    name = None
    age = None

class Student(Person):

    major = None


    def study(self,name,major):
        print( f"my name is {name} and i learn {major}")

s1= Student()
s1.name = "dani"
s1.major ="QA"

s1.study(s1.name,s1.major)


#3 + 4

class Animal:

    def __init__(self,leg_numbers):
        self.leg_numbers= leg_numbers

    def legs_print (self):
        print("number of legs is " + self.leg_numbers)

    def speak(self):
        print("Woof!")
class Dog(Animal):

    def __init__(self,leg_numbers):
        super().__init__(leg_numbers)

    def speak(self):
        print("Ho ho ho!")

a1 = Dog("5")
a1.speak()
super(Dog, a1).speak()
super(Dog, a1).legs_print()

"""
#5

class Car :
    def __init__(self, year,car_company, color):
        self.__year = self.set_year(year)
        self.car_company = car_company
        self.color = color

    def set_year (self,value):
        #if value > 2010 and value < 2014 :
        if 2010 < value < 2014 :
            self.__year = value
        else :
            self.__year = "NOT VALID"
        return self.__year

    def get_year (self):
        return self.__year

    def info(self):
        print(f"The car's year of manufacture is {self.get_year()} and its manufacturing company is {self.car_company} and it is {self.color} color")

c1 = Car (2009,"volvo","red")
c1.info()
c1.set_year(2013)
c1.info()



#----------------------------------------------דוגמאות מהמצגת







