# date-30oct,2026
#Data fram

# x=[i for i in range(1,201) if i%2==0]
# print(x)


'''lambda function'''
# def mysqr(a):
#     return a**2
# print(mysqr(5))

# sq=lambda x:x**2
# print(sq(4))

# print((lambda a,b:a+b)(5,3))

# add=lambda a,b:a+b
# print(add(5,3))

# even=lambda n : n%2==0
# print(even(4))

# upper=lambda s:s.upper()
# print(upper("hello"))

# mul_pi=lambda pi:pi*2
# print(mul_pi(3.14))


'''map function'''
# print(list(map(lambda X:X*2,[1,2,3])))

# print(list(map(str.upper, ["h", "e", "l", "l", "o"])))

# print(list(map(str.upper, ["hello","all","of","you"])))

# print(list(map(lambda x:x+10,[1,2,3,4])))

# print(list(map(str.__len__, ["hello","all","of","you"])))

# print(list(map(lambda x:len(x), ["hello","all","of","you"])))



'''Filter'''
# print(list(filter(lambda x:x%2==0,[1,2,3,4])))

# print(list(filter(lambda x:x>0,[-1,-2,0,1,2])))

# print(list(filter(None,["apple","banana",""])))

# print(list(filter(lambda s: s.startswith("a"),["hello","ameazing"])))



'''reduce funtion'''
# from functools import reduce
# print(reduce(lambda a, b: a + b, [1, 2, 3, 4]))

# print(reduce(lambda n,m: n*m, [1, 2, 3, 4]))

# print(list(reduce(lambda x,y: x+y,["a","b","c"])))

# print(reduce(lambda n,m: n if n>m else m , [1, 2, 3, 4]))

# print(reduce(lambda a, b: a + b, [1, 2, 3],10))


'''comprehension'''
'''list'''
# print([x**2 for x in range(3)])

'''dict'''
# print({x:x**2 for x in range(3)})

'''set'''
# print({x%2 for x in range(4)})

'''nested list 2*2 grid'''
# print([[i for i in range(2)] for _ in range(2)])
'''nested list 3*2 grid'''
# print([[i,j] for i in range(3) for j in range(2)])


'''Hingher order function'''
# def apply_func(f,x):
#     return f(x)
# print(apply_func(lambda x:x*10,3))

# def make_mul(n):
#     return lambda x:x*n
# double=make_mul(2)
# print(double(5))

# l=[34,23,65,13,87,30]
# print(l)
# print(sorted(l))

'''sorted() with custom key'''
# print(sorted([("h",3),("b",10)],key= lambda x:x[1]))


'''iterators and genrators'''
"list iterator"
# for x in[1,2]:
#     print(x,end="")
    
# l=iter([1,2])
# print(next(l))

"string"
# for c in "hi":
#     print(c,end="")

"dict"

'''date-31 Oct,2026'''

# ends_with_dot=lambda  s:s.endswith(".")
# print(ends_with_dot("Hello."))

# tips=lambda bill:round(bill*.15,2)
# print(tips(2000))

'''map'''
# print(list(map(lambda X:X-5,[10,20,30])))

# print(list(map(abs,[-1,2,-3,4])))
# print(list(map(lambda x: -x if x < 0 else x, [-1, 2, -3, 4])))

# print(list(map(lambda s: s[::-1], ["dog", "cat", "sun"])))

# print(list(filter(lambda s:s.startswith("b"),["bat","cat","ball","dog"])))
# print(list(filter(lambda x: x < 10, [5, 12, 3, 15, 4])))

'''reduce'''

from functools import reduce
# print(reduce(lambda a, b: a if a < b else b, [15, 3, 22, 8]))

# print(reduce(lambda a, b: f"{a}-{b}",["python","is","fun"]))

# print(reduce(lambda total, word: total + len(word), ["hi", "world"], 0))

# print([len(x) for x in ["apple","kiwi","pear"]])

# print([len(w) for w in {"sun","moon"}])

# print([x[0] for x in {"apple","apricot","banana"}])

# print({x[0] for x in ["apple","apricot","banana"]})

# print([x for x in range(1,10) if x%3==0])

'''HOD'''

# def mymap(f,li):
#     return [f(x)for x in li]
# print(mymap(lambda x:x+1,[1,2,3]))

def apptwic(func,x):
    return func(func(x))
print(apptwic(lambda x:x+3,5))