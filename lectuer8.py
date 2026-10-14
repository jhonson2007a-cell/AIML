#Date- 08 oct,2026
#learning about list and tuple method

#LIST
l1=[]
l2=[123,"python",3.7]
l3=[1,2,3,4,5]
l4=["c","python","java"]
mylist=["apple","banana","grev","pineapple"]
print(l1)
print(l2)
print(l3)
print(l4)
print(l3+l2)
print(l2*2)
print("py" in l4)
del l3[1]
print(l3)
del l3[1:3]
print(l3)
print(max(mylist))
print(sorted(mylist))
print(mylist.sort())
print(mylist.append("kive"))
print(mylist[0::1])


# Tuple 
t = (10, 20, 30, 20, 40)

# 1. count()
print(t.count(20))    


# 2. index()
print(t.index(30))    
print(t.index(20, 1)) 

# other tuple operations
print(len(t))         
print(max(t))         
print(min(t))        
print(sum(t))        
print(sorted(t))     
my_tuple = ("apple", "banana", "apple", "orange")

print(my_tuple.count("apple"))
print(my_tuple.index("banana")) 

s1={1,2,3}
s2={3,4,5}
s3=s2&s1
s4=s1|s2
print(s3)
print(s4)