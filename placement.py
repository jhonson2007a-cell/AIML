answer 7
def is_armstrong(num):
    temp = num
    total = 0
    power = len(str(num))

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
        return total == num
no = int(input("Enter number: "))
if is_armstrong(no):
    print(no," is Armstrong")
else:
    print(no ,"is NOT Armstrong")

answer5
num=int(input("enter the number:-"))
for i in range (1,11):
    print(num,"X",i,"=",i*num)
    
answer1
n = int(input("Enter a number: "))
if n < 0:
     print(n ," is a positive")
elif n>0:
     print(n," is a nagetive")
else:
    print(n," is a zero")

answer2
def sum_of_digit(num):
    total = 0
    tem = abs(num)
    while tem > 0:
        digi = tem % 10
        total += digi
        tem //= 10
    return total
No=int(input("enter the number="))
print(sum_of_digit(No))

answer06
a = input("enter the element to find palindrome:- ")
if a == a[::-1]:
     print("element is a palindrome")
else:
     print("element is not a palindrome")

answer7
s = input("enter the String=")
V = "AEIOUaieou"
vowels = sum(s.lower().count(v) for v in V)
print("Vowel count:", vowels)

anwser 8
s=input("enter the string for count=")
print("lower case=", sum(1 for char in s if char.islower()))
print("upper case=", sum(1 for char in s if char.isupper()))
print("upper case=", sum(1 for char in s if char.isdigit()))

answer 11
list=[12, 5, 30, 8, 2]
print("Largest=", max(list))
print("Smallest=",min(list))

answer19
words = input("Enter words separated by spaces: ").split()
groups = {}
for word in words:
    first = word[0].lower()
    groups.setdefault(first, []).append(word)
print(groups)

answer13
numbers = [12, 5, 30, 8, 2]
un = sorted(set(numbers), reverse=True)
if len(un) >= 2:
    print("Second largest =", un[1])
else:
    print("There is no second-largest distinct number.")
