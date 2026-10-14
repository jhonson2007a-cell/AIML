#Date-10 oct,2026
# learn about function

# 1. Simple function
# def greet():
#     print("Hello, world!")
# greet()


# 2. Function with parameters
# def add(a, b):
#     return a + b

# print(add(5, 3))   


# 3. Function with default values
# def greet_user(name="User"):
#     print("Hello,", "\n",name,"!")

# greet_user()
# greet_user("jack")


# 4. Function returning multiple values
# def min_max(numbers):
#     return min(numbers), max(numbers)

# small, large = min_max([3, 8, 1, 10, 5])
# print(small, large) 


# 5. Function with variable arguments
# def total(*numbers):
#     return sum(numbers)

# print(total(1, 2, 3, 4, 5)) 


# 6. Function with keyword arguments
# def person(name, age):
#     print("Name: ",name," Age:", age)

# person(name="John", age=20)


# 7. Lambda function
# square = lambda x: x * x
# print(square(7))   

#Answer09
# x=20
# def change():
#     global x
#     x=25
#     print("Inside change variable function",x)

# change()
# print("outer unchanged variable function",x)

#ANSWER10
# a = 5
# def out():
#     b = 10
#     def inner():
#         nonlocal b
#         global a
#         b = 20
#         a = 10
#         c = 30
#         print("local =", c)
#         print("global =", a)
#         print("enclosing =", b)
#     inner()
#     print("updated b in out =", b)
# out()
# print("updated a in global =", a)

#Answer04


    

