# Date: 09 Oct 2026
# Set methods in Python


# items = {1, 2, 3}
# other = {3, 4, 5}

# Add or remove items
# items.add(4)
# items.update([5, 6])
# items.remove(1)       
# items.discard(99)     
# removed = items.pop() 

# Make or empty a set
# items_copy = items.copy()
# items_copy.clear()

# Set operations (return new sets)
# print(items.union(other))                 
# print(items.intersection(other))          
# print(items.difference(other))             
# print(items.symmetric_difference(other))   

# In-place set operations (change items)
# items.update(other)
# items.intersection_update(other)
# items.difference_update(other)
# items.symmetric_difference_update(other)

# Relationship checks (return True or False)
# print(items.isdisjoint(other)) 
# print(items.issubset(other))   
# print(items.issuperset(other)) 


# Mini project: Student marks and result management using a dictionary

students = {}

while True:
    print("\n1. Add student marks")
    print("2. Show results")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        math = int(input("Enter Math marks: "))
        science = int(input("Enter Science marks: "))
        english = int(input("Enter English marks: "))

        students[name] = {
            "Math": math,
            "Science": science,
            "English": english
        }
        print("Student marks saved.")

    elif choice == "2":
        for name, marks in students.items():
            total = marks['Math'] + marks['Science'] + marks['English']
            average = total / 3

            print("\nStudent:", name)
            print("Marks:", marks)
            print("Total:", total)
            print("Average:", average)

            if average >= 40:
                print("Result: Pass")
                if average>=86:
                    print("PASS With A+")
                elif average>=80:
                    print("PASS With A")
                elif average>=75:
                    print("PASS With B+")
                elif average>=70:
                    print("PASS With B")
                elif average>=56:
                    print("PASS With C")
                else:
                    print("PASS With D")
            else:
                print("Result: Fail")

    elif choice == "3":
        break

    else:
        print("\n1. Add student marks")
        print("2. Show results")
        print("3. Exit")
        print("Please choose 1, 2, or 3.")
     


#data sturcture in youtube 