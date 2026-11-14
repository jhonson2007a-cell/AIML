#date-13oct,2026
# def add(a, b):
#     return a + b
# def mul(a, b):
#     return a * b
# def sub(a,b):
#     return a-b
# def div(a,b):
#     return a/b
# def mod(a,b):
#     return a%b

def feran(c):
    return (c*9/5)+32

def is_armstrong(num):
    # Armstrong = sum of cubes of digits = number. Ex: 153 = 1^3+5^3+3^3
    temp = num
    total = 0
    power = len(str(num))

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10

    return total == num

# Main
n = int(input("Enter number: "))
if is_armstrong(n):
    print(f"{n} is Armstrong")
else:
    print(f"{n} is NOT Armstrong")

# Test: 153, 370, 371, 407 are Armstrong