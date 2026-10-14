# a=2
# b=3
# print(a&b)

# print(a|b)

# print(~ b)

# print(a>>1)

# print(b<<1)

# print(bin(a&b))

# print(bin(a|b))

# print(bin(~ b))

# print(bin(a>>1))

# print(bin(b<<1))

# x=20
# y=10
# print(x+y)
# print(x-y)
# print(x*y)
# print(x+y)
# print(x/y)
# print(x%y)
# print(x//y)
# print(x**y)


# text = "python"

# print("y" in text)      # True
# print("x" in text)      # False

# print(text.index("h"))  # 3

# c=-6
# print(id(c))




items = ["Rice", "Milk", "Bread", "Soap"]
prices = [120, 80, 60, 45]

gst_rate = 0.05   # 5% GST
discount_rate = 0.10  # 10% discount

bill = 0
print("shop name=Akash genral\t\tshop NO=10 ")
print("gali No-4,Gol bazar,Raipur(C.G) ,pincode-492001")
print("\t\tSHOP BILL")
print("***************************************************")

print("Item\tPrice")

for i in range(len(items)):
    print(items[i], "\t", prices[i])
    bill += prices[i]

sub_total = bill
gst = sub_total * gst_rate
discount = sub_total * discount_rate
final_total = sub_total + gst - discount
print("***************************************************")
print("Sub Total:", sub_total)
print("GST (5%):", round(gst, 2))
print("Discount (10%):", round(discount, 2))
print("***************************************************")
print("Final Total:", round(final_total, 2))
