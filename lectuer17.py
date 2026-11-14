'''date-31 Oct,2026'''

'''Iterator'''
# x=[10,20,30,40]
# i=iter(x)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# # print(next(i))

# class poweroftwo:
#     def __init__(self,limit):
#         self.limit=limit
#         self.curr=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.curr>self.limit:
#             raise StopIteration
#         val=self.curr
#         self.curr*=2
#         return val
# print(list(poweroftwo(8)))
 
# class skipiter:
#     def __init__(self,lst) :
#         self.index=0
#         self.length=len(lst)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<=self.length:
#             val=lst[self.index]
#             self.index=self.index+2
#             return val
#         else:
#             raise StopIteration   


# class skipiter:
#     def __init__(self, lst):
#         self.lst = lst
#         self.index = 0
#         self.length = len(lst)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index < self.length:
#             val = self.lst[self.index]
#             self.index += 2
#             return val
#         else:
#             raise StopIteration