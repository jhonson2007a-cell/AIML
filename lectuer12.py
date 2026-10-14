#date-13oct,2026
#study about module

# import math as m #define a short key
# import math
# a=9
# print(m.sqrt(a))
# print(math.factorial(5))
# print(math.floor(4.9))    
# print(math.ceil(4.6))      
# print(math.pow(2, 3))     
# print(m.sin(math.pi/2))
# print(m.cos(math.pi/2))
# print(m.tan(math.pi/2))
# print(m.log(10))       
# print(m.pi)            

# import calculate
# print(calculate.add(2,3))
# print(calculate.div(4,2))
# print(calculate.mul(2,3))
# print(calculate.sub(4,2))

# import random
# print(random.random())
# print(random.randint(1,5))  
# print(random.randrange(1, 10))  
# print(random.uniform(1, 5))     
# print(random.choice(["A", "B", "C"])) 
# lst = [1, 2, 3, 4, 5]
# random.shuffle(lst)
# print(lst)                     

# print(random.sample([10, 20, 30, 40], 2))


import datetime

# now = datetime.datetime.now()      
# print(now)
# today_date = datetime.date.today()     
# print(today_date)

# dt = datetime.datetime(2026, 10, 13, 9, 30, 15)
# print(dt)
# print(dt.year)       
# print(dt.month)     
# print(dt.day)        
# print(dt.hour)       
# print(dt.minute)     
# print(dt.second)     
# print(dt.microsecond)

# today = datetime.datetime.now()
# print(today.strftime("%Y-%m-%d"))      
# print(today.strftime("%d/%m/%Y"))      
# print(today.strftime("%H:%M:%S"))  
# print(today.year)
# print(today.month)
# print(today.day)
# print(today.hour)
# print(today.minute)
# print(today.second)
# print(today.microsecond)

import os
from abc import ABC, abstractmethod


class feran(ABC):
    @abstractmethod
    def to_fahrenheit(self, celsius):
        pass

    @abstractmethod
    def to_celsius(self, fahrenheit):
        pass

    @abstractmethod
    def description(self):
        pass


class CelsiusConverter(feran):
    def to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def description(self):
        return "Converts temperatures between Celsius and Fahrenheit."


class calculate:
    @staticmethod
    def feran(c):
        converter = CelsiusConverter()
        return converter.to_fahrenheit(c)


# print(os.getcwd())
# print(os.listdir())
# os.mkdir("demo")
# print(os.path.exists("demo"))
# print(os.path.isdir("demo"))
# os.rmdir("demo")

# import math
# r=5
# print(math.pi*r*r)

# import random
# secret_number = random.randint(1, 10)
# print("Welcome to the Number Guessing Game!")
# print("Guess the number between 1 and 10")
# user_guess = int(input("Enter your guess: "))
# if user_guess == secret_number:
#     print("You win! Correct guess.")
# else:
#     print("Wrong guess! The secret number was", secret_number,".")

# import datetime
# user_date = input("Enter a date (YYYY-MM-DD): ")
# user_dt = datetime.datetime.strptime(user_date, "%Y-%m-%d")
# now = datetime.datetime.now()
# diff = now-user_dt
# print("Difference:",diff)
# print("Days:",diff.days)
# print("User date:",user_dt)
# print("Current date:",now)

# import os
# file_name = "test.txt"
# if os.path.exists(file_name):
#     print(file_name, "exists")
# else:
#     print(file_name, "does not exist")

import random
otp = random.randint(0, 999999)
print("Your OTP is: ",otp)

c=int(input("enter the temp="))
print(calculate.feran(c))







           






  