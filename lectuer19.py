''''def greet(name):
    return f"Hello, {name}"

x = greet("Test")
y = greet
print(type(x))
print(type(y))
print(x)
print(y)
print(y("Testing"))'''


'''myfunc=[lambda x:x*2, lambda x:x*3]
print(myfunc[0](4))
print(myfunc[1](4))'''

'''#passing a function as an argument
def greet(name):
    print(f"Hello : {name}")
def execute(func):
    func("Testing")
execute(greet)'''

'''#Returning a function from another function
def apply_func(f,val):
    return f(val)
print(apply_func(lambda x:x**2,4))'''


'''#Storing functions in a dictionary mapping
action={"add": lambda a, b: a+b, "sub": lambda a,b: a-b}
print(action["sub"](10,5))'''

'''#Exercise 1
mytuple=(min,max,sum)
print(mytuple[2]([1,2,3,4,5]))'''

'''def outer():
    def inner():
        return "Inside Inner"
    return inner()
print(outer())'''

'''def multiplier(n):
    def multiply(x): return n**x
    return multiply(5)
print(multiplier(3))'''


# def applyfunc(f,val):
#     return f(val)
# print(applyfunc(lambda x:x**2,4))

# action={
#     "add":lambda a,b:a+b,"sum":lambda a,b:a-b
# }
# print(action["add"](5,6))
# print(action["sum"](10,6))

# mytu=(min,max,sum)
# print(mytu[1]([4, 9, 2]))

# def outer():
#     def inner():
#         return "inside inner"
#     return inner()
# print(outer())


# def mu(n):
#     def mul(x):
#         return n**x
#     return mul(5)
# print(mu(3))


# def pr(vsl):
#     def clean():
#         return vsl.strip()
#     return clean().upper()
# print(pr(" python "))


# def cir(r):
#     def ar():
#         return 3.14*r*r
#     return ar()
# print(cir(4))

# def name(fi,la):
#     def com():
#         return fi+la
#     return com()
# print(name("jhon"," lahre"))



# def app_dis(re):
#     def cal(pr):
#         return pr*(1-re)
#     return cal
# ten_per=app_dis(0.10)
# print(ten_per(200))


def greet():
    print("hello")
def dec(fun):
    def wa():
        print("before function")
        fun()
        print("after function")
    return wa
dec(greet)()


def att(fun):
    def waa():
        print("Attentens mark")
    return waa
