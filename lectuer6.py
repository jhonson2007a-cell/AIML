# lectuer6 date-01 oct, 2026

# n = int(input("Enter a number: "))

# if n < 2:
#     print(n ," is not a prime number")
# else:
#     is_prime = True
#     for divisor in range(2, int(n**0.5) + 1):
#         if n % divisor == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("number is a prime number")
#     else:
#         print("number is not a prime number")

# palindrome number
# a = input("enter the element to find palindrome:- ")

# if a == a[::-1]:
#     print("element is a palindrome")
# else:
#     print("element is not a palindrome")


#factorial
# b = int(input("enter the number:-"))
# fact = 1
# for i in range(1, b + 1):
#     fact=fact* i
# print("Factorial of",b,"=", fact)

#febonacci serice
# c=int(input("enter the number:-"))
# febo=0
# a , b = 0, 1
# for i in range(c):
#     print(a, end=" ")
#     a, b = b, a + b
# print()
   

#armstrong 
# num = int(input("Enter a number: "))
# original = num
# digits = len(str(num))
# total = 0
# while num > 0:
#     digit = num % 10
#     total =total+ digit ** digits
#     num =num// 10
# if total == original:
#     print(original, "is an Armstrong number")
# else:
#     print(original, "is not an Armstrong number")