import re


student1_name = "avi"
student1_age = 6
student1_email = "avi@gmail.com"

student2_name = "yossi"
student2_age = 8
student2_email = "yossi@gmail.com"

student3_name = "lital"
student3_age = 9
student3_email = "lital@gmail.com"




class Student:
    def __init__(self,name, age, email):
        self.name = name
        self.age = age
        self.__email = email

    # setter  method
    def set_email(self, value):
        self.__email = value

         # getter method
    def get_email(self):
            return self.__email

    def print_info(self):
         print(f"The student's name is {self.name}  and his age is {self.age}  and your email is {self.__email}")


s1 = Student("david", 19,"david@gmail.com")
s1.print_info()
s1.set_email("aaa")
print(s1.get_email())




# email_validate_pattern = r"[a-z0-9]+@+[a-z0-9]+[\.]+[a-z0-9]"
# if re.match(email_validate_pattern, value):
#     self.__email = value
# else:
#     raise ValueError("Sorry the email incorrect")


# s1.print_info()
# s1.__age=2
# print(s1.__age)
# s1.print_info()


# # setter  method
# def set_email(self, value):
#     if value == "bbb" :
#          self.__email= value
#     else:
#         print("NOT")
#
#  # getter method
# def get_age(self):
#     return self.__email


# email_validate_pattern = r"[a-z0-9]+@+[a-z0-9]+[\.]+[a-z0-9]"
# if re.match(email_validate_pattern, value):
#     self.__email = value
# else:
#     raise ValueError("Sorry the email incorrect")

# @property
# def email(self):
#     print("getter method called")
#     return self.__email
#
#     # a setter function
#
#
# @email.setter
# def email(self, value):
#     self.__email = value
