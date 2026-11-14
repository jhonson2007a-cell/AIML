#Date 15oct,2026
#placement Queswer

# answer 7
# def is_armstrong(num):
#     temp = num
#     total = 0
#     power = len(str(num))

#     while temp > 0:
#         digit = temp % 10
#         total += digit ** power
#         temp //= 10
#         return total == num
# no = int(input("Enter number: "))
# if is_armstrong(no):
#     print(no," is Armstrong")
# else:
#     print(no ,"is NOT Armstrong")

# answer5
# num=int(input("enter the number:-"))
# for i in range (1,11):
#     print(num,"X",i,"=",i*num)
    
# answer1
# n = int(input("Enter a number: "))
# if n < 0:
#      print(n ," is a positive")
# elif n>0:
#      print(n," is a nagetive")
# else:
#     print(n," is a zero")

# answer2
# def sum_of_digit(num):
#     total = 0
#     tem = abs(num)
#     while tem > 0:
#         digi = tem % 10
#         total += digi
#         tem //= 10
#     return total
# No=int(input("enter the number="))
# print(sum_of_digit(No))

# answer06
# a = input("enter the element to find palindrome:- ")
# if a == a[::-1]:
#      print("element is a palindrome")
# else:
#      print("element is not a palindrome")

# answer7
# s = input("enter the String=")
# V = "AEIOUaieou"
# vowels = sum(s.lower().count(v) for v in V)
# print("Vowel count:", vowels)

# anwser 8
# s=input("enter the string for count=")
# print("lower case=", sum(1 for char in s if char.islower()))
# print("upper case=", sum(1 for char in s if char.isupper()))
# print("upper case=", sum(1 for char in s if char.isdigit()))

# answer 11
# list=[12, 5, 30, 8, 2]
# print("Largest=", max(list))
# print("Smallest=",min(list))

# answer19
# words = input("Enter words separated by spaces: ").split()
# groups = {}
# for word in words:
#     first = word[0].lower()
#     groups.setdefault(first, []).append(word)
# print(groups)

# answer13
# numbers = [12, 5, 30, 8, 2]
# un = sorted(set(numbers), reverse=True)
# if len(un) >= 2:
#     print("Second largest =", un[1])
# else:
#     print("There is no second-largest distinct number.")

#3
# def reverse_number(num):
#     rev = 0
#     temp = abs(num)
#     while temp > 0:
#         rev = rev * 10 + temp % 10
#         temp //= 10
#     return rev if num >= 0 else -rev

# n = int(input())
# print(reverse_number(n))

#9
# def is_anagram(s1, s2):
#     return sorted(s1.lower()) == sorted(s2.lower())

# s1 = input()
# s2 = input()
# if is_anagram(s1, s2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")

# #10
# def first_non_repeat(s):
#     for ch in s:
#         if s.count(ch) == 1:
#             return ch
#     return "No non-repeating character"

# s = input()
# print(first_non_repeat(s))

# #12
# def move_zeros(lst):
#     non_zero = [x for x in lst if x != 0]
#     zero = [x for x in lst if x == 0]
#     return non_zero + zero
# lst = [0, 1, 0, 3, 12]
# print(move_zeros(lst))

# #14
# def common_elements(a, b):
#     return list(set(a) & set(b))
# a = [1, 2, 2, 3, 4]
# b = [2, 3, 3, 5]
# print(common_elements(a, b))

# #16
# def frequency(lst):
#     freq = {}
#     for i in lst:
#         freq[i] = freq.get(i, 0) + 1
#     return freq
# print(frequency([1, 2, 2, 3, 3, 3]))


# #15
# def find_missing(lst, n):
#     expected_sum = n * (n + 1) // 2
#     return expected_sum - sum(lst)

# print(find_missing([1, 2, 4, 5], 5))


# #20
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# print(gcd(12, 18))

# #17
# def max_key(d):
#     return max(d, key=d.get)

# marks = {"Amit": 75, "Riya": 92, "Neha": 85}
# print(max_key(marks))


# #18
# def merge_dict(a, b):
#     result = a.copy()
#     for k, v in b.items():
#         result[k] = result.get(k, 0) + v
#     return result

# a = {"x": 10, "y": 20}
# b = {"y": 5, "z": 30}
# print(merge_dict(a, b))

# #25
# import random
# for _ in range(5):
#     print(random.randint(1, 100))