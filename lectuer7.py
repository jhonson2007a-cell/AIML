#string-index,slicing,method,searching,replaceing,another method.
#date-06/10/26

# name = " welcome to python programming "
# print(name)
# print(name[11:17])
# print(name[18:])
# print(name.capitalize())
# print(name.find("p"))
# print(name.upper())
# print(name.title())
# print(name.swapcase())
# print(name.strip())
# print(name.lstrip())
# print(name.rstrip())
# print(name.count("p"))



#placement quswer
# n = "welcome to python programming"
# print(len(n))
# print(n[-1:-30:-1])


# name = "jack"
# mark = 70
# print("Name:{}, Mark:{}".format(name, mark))

# s = "A-B-C"
# print(s.split("-"))
# # ['A', 'B', 'C']

# items = ['A', 'B', 'C']
# print("-".join(items))
# # A-B-C

# s = "Python"
# print(s.encode("utf-8"))

# p = "Name:\tPython"
# print(p.expandtabs(4))
# r = "report.pdf"
# print(r.removesuffix(".pdf"))


#company quswer
 


#ANSWER1
s = "hello python"
V = "AEIOUaieou"
vowels = sum(s.lower().count(v) for v in V)
print("Vowel count:", vowels)

#ANSWER2
d=input("enter the digit(only digits)=")
print(d.isdigit())

#ANSWER3
h=input("enter somethings- ")
print("word are replace space into hyphen...")
print(h.replace(" ","-"))

#ANSWER4
sp=input("enter to count by split=")
print("count=" ,len(sp.split()))

#ANSWER5
Join=["hello ","python"]
print("-".join(Join))

#ANSWER6
end=input("enter the file name:-")
print(end.endswith(".pdf"))

#ANSWER7
word=input("enter something to find inside word:-")
sr=input("enter the search character:-")
print("find character =",word.find(sr))
print("total character =",word.rfind(sr))

#ANSWER8
trimmed = "   Python programming   ".strip()
print("8. Trimmed text:", trimmed)