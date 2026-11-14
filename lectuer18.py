'''date- 03/11/2026 '''
# def get_number():
#     return [1,2,3,4]
# nums=get_number()
# for n in nums:
#     print(n)

'''generator'''
'''it give value one by one on demande and you used generator by yield(produces) '''
# explem-
# def numbers():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
# x=numbers()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))  Exception has occurred: StopIteration

'''Iterator'''
'''skip every second element by using iterator '''
# from typing import Any
#  class skipIterator:
#     def __init__(self, data):
#         self.data = data
#         self.c = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.c >= len(self.data):
#             raise StopIteration
#         val = self.data[self.c]
#         self.c += 2
#         return val

# x = skipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# class repeatItem:
#     def __init__(self,item,count):
#         self.item=item
#         self.count=count
#         self.c=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.c > self.count:
#             raise StopIteration
#         val=self.item
#         self.c=self.c+1
#         return val
# print(list(repeatItem(item="hi",count=4)))


'''Resver the string by using itaration '''
# class reverseString:
#     def __init__(self,string):
#         self.string=string
#         self.count=len(self.string)-1
        
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.count<0:
#             raise StopIteration
#         val=self.string[self.count]
#         self.count=self.count-1
#         return val

# print(list(reverseString("welcome")))


def genex():
    for i in range(10):
        yield i
# print(list(genex()))  '''one method to print for one line outpuy'''
# x=genex()  '''second method line by line'''
# for y in x:
#     print(y)

'''create a custom class my sector that display the multiple of a number until 
thread show'''

# class MyMultiples:
#     def __init__(self, number, count):
#         self.number = number
#         self.count = count
#         self.current = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current > self.count:
#             raise StopIteration
#         result = self.number * self.current
#         self.current += 1
#         return result

# for multiple in MyMultiples(5,75):
#     print(multiple)

# def countdown(n):
#     while n>0:
#         yield  n;
#         n=n-1
# x=countdown(7)
# # print(list(x)) '''1 method'''
# # print(next(x)) '''2 method'''

# def even(n):
#    for i in range (n):
#        if i%2==0:
#            yield i

# print(list(even(5)))

'''Generation express'''

# y=[i for i in range (5)]
# print(y)

# x=(i for i in range (5))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# generator function to create powerof 3
def power_3(limit):
    val=1
    count=1
    while count <=limit:
        yield val
        val=val*3
        count=count
print(list(power_3(9)))

def b(n):
    i=1
    while i<=n:
        if n%i==0:
            yield True
        else:
            yield False
        i=i+1

print(list(b(9)))