#QUESTION 1
student = {
    "name": "Ram",
    "age": 20,
    "course": "Python",
    "city": "Kathmandu"
}

# 1. Complete dictionary
print(student)

# 2. Name
print(student["name"])

# 3. Age
print(student["age"])

# 4. Course
print(student["course"])

# 5. City
print(student["city"])

#QUESTION 2

student = {
    "name": "Sita",
    "age": 21,
    "course": "Python"
}

# 1. Add city
student["city"] = "Pokhara"

# 2. Add grade
student["grade"] = "A"

# 3. Change age
student["age"] = 22

# 4. Change course
student["course"] = "Data Science"

# 5. Print updated dictionary
print(student)

#QUESTION 3

employee = {
    "name": "John",
    "age": 30,
    "department": "IT",
    "salary": 50000,
    "city": "Kathmandu"
}

# 1. Remove age
del employee["age"]

# 2. Remove city
del employee["city"]

# 3. Print dictionary
print(employee)

# 4. Safely try to remove email
employee.pop("email", None)

print(employee)

#QUESTION 4
book = {
    "title": "Python Basics",
    "author": "John Smith",
    "year": 2025,
    "price": 500
}

# 1. All keys
print(book.keys())

# 2. All values
print(book.values())

# 3. All key-value pairs
print(book.items())

# Display dictionary using a loop
for key, value in book.items():
    print(key, "=", value)


#QUESTION 5
student = {
    "name": "Hari",
    "age": 19,
    "course": "Python",
    "city": "Lalitpur"
}

key = input("Enter a key: ")

if key in student:
    print(key, "exists in the dictionary.")
else:
    print(key, "does not exist in the dictionary.")

#QUESTION 6
marks = {
    "Ram": 75,
    "Sita": 88,
    "Hari": 65,
    "Gita": 92,
    "John": 55
}

# 1. Print all students and marks
for name, mark in marks.items():
    print(name, "-", mark)

# 2. Total marks
total = sum(marks.values())
print("Total:", total)

# 3. Average
average = total / len(marks)
print("Average:", average)

# 4. Highest mark
highest = max(marks.values())
print("Highest:", highest)

# 5. Lowest mark
lowest = min(marks.values())
print("Lowest:", lowest)

# 6. Student with highest mark
for name, mark in marks.items():
    if mark == highest:
        print("Highest student:", name)


#QUESTION 7
fruits = [
    "apple", "banana", "apple",
    "orange", "banana", "apple",
    "mango", "orange", "banana"
]

count = {}

for fruit in fruits:
    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1

print(count)

#QUESTION 8
product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 75000,
    "quantity": 5
}

# 1. Product name and brand
print("Name:", product["name"])
print("Brand:", product["brand"])

# 2. Price
print("Price:", product["price"])

# 3. Quantity
print("Quantity:", product["quantity"])

# 4. Total value
total = product["price"] * product["quantity"]
print("Total value:", total)

# Sell 2 laptops
product["quantity"] = product["quantity"] - 2

print("Updated quantity:", product["quantity"])

#QUESTION 9

students = {
    101: {
        "name": "Ram",
        "age": 20,
        "course": "Python"
    },
    102: {
        "name": "Sita",
        "age": 21,
        "course": "Java"
    },
    103: {
        "name": "Hari",
        "age": 19,
        "course": "Python"
    }
}

# 1. Display all students
print(students)

# 2. Display student 102
print(students[102])

# 3. Change student 103's course
students[103]["course"] = "Data Science"

# 4. Add student 104
students[104] = {
    "name": "Gita",
    "age": 20,
    "course": "Python"
}

# 5. Remove student 101
del students[101]

# 6. Display final dictionary
print(students)

#QUESTION 10
contacts = {
    "Ram": "9841000000",
    "Sita": "9851000000",
    "Hari": "9861000000"
}

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # 1. Add contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact added successfully.")

    # 2. Search contact
    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")

    # 3. Update contact
    elif choice == "3":
        name = input("Enter name to update: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    # 4. Delete contact
    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    # 5. Display contacts
    elif choice == "5":
        for name, phone in contacts.items():
            print(name, "-", phone)

    # 6. Exit
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

